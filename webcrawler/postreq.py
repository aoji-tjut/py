#! /usr/bin/env python
# -*- coding: utf-8 -*-

#chrome->开发者工具->network->输入https://passport.lagou.com/login/login.html->开始录制->随便写用户名aaa@111.com密码aaa111提交
#network中显示login.json,然后查看请求报文头：
#isValidate:true
# username:aaa@111.com
# password:5b8df1d857cc0904cd9299fa86cb7ab8
# request_form_verifyCode:
# submit:

# 获取到了提交内容：然后代码构建模拟提交,大致流程是这样，但是最好的方式还是cookie的get请求

import requests

params={
    'isValidate':'true',
    'username':'17695586816',
    'password':'7a62bafee1bbafee04d5030be48ccbcf'
}

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

html=requests.post("http://www.china-pub.com/edition06/dl.asp",params,headers=headers)
print(html.text)