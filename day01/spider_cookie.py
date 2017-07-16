# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: spider_cookie.py
@time: 2017/7/16 12:09
"""
import urllib
import urllib2
import ssl

context = ssl._create_unverified_context()

url = "https://www.zhihu.com/"

header = {
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "authorization":"Bearer Mi4wQUFCQXpkOF9BQUFBWU1MZ0pXYnVDeGNBQUFCaEFsVk5Sb050V1FESDlpNkU5UVVrMzRBbUZ0NzZTemhOb2RCQ0Rn|1497757254|9b31a81c9b3e50e3504ff4ad6466671a2e941b77",
    "Cookie":'r_cap_id="Yzg0ZWQwNzczMjNjNDRlNzkxMmU2YzE0MDk2ZjM1MGQ=|1497757246|51e5c940560a2ce7de94f315ff50bfc8aad69441"; cap_id="YjM0NThkYzBiMmI4NDk1MGJkNGVkM2RjN2U5MTNhMWM=|1497757246|3f3416854f1567207452215ef7396118e16d5ca2"; d_c0="AGDC4CVm7guPThBvXsGrkY8g4NJJ20CgE4s=|1497757248"; _zap=75fdae6c-8525-47ef-bc14-6b4e8c9bc823; z_c0=Mi4wQUFCQXpkOF9BQUFBWU1MZ0pXYnVDeGNBQUFCaEFsVk5Sb050V1FESDlpNkU5UVVrMzRBbUZ0NzZTemhOb2RCQ0Rn|1497757254|9b31a81c9b3e50e3504ff4ad6466671a2e941b77; q_c1=16cf325c8e634293b1cbdc573b3bce65|1498656462000|1491053507000; q_c1=16cf325c8e634293b1cbdc573b3bce65|1498656462000|1491053507000; __utma=51854390.1521929809.1497757246.1497757246.1498657617.2; __utmz=51854390.1498657617.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/51446969/answer/125880656; __utmv=51854390.100-1|2=registration_date=20141109=1^3=entry_date=20141109=1; aliyungf_tc=AQAAAACuaxERhwQA6p50cbTIm/3YV1yI; _xsrf=b7e5b649-9c02-4e84-b4b3-7af778a64074',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}

request = urllib2.Request(url, headers=header)

response = urllib2.urlopen(request, context=context)

print response.read()