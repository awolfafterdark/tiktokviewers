import requests, time, json, urllib.parse, random, threading
from pystyle import Colorate, Colors, Write, Add, Center
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse, urlencode
import ssl
import queue
import re
import os
import hashlib

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r = requests.Session()
countQueue = queue.Queue()
sentRequests = 0
completed = False

r.cookies.set_policy(BlockCookies())

class Gorgon:
    def __init__(self, params: str, data: str, cookies: str, unix: int) -> None:
        self.unix = unix
        self.params = params
        self.data = data
        self.cookies = cookies

    def hash(self, data: str) -> str:
        try:
            _hash = str(hashlib.md5(data.encode()).hexdigest())
        except Exception:
            _hash = str(hashlib.md5(data).hexdigest())
        return _hash

    def get_base_string(self) -> str:
        base_str = self.hash(self.params)
        base_str = base_str + self.hash(self.data) if self.data else base_str + str('0' * 32)
        base_str = base_str + self.hash(self.cookies) if self.cookies else base_str + str('0' * 32)
        return base_str

    def get_value(self) -> json:
        base_str = self.get_base_string()
        return self.encrypt(base_str)

    def encrypt(self, data: str) -> json:
        unix = self.unix
        len = 20
        key = [223, 119, 185, 64, 185, 155, 132, 131, 209, 185, 203, 209, 247, 194, 185, 133, 195, 208, 251, 195]
        param_list = []
        for i in range(0, 12, 4):
            temp = data[8 * i:8 * (i + 1)]
            for j in range(4):
                H = int(temp[j * 2:(j + 1) * 2], 16)
                param_list.append(H)
        param_list.extend([0, 6, 11, 28])
        H = int(hex(unix), 16)
        param_list.append((H & 4278190080) >> 24)
        param_list.append((H & 16711680) >> 16)
        param_list.append((H & 65280) >> 8)
        param_list.append((H & 255) >> 0)
        eor_result_list = []
        for (A, B) in zip(param_list, key):
            eor_result_list.append(A ^ B)
        for i in range(len):
            C = self.reverse(eor_result_list[i])
            D = eor_result_list[(i + 1) % len]
            E = C ^ D
            F = self.rbit_algorithm(E)
            H = (F ^ 4294967295 ^ len) & 255
            eor_result_list[i] = H
        result = ''
        for param in eor_result_list:
            result += self.hex_string(param)
        return {'X-Gorgon': '0404b0d30000' + result, 'X-Khronos': str(unix)}

    def rbit_algorithm(self, num):
        result = ''
        tmp_string = bin(num)[2:]
        while len(tmp_string) < 8:
            tmp_string = '0' + tmp_string
        for i in range(0, 8):
            result = result + tmp_string[7 - i]
        return int(result, 2)

    def hex_string(self, num):
        tmp_string = hex(num)[2:]
        if len(tmp_string) < 2:
            tmp_string = '0' + tmp_string
        return tmp_string

    def reverse(self, num):
        tmp_string = self.hex_string(num)
        return int(tmp_string[1:] + tmp_string[:1], 16)

def view(video):
    for x in range(10):
        try:
            version = random.choice([247, 312, 322, 357, 358, 415, 422, 444, 466])
            device = random.choice([
                "SM-G9900", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B",
                "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B", "SM-A525F"
            ])
            host = random.choice([
                "api22-core-c-useast1a.tiktokv.com", "api19-core-c-useast1a.tiktokv.com",
                "api16-core-c-useast1a.tiktokv.com", "api21-core-c-useast1a.tiktokv.com"
            ])

            params = urlencode({
                "app_language": "fr",
                "iid": "IID",
                "device_id": "DID",
                "channel": "googleplay",
                "device_type": device,
                "ac": "wifi",
                "os_version": random.randint(5, 11),
                "version_code": version,
                "app_name": "trill",
                "device_brand": "samsung",
                "ssmix": "a",
                "device_platform": "android",
                "aid": 1180
            })

            payload = f"item_id={video}&play_delta=1"
            sig = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()

            response = r.post(
                url="https://" + host + "/aweme/v1/aweme/stats/?" + params,
                data=payload,
                headers={
                    'cookie': 'sessionid=90c38a59d8076ea0fbc01c8643efbe47',
                    'x-gorgon': sig['X-Gorgon'],
                    'x-khronos': sig['X-Khronos'],
                    'user-agent': f'com.ss.android.ugc.trill/{version} (Linux; U; Android 11; fr_FR; {device}; Build/RP1A.200720.012; Cronet/58.0.2991.0)'
                },
                verify=False
            )

            try:
                if response.json().get('status_code') == 0:
                    print(f'Success: View incremented for video {video}')
            except:
                continue

        except Exception as e:
            pass

if __name__ == "__main__":
    try:
        link = input("Enter video link: ")
        video = str(re.findall(r"(\d{18,19})", link)[0] if len(re.findall(r"(\d{18,19})", link)) == 1 else
                         re.findall(r"(\d{18,19})", requests.head(link, allow_redirects=True, timeout=5).url)[0])
    except:
        exit("Invalid link")

    os.system('cls' if os.name == 'nt' else 'clear')

    view(video)
