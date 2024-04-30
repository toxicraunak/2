import requests
import os
from os import system, name
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except:
    system('pip install websocket-client')
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []

print()
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print()
token = "6737562665:AAH1NBn84h2s64LFucbMWKq7oRMzq4MHybI"
telegram_chat_id = "-1002038908424"
print(f'  {{•}}  TOKEN   ๛   {token}')
print()
ID = telegram_chat_id
print(f'  {{•}}  ID  ๛  {ID}')
print()
print(' ✖✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖ ✘✖  ')
print()

os.system('clear')

def work():
    global failed, success, retry
    username = choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(choices(list('qwertyuioplkjhgfdsazxcvbnm1234567890'), k=12))
    try:
        con = create_connection("wss://193.200.173.45/Auth", header={"app": "com.safeum.android","host": None,"remoteIp": "193.200.173.45","remotePort": str(8080),"sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195","time": "2023-04-30 12:13:32","url": "wss://51.79.208.190/Auth"},sslopt={"cert_reqs": CERT_NONE})
        con.send(dumps({"action":"Register","subaction":"Desktop","locale":"en_IN","gmt":"+05","password":{"m1x":"db64e904558056bd9cb678e293208c0e405ac7a5176e749c13394c26cc45811c","m1y":"cad211c0407c46123a9e6a1b12c1e3dcd833ab25d4035c86f8dc60db6998aec0","m2":"5be138004398f943009ac3ee83a998787ec65d223f785f151a1d96ee6565d9ba","iv":"c65e5eeb9e35b59b735122f294b91174","message":"755d3d407548424954ae8028f94fe47ee945769b3594ac2c35e7915930fe31153bcf348886852aeb0607bf22e6d4faa9e9c0d67fcc790494cc82fe0321e7b1a10c3eaf71dedbd099c6129688241131dc"},"magicword":{"m1x":"380bad74db434a1e9cdee300acd17a95dce15f1350104e41828d076659418e41","m1y":"119f91e7d61f7cc7c232b9f9208dd9ac6d1feb90092d526ec6d52a2267afbf92","m2":"9b08db28a9c8fac929d2eee507cc76430ee972bddc651d0e8e3cd066cc3fd05c","iv":"09634bfa435bdfd3f6d651ca8fa46480","message":"ebeb8efca60c56f6d781b6d6c6e0a4d5"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi 220733SPH","softwareversion":"1.1.0.1457","nickname":"sibshocs6227hsys","os":"AND","deviceuid":"b0c55c7c17fddd4b","devicepushuid":"*cYwQmtN0GC4:APA91bGdy73ku9qhNJi8Inhe01e2pXa_dp-CiVULHhPMkcqgi4JFOTCMS-jHhJzxhoO5ZdmGhjFgy-qxGQFSB86l0A1iQGM9RSl3c6X33zPAqxkRQ6C1qm2Gfx94e72joG2twLFbh61E","osversion":"and_12.0.0","id":"1392209033"}))
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success+= 1
            accounts.append(username+':@Haxkx')
            with open('SafeUM-Haxkx.txt', 'a') as f:
                f.write(username + ":@Haxkx\n")
            # send account to Telegram bot
            tlg = f'\n🥹🌹 New Account Found By @Haxkx \nUsername {username} /nAccount password @Haxkx /nFollow @Haxkx For More ❤️'
            requests.post(f"https://api.telegram.org/bot{token}/sendmessage?chat_id={telegram_chat_id}&text="+str(tlg))
        else:
            failed+=1
    except:
        retry+=1
    print(f'\rSuccess: {success}, Failed: {failed}, Retry: {retry}', end='', flush=True)

start = ThreadPoolExecutor(max_workers=3000)
while True:
    start.submit(work)
