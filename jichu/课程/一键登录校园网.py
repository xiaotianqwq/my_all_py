# -*- conding = utf-8 -*-
# @Time:2021/10/3 21:30
# @Author:宇
# @Flie:一键登录校园网.py
# @Software:PyCharm

import requests
#验证码
check_url_requests = 'http://111.32.9.98:8090/generateVerifyCode.wlan'
check_res = requests.get(url=check_url_requests).json()
check_url = 'http://111.32.9.98:8090/' + check_res["url"]
check_jpg = requests.get(url=check_url).content
with open('./check.jpg','wb') as f:
    f.write(check_jpg)

check = input('验证码:')
url = 'http://111.32.9.98:8090/portalLogin.wlan?1633510308799'
data = {
    'lanAcName': '2111.3716.1179',
    'wlanAcIp': '',
    'wlanUserIp': '10.240.124.40',
    'ssid': 'CMCC-EDU',
    'portalLogin': '5535a402d9ce47cea480115026470b98',
    'passType': '1',
    'userName': '18812707266',
    'userPwd': '147258',
    'verifyCode': check,
    'verifyHidden': '8DCBC512EFDA3EE56E3518BCB4112A94962EE72873AACEAA'
}
requests.post(url=url,data=data)
