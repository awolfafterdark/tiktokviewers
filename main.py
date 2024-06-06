import requests
import ssl
import re
import cursor

cursor.hide()
import requests, time, json, urllib.parse, random, threading
import ssl
import requests, time, json, urllib.parse, random, threading,hashlib

import time
import queue
import threading
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from pystyle import *
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
from xgorgon import Gorgon
from device_gen import *
import time
from random import choice, randint, shuffle
try:
  from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except:
  os.system('pip install pystyle')
from os.path import isfile

text = """
                                         do.
                                        :NOX
                                       ,NOM@:
                                       :NNNN:
                                       :XXXON
                                       :XoXXX.
                                       MM;ONO:
  .oob..                              :MMO;MOM
 dXOXYYNNb.                          ,NNMX:MXN
 Mo"'  '':Nbb                        dNMMN MNN:
 Mo  'O;; ':Mb.                     ,MXMNM MNX:
 @O :;XXMN..'X@b.                  ,NXOMXM MNX:
 YX;;NMMMM@M;;OM@o.                dXOOMMN:MNX:
 'MOONM@@@MMN:':NONb.            ,dXONM@@MbMXX:
  MOON@M@@MMMM;;:OOONb          ,MX'"':ONMMMMX:
  :NOOM@@MNNN@@X;""XNN@Mb     .dP"'   ,..OXM@N:
   MOON@@MMNXXMMO  :M@@M...@o.oN"0MQOOOXNNXXOo:
   :NOX@@@MNXXXMNo :MMMM@K"`,:;NNM@@NXM@MNO;.'N.
    NO:X@@MNXXX@@O:'X@@@@MOOOXMM@M@NXXN@M@NOO ''b
    `MO.'NMNXXN@@N: 'XXM@NMMXXMM@M@XO"'"XM@X;.  :b
     YNO;'"NXXXX@M;;::"XMNN:""ON@@MO: ,;;.:Y@X: :OX.
      Y@Mb;;XNMM@@@NO: ':O: 'OXN@@MO" ONMMX:`XO; :X@.
      '@XMX':OX@@MN:    ;O;  :OX@MO" 'OMM@N; ':OO;N@N
       YN;":.:OXMX"': ,:NNO;';XMMX:  ,;@@MNN.'.:O;:@X:
       `@N;;XOOOXO;;:O;:@MOO;:O:"" ,oMP@@K"YM.;NMO;`NM
        `@@MN@MOX@@MNMN;@@MNXXOO: ,d@NbMMP'd@@OX@NO;.'bb.
       .odMX@@XOOM@M@@XO@MMMMMMNNbN"YNNNXoNMNMO"OXXNO.."";o.
     .ddMNOO@@XOOM@@XOONMMM@@MNXXMMo;."' .":OXO ':.'"'"'  '""o.
    'N@@X;,M@MXOOM@OOON@MM@MXOO:":ONMNXXOXX:OOO               ""ob.
   ')@MP"';@@XXOOMMOOM@MNNMOO""   '"OXM@MM: :OO.        :...';o;.;Xb.
  .@@MX" ;X@@XXOOM@OOXXOO:o:'      :OXMNO"' ;OOO;.:     ,OXMOOXXXOOXMb
 ,dMOo:  oO@@MNOON@N:::"      .    ,;O:."'  .dMXXO:    ,;OX@XO"":ON@M@
:Y@MX:.  oO@M@NOXN@NO. ..: ,;;O;.       :.OX@@MOO;..   .OOMNMO.;XN@M@P
,MP"OO'  oO@M@O:ON@MO;;XO;:OXMNOO;.  ,.;.;OXXN@MNXO;.. oOX@NMMN@@@@@M:
`' "O:;;OON@@MN::XNMOOMXOOOM@@MMNXO:;XXNNMNXXXN@MNXOOOOOXNM@NM@@@M@MP
   :XN@MMM@M@M:  :'OON@@XXNM@M@MXOOdN@@@MM@@@@MMNNXOOOXXNNN@@M@MMMM"
   .oNM@MM@ONO'   :;ON@@MM@MMNNXXXM@@@@M@PY@@MMNNNNNNNNNNNM@M@M@@P'
  ;O:OXM@MNOOO.   'OXOONM@MNNMMXON@MM@@b. 'Y@@@@@@@@@@@@@M@@MP"'
 ;O':OOXNXOOXX:   :;NMO:":NMMMXOOX@MN@@@@b.:M@@@M@@@MMM@
 :: ;"OOOOOO@N;:  'ON@MO.'":""OOOO@@NNMN@@@. Y@@@MMM@@@@b
 :;   ':O:oX@@O;;  ;O@@XO'   "oOOOOXMMNMNNN@MN""YMNMMM@@MMo.
 :N:.   ''oOM@NMo.::OX@NOOo.  ;OOOXXNNNMMMNXNM@bd@MNNMMM@MM@bb    @GUINNESSGSHEP
  @;O .  ,OOO@@@MX;;ON@NOOO.. ' ':OXN@NNN@@@@@M@@@@MNXNMM@MMM@,
  M@O;;  :O:OX@@M@NXXOM@NOO:;;:,;;ON@NNNMM'`"@@M@@@@@MXNMMMMM@N
  N@NOO;:oO;O:NMMM@M@OO@NOO;O;oOOXN@NNM@@'   `Y@NM@@@@MMNNMM@MM
  ::@MOO;oO:::OXNM@@MXOM@OOOOOOXNMMNNNMNP      ""MNNM@@@MMMM@MP
    @@@XOOO':::OOXXMNOO@@OOOOXNN@NNNNNNNN        '`YMM@@@MMM@P'
    MM@@M:'''' O:":ONOO@MNOOOOXM@NM@NNN@P            "`SHEP'
    ''MM@:     "' 'OOONMOYOOOOO@MM@MNNM"
      YM@'         :OOMN: :OOOO@MMNOXM'
      `:P           :oP''  "'OOM@NXNM'
       `'                    GUINNESS' 
"""
Anime.Fade(Center.Center(text), Colors.red_to_blue, Colorate.Vertical, enter=True)
def banner():
 banner = f"""


d888888b d888888b db   dD d888888b  .d88b.  db   dD            db    db d888888b d88888b db   d8b   db 
`~~88~~'   `88'   88 ,8P' `~~88~~' .8P  Y8. 88 ,8P'            88    88   `88'   88'     88   I8I   88 
   88       88    88,8P      88    88    88 88,8P              Y8    8P    88    88ooooo 88   I8I   88 
   88       88    88`8b      88    88    88 88`8b     C8888D   `8b  d8'    88    88~~~~~ Y8   I8I   88 
   88      .88.   88 `88.    88    `8b  d8' 88 `88.             `8bd8'    .88.   88.     `8b d8'8b d8' 
   YP    Y888888P YP   YD    YP     `Y88P'  YP   YD               YP    Y888888P Y88888P  `8b8' `8d8'  
      
                                Tool Buff View TikTok Version Python 2024
                         
                                    TikTok: guinnessgshep

"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush()

banner()
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
class BytedanceFuck:
    def __init__(self, __aweme_id) -> None:
        self.__aweme_id = __aweme_id
        self.__success = 0
        self.__errors = 0
        self.__devices = 0
        self.__device = 0
        self.__version = "2.0"
        self.__lock = threading.Lock()
        self.__devices = ["SM-G9900", "SM-A136U1", "SM-M225FV", "SM-E426B", "SM-M526BR", "SM-M326B", "SM-A528B",
                          "SM-F711B", "SM-F926B", "SM-A037G", "SM-A225F", "SM-M325FV", "SM-A226B", "SM-M426B",
                          "SM-A525F"]
        self.__domains = ["api22-core-c-useast1a.tiktokv.com", "api19-core-c-useast1a.tiktokv.com",
                          "api16-core-c-useast1a.tiktokv.com", "api21-core-c-useast1a.tiktokv.com"]
        self.__versions = ["190303", "190205", "190204", "190103", "180904", "180804", "180803", "180802"]
        self.__client = requests.Session()
        self.__proxies = open("proxies.txt", "r").read().splitlines()        
        self.__client.cookies.set_policy(BlockCookies())
    def __safe_print(self, arg):
        self.__lock.acquire()
        print(arg)
        self.__lock.release()
    def __send_request(self, __device_id, __install_id):
        try:
            proxy = random.choice(self.__proxies)
            params = urlencode(
                {
                    "device_id": __device_id,
                    "iid": __install_id,

                    "device_type": random.choice(self.__devices),
                    "app_name": "musical_ly",
                    "host_abi": "armeabi-v7a",
                    "channel": "googleplay",
                    "device_platform": "android",
                    "version_code": random.choice(self.__versions),
                    "device_brand": "samsung",
                    "os_version": random.randint(6, 9),
                    "aid": 1233,
                }
            )
            payload = urlencode(
                {
                    "item_id": self.__aweme_id,
                    "play_delta": 1
                }
            )
            sig = Gorgon(params, payload, None).get_value()
            response = self.__client.post(
                url=(
                        "https://"
                        + random.choice(self.__domains)
                        + "/aweme/v1/aweme/stats/?"
                        + params
                ),
                headers={
                    "x-gorgon": sig["X-Gorgon"],
                    "x-khronos": sig["X-Khronos"],
                    "user-agent": "okhttp/3.10.0.1",
                },
                data=payload,
                proxies={
                    'http': f'http://{proxy}',
                    'https': f'http://{proxy}'
                },
                verify=False
            )
            try: 
             if response.json()['status_code'] == 0:
                self.__success += 1
                self.__safe_print(f" \033[1;93m~ Views sent: "+Col.purple+"["+Col.reset+f"{self.__success}"+Col.purple+"]"+Col.blue+" </>"+Col.lblue+f" {str(response.json()['log_pb']['impr_id']).lower()}")
             else:
                self.__errors += 1
            except:
             pass
        except Exception as e:
           pass
    def __view_loop(self, __device_id, __install_id):
     while True:
      for x in range (100000000000000):
        __thread_contition = 0
        while __thread_contition < 2000:
            if threading.active_count() < 1000:
                threading.Thread(target=self.__send_request, args=[__device_id, __install_id]).start()
                __thread_contition += 1
    def __device_loop(self):
        while True:
            try:
                proxy = random.choice(self.__proxies)
                __start = time.time()
                device: dict = Device().create_device()
                __device_id, __install_id = Applog(device, proxy).register_device()
                Xlog(__device_id, proxy).bypass()
                self.__device += 1
                #print(
                   # Col.purple + "{" + Col.reset + "*" + Col.purple + "}" + Col.reset + f"{Col.reset} Generated device {Col.blue}! {Col.purple}[{Col.blue}{__device_id} {Col.reset}|{Col.blue} {__install_id}{Col.purple}] {Col.purple}[{Col.reset}Execution time: {Col.blue}{round(time.time() - __start, 1)}s{Col.purple}]{Col.reset}")
                print(f" \033[1;93m~ [LQM] \033[1;94m=> \033[1;95m[{__device_id}] \033[1;96m</> \033[1;97m[{__install_id}] ")
                print('- '*25)
                
                threading.Thread(
                    target=self.__view_loop,
                    args=[
                        __device_id, __install_id
                    ]
                ).start()

            except Exception as e:
                print(e)
                continue

    def start(self):
     #while True:
     # for v in range(10000000000):
        for x in range(1):
            threading.Thread(target=self.__device_loop).start()
def init():
    os.system(f'cls' if os.name == 'nt' else 'clear')
    banner()
    link = input(
        Col.purple + "{" + Col.reset + "LQM" + Col.purple + "}" + Col.reset + " Nhập link video" + Col.purple + "[" + Col.reset + "Nhập xong bấm " + Col.blue + "Enter" + Col.reset + " để bắt đầu" + Col.purple + "]" + Col.reset + " -> ")

    __aweme_id = str(re.findall(r"(\d{18,19})", link)[0] if len(re.findall(r"(\d{18,19})", link)) == 1 else
                     re.findall(r"(\d{18,19})", requests.head(link, allow_redirects=True, timeout=5).url)[0])
    os.system('cls' if os.name == 'nt' else 'clear')
    print(__aweme_id)
    BytedanceFuck(__aweme_id).start()

def fetch_proxies():
    response = requests.get(
        url="https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt"
    )

    if response.ok:
        os.unlink("proxies.txt")
        with open("proxies.txt", "w") as f:
            f.write(response.text)
            f.close()
            print("proxy list fetched :)")

    else:
        print("proxy list fetch error...")
        exit(1)


if __name__ == '__main__':
    os.system(f'cls' if os.name == 'nt' else 'clear')
    banner()
    link = input(
        Col.purple + "{" + Col.reset + "LQM" + Col.purple + "}" + Col.reset + " Nhập link video " + Col.purple + "[" + Col.reset + "Nhập xong bấm " + Col.blue + "Enter" + Col.reset + " để bắt đầu" + Col.purple + "]" + Col.reset + " -> ")
    __aweme_id = str(re.findall(r"(\d{18,19})", link)[0] if len(re.findall(r"(\d{18,19})", link)) == 1 else
                     re.findall(r"(\d{18,19})", requests.head(link, allow_redirects=True, timeout=5).url)[0])
    print(" \033[1;93m~ \033[1;94m[\033[1;95mLQM\033[1;94m] \033[1;93m=> \033[1;97mLoading..!                         ",end="\r")
    BytedanceFuck(__aweme_id).start()
