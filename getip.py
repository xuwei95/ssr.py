#coding:utf-8 -*-
import requests,urllib2
def getip():
	res=requests.get('http://members.3322.org/dyndns/getip')
	res.encoding = 'utf8'
	return str(res.text.replace("\n", ""))
def get():
	ip=urllib2.urlopen('http://members.3322.org/dyndns/getip').read()
	return ip
print get()
