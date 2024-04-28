import telebot
import requests
import os
import time
import sys
import webbrowser
import pyfiglet
import termcolor
from fake_useragent import UserAgent
import random
import string
import names

token = "7014906584:AAF3El3T7jJqnhc2ZpOKOmixJArzAi79x7Q"
bot = telebot.TeleBot(token)

proxies = None

def get_headers(Country, Language):
    while True:
        try:
            an_agent = f'Mozilla/5.0 (Linux; Android {random.randint(9,13)}; {"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111,999)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
            res = requests.get("https://www.facebook.com/", headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}, proxies=proxies, timeout=30)
            js_datr = res.text.split('["_js_datr","')[1].split('",')[0]
            r = requests.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers={
                'user-agent': an_agent
            }, proxies=proxies, timeout=30).cookies

            headers1 = {
                'authority': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': an_agent,
                'viewport-width': '980',
            }
            response1 = requests.get('https://www.instagram.com/', headers=headers1, proxies=proxies, timeout=30)
            appid = response1.text.split('APP_ID":"')[1].split('"')[0]
            rollout = response1.text.split('rollout_hash":"')[1].split('"')[0]
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/signup/email/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': an_agent,
                'viewport-width': '360',
                'x-asbd-id': '198387',
                'x-csrftoken': r["csrftoken"],
                'x-ig-app-id': str(appid),
                'x-ig-www-claim': '0',
                'x-instagram-ajax': str(rollout),
                'x-requested-with': 'XMLHttpRequest',
                'x-web-device-id': r["ig_did"],
            }
            return headers
        except Exception as E:
            print(E)

def Get_UserName(Headers, Name, Email):
    try:
        updict = {"referer": 'https://www.instagram.com/accounts/signup/birthday/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}
        while True:
            data = {
                'email': Email,
                'name': Name + str(random.randint(1, 99)),
            }
            response = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
                headers=Headers,
                data=data,
                proxies=proxies,
                timeout=30
            )
            if 'status":"fail' in response.text:
                print(response.text)
            elif 'status":"ok' in response.text:
                print(response.text)
                return random.choice(response.json()['suggestions'])
            else:
                print(response.text)
    except Exception as E:
        print(E)

def Send_SMS(Headers, Email):
    try:
        data = {
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
        }
        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/send_verify_email/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30
        )
        return response.text
    except Exception as E:
        print(E)

def Validate_Code(Headers, Email, Code):
    try:
        updict = {"referer": 'https://www.instagram.com/accounts/signup/emailConfirmation/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}
        data = {
            'code': Code,
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
        }
        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30
        )
        return response
    except Exception as E:
        print(E)

def Create_Acc(Headers, Email, SignUpCode, headers ,chat_id):
    try:
        firstname = names.get_first_name()
        UserName = Get_UserName(headers, firstname, Email)
        Password = firstname.strip() + '_.\_' + str(random.randint(111, 999))

        updict = {"referer": 'https://www.instagram.com/accounts/signup/username/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}

        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}',
            'email': Email,
            'username': UserName,
            'first_name': firstname,
            'month': random.randint(1, 12),
            'day': random.randint(1, 28),
            'year': random.randint(1990, 2001),
            'client_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': SignUpCode,
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30
        )

        if '"account_created":true' in response.text:
            X = f"""
●●━═━═━═━═━═━═━═━═━═━═━═━●
@Haxkx
INSTA ID CREATE DN
●━═━═━═━═━═━═━═━═━═━═━═━●
GMAIL: {Email}
Username: {UserName}
Password: {Password}
●━═━═━═━═━═━═━═━═━═━═━═━●
Sessionid: {response.cookies['sessionid']}
Csrftoken: {response.cookies['csrftoken']}
Ds_user_id: {response.cookies['ds_user_id']}
Ig_did: {response.cookies['ig_did']}
Rur: {response.cookies['rur']}
Mid: {Headers['cookie'].split('mid=')[1].split(';')[0]}
Datr: {Headers['cookie'].split('datr=')[1]}
●━═━═━═━═━═━═━═━═━═━═━═━●
"""

            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={X}')
        else:
            pass
    except Exception as E:
        print(E)

@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    os.system('clear')
    a = pyfiglet.figlet_format("CoViDx")
    termcolor.cprint(a, "cyan")
    print(47 * "-")
    termcolor.cprint('WELCOME TO THE CoViDx WORLD INSTAGRAM CREATE', "green")
    print(47 * "-")
    bot.reply_to(message, "Enter your email address:")
    bot.register_next_step_handler(message, get_email)

def get_email(message):
    email = message.text
    headers = get_headers(Country='US', Language='en')
    ss = Send_SMS(headers, email)
    print(ss)
    if 'email_sent":true' in ss:
        bot.reply_to(message, "Enter the verification code:")
        bot.register_next_step_handler(message, validate_code, headers, email)
    else:
        bot.reply_to(message, "Error sending verification code. Please try again.")

def validate_code(message, headers, email):
    code = message.text
    a = Validate_Code(headers, email, code)
    print(a.text)
    if 'status":"ok' in a.text:
        SignUpCode = a.json()['signup_code']
        Create_Acc(headers, email, SignUpCode, headers, message.chat.id)
        bot.reply_to(message, "Account created successfully!")
    else:
        bot.reply_to(message, "Invalid verification code. Please try again.")

bot.polling(True)
