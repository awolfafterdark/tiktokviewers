import requests, time, json, urllib.parse, random, threading
from pystyle import Colorate, Colors, Write, Add, Center
#7138367478103574021 7138368303832090374
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
import ssl
import queue
class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r                                 = requests.Session()
countQueue                        = queue.Queue()
sentRequests                      = 0
completed                         = False

r.cookies.set_policy(BlockCookies())
import requests, time, json, urllib.parse, random, threading
link = input(
        Col.purple + "{" + Col.reset + "?" + Col.purple + "}" + Col.reset + " Enter video link " + Col.purple + "[" + Col.reset + "press " + Col.blue + "Enter" + Col.reset + " to start" + Col.purple + "]" + Col.reset + " -> ")

video = str(re.findall(r"(\d{18,19})", link)[0] if len(re.findall(r"(\d{18,19})", link)) == 1 else
                     re.findall(r"(\d{18,19})", requests.head(link, allow_redirects=True, timeout=5).url)[0])
os.system('cls' if os.name == 'nt' else 'clear')

def view(video):
    global reqs, _lock, success, fails, rps, rpm

    for x in range(10):
        try:
            ve = random.choice(
                [247, 312, 322, 357, 358, 415, 422, 444, 466]
            )

            device = random.choice(
                ["SM-G9900", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B",
                 "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B",
                 "SM-A525F"]
            )
            host = random.choice(["api22-core-c-useast1a.tiktokv.com", "api19-core-c-useast1a.tiktokv.com",
                                  "api16-core-c-useast1a.tiktokv.com", "api21-core-c-useast1a.tiktokv.com"])

            params = urllib.parse.urlencode(
                {
                    "os_api": "25",
                    "device_type": device,
                    "ssmix": "a",
                    "manifest_version_code": ve,
                    "dpi": "240",
                    "region": "VN",
                    "carrier_region": "VN",
                    "app_name": "musically_go",
                    "version_name": "27.2.4",
                    "timezone_offset": "-28800",
                    "ab_version": "27.2.4",
                    "ac2": "wifi",
                    "ac": "wifi",
                    "app_type": "normal",
                    "channel": "googleplay",
                    "update_version_code": ve,
                    "device_platform": "android",
                    "iid": IID,
                    "build_number": "27.2.4",
                    "locale": "vi",
                    "op_region": "VN",
                    "version_code": ve,
                    "timezone_name": "Asia/Ho_Chi_Minh",
                    "device_id": DID,
                    "sys_region": "VN",
                    "app_language": "vi",
                    "resolution": "720*1280",
                    "device_brand": "samsung",
                    "language": "vi",
                    "os_version": "7.1.2",
                    "aid": "1340"
                }
            )

            payload = f"item_id={video}&play_delta=1"
            sig = Gorgon(params=params, cookies=None, data=None, unix=int(time.time())).get_value()

            response = r.post(
                url=(
                    "https://"
                    + host +
                    "/aweme/v1/aweme/stats/?" + params
                ),
                data=payload,
                headers={
                    'cookie': 'sessionid=90c38a59d8076ea0fbc01c8643efbe47',
                    'x-gorgon': sig['X-Gorgon'],
                    'x-khronos': sig['X-Khronos'],
                    'user-agent': f"com.ss.android.ugc.trill/{ve} (Linux; U; Android 11; fr_FR; {device}; Build/RP1A.200720.012; Cronet/58.0.2991.0)"
                },
                verify=False
            )

            reqs += 1
            try:
                if response.json()['status_code'] == 0:
                    _lock.acquire()
                    print(f'[GUINNESS][BUFF VIEW SUCCESS] +: {success} View')
                    success += 1
                    _lock.release()
            except:
                if _lock.locked():
                    _lock.release()
                fails += 1
                continue

        except Exception as e:
            pass
