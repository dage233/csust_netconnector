#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project : PC
@author  : 王智峰
@file   : main.py
@ide    : PyCharm
@time   : 2019-06-13 18:23:23
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import random
import threading
import time
import requests
import wx
import wx.adv

stop = False  # 结束


class AutoLogin:
	def __init__(self):
		self.user_agent = [
			'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '
			'Safari/534.50',
			'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
			'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
			'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; '
			'.NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
			'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
			'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
			'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
			'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
			'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
			'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 '
			'Safari/535.11',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR '
			'2.0.50727; SE 2.X MetaSr 1.0)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
			'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
			'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) '
			'Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
			'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) '
			'Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
			'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 '
			'Mobile/8J2 Safari/6533.18.5',
			'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) '
			'Version/4.0 Mobile Safari/533.1',
			'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 ('
			'KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
			'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
			'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 '
			'Safari/534.13',
			'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile '
			'Safari/534.1+',
			'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 '
			'Safari/534.6 TouchPad/1.0',
			'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) '
			'AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
			'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
			'UCWEB7.0.2.37/28/999',
			'NOKIA5700/ UCWEB7.0.2.37/28/999',
			'Openwave/ UCWEB7.0.2.37/28/999',
			'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999', ]
		self.url_login = "http://192.168.7.221:801/eportal/?" \
		                 "c=ACSetting&" \
		                 "a=Login&" \
		                 "protocol=http:&" \
		                 "iTermType=1&" \
		                 "enAdvert=0&" \
		                 "queryACIP=0&" \
		                 "loginMethod=1 "
		self.user_passwd_dict = [] # 账号不会给你的...
		self.main()
	
	def check(self):
		try:
			requests.get('https://www.baidu.com/', timeout=1)
			return False
		except:
			return True
	
	def login(self, user, passwd, oneuseragent):
		data = {
			"DDDDD": ',0,' + user,
			"upass": passwd,
		}
		header = {
			'User-Agent': oneuseragent
		}
		res = requests.post(self.url_login, data=data, headers=header)
		return res.text.find('认证成功页') != -1 or res.text.find('login again') != -1
	
	def main(self):
		while True:
			while True:
				if stop or self.check():
					break
				time.sleep(3)
			while True:
				user_and_passwd = random.choice(self.user_passwd_dict)
				if stop or self.login(user_and_passwd[0], user_and_passwd[1], random.choice(self.user_agent)):
					break
			if stop:
				break


class MyTaskBarIcon(wx.adv.TaskBarIcon):
	ICON = "logo.ico"  # 图标地址
	ID_ABOUT = wx.NewId()  # 菜单选项“关于”的ID
	ID_EXIT = wx.NewId()  # 菜单选项“退出”的ID
	TITLE = "校园网登录(简化版)"  # 鼠标移动到图标上显示的文字
	
	def __init__(self):
		threading.Thread.__init__(self)
		wx.adv.TaskBarIcon.__init__(self)
		self.SetIcon(wx.Icon(self.ICON), self.TITLE)  # 设置图标和标题
		self.Bind(wx.EVT_MENU, self.on_about, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
		self.Bind(wx.EVT_MENU, self.on_exit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
	
	# “关于”选项的事件处理器
	def on_about(self, event):
		wx.MessageBox(
			'                   使用说明\n'
			'连接bg/有线网 然后点击运行即可\n'
			'可选择开机自启\n\n '
			'嘿兄弟 你看起来很不好，你最好在天黑前找点吃的\n\n'
			'版本: 2.2\n最后更新日期：2019-6-14\n'
			'本软件仅用于学习,研究.绝不会用于商业用途',
			"关于")
	
	# “退出”选项的事件处理器
	def on_exit(self, event):
		global stop
		stop = True
		wx.Exit()
		exit(0)
	
	# 创建菜单选项
	def CreatePopupMenu(self):
		menu = wx.Menu()
		for mentAttr in self.getMenuAttrs():
			menu.Append(mentAttr[1], mentAttr[0])
		return menu
	
	# 获取菜单的属性元组
	def getMenuAttrs(self):
		return [
			('关于', self.ID_ABOUT),
			('退出', self.ID_EXIT)
		]


class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self)
		MyTaskBarIcon()  # 显示系统托盘图标


class MyApp(wx.App):
	def OnInit(self):
		MyFrame()
		return True


if __name__ == "__main__":
	threading.Thread(target=AutoLogin).start()
	app = MyApp()
	app.MainLoop()
