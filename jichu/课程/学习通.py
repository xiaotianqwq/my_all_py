# -*- conding = utf-8 -*-
# @Time:2021/11/9 22:10
# @Author:宇
# @Flie:学习通.py
# @Software:PyCharm

from selenium import webdriver
from time import sleep
import requests
'''
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'k8s=79cb61921b8937341a5e06c7c69864b15c8ba6c3; jrose=93BFF6AE4CACD1F008FEDC831E33BF7B.mooc2-2248767101-j7phv; route=1808ff30540c76e74a8f7fef65cb795c; source=""; lv=1; fid=1697; _uid=203739928; uf=b2d2c93beefa90dc558e1be56ddb6ced66ef86f93a435cc9c807cdb4c1a1e7dfcba3c0868c3c246e6f7dd18c135e2b0f913b662843f1f4ad6d92e371d7fdf644e578c2b9d380a8e6fd68be96b6183b1a15ba01ec738f02a60c4035cab69dda3a6072c284b6aee818; _d=1636466457439; UID=203739928; vc=4B9F361537107C545D942003E3850FFC; vc2=66062239F6B23AD66B0E9FADB5D72444; vc3=GOzmQml5AwxdBt2djm6zsOvyBMzkJKwlh6XvFN2YkMxQ1xU1iqPaPyvyYSNKGnsrknRYeMQFWkx3ISjR6YJmuGJTP%2Fl3GYoQ49oQ7uFcm2Mhfl%2BpA61UqVv5bL2%2Br1OHUtan3hJt0xCpjEuYDji%2Fb9aW1B6juIOLd3fpRrlYOeE%3De306b905de49c0b5e43261cf2302cad7; xxtenc=afe1c26f40669f7466f7d19d632b8f64; DSSTASH_LOG=C_38-UN_308-US_203739928-T_1636466457440; spaceFid=1697; spaceRoleId=""; thirdRegist=0',
    'Host': 'mooc2-ans.chaoxing.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
'''


#账号密码
#namename = input('账号:')
#namepass = input('密码：')
#x = int(input('第几单元：'))

browser = webdriver.Edge(executable_path ="./msedgedriver.exe")
browser.get("https://mooc2-ans.chaoxing.com/mycourse/stu?courseid=218785022&clazzid=46004325&cpi=212596368&enc=51b149520ca541e36ee9175c254b9c09&t=1636466540589&pageHeader=1")