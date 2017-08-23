#coding:utf-8 -*-
import os
import json
import urllib2
def getip():
	res=urllib2.urlopen('http://members.3322.org/dyndns/getip').read()
	return str(res)
def liuliang(x):
	return x*1024**3
def QueryUserExist(x,a):
	for m in a:
		if x==m[u'user']:
			return True
	return False
def QueryUserPlace(x,a):
	i=0
	for m in a:
		if x==m[u'user']:
			return i
		else:
			i+=1
	return False
def queryport(x,a):
	for m in a:
		if x==m[u'port']:
			return True
	return False
def fun(val):
        ret=""
        if val / 1024 < 4:
                ret += "%s" % val
        elif val / 1024 ** 2 < 4:
                val /= float(1024)
                ret += "%s KB" % val
        elif val / 1024 ** 3 < 4:
                val /= float(1024 ** 2)
                ret += "%s MB" % val
        else:
                val /= float(1024 ** 3)
                ret += "%s GB" % val
        return ret
def QueryAllUser():
        f = file("/root/shadowsocksr/mudb.json")
        a= json.load(f);##server,user,port,passwd,used,enable,protoco,canshu,method,obfs,type
        server=getip()
        for x in a:
                user= x[u'user']
                passwd= x[u'passwd']
                port= x[u'port']
                obfs= x[u'obfs']
                used=x[u'd']
                enable=x[u'transfer_enable']
                u=enable-used
                protocol=x[u'protocol']
                canshu='%d:%s'%(port,passwd)
                method=x[u'method']
                print u"服务器：%s\n用户名：%s\n密码：%s\n端口：%d\n已用流量：%s\n剩余流量：%s\n总流量：%s\n加密方法：%s\n混淆方式：%s\n协议：%s\n单端口多用户协议参数：%s\n"%(server,user,passwd,port,fun(used),fun(u),fun(enable),method,obfs,protocol,canshu)
        f.close()
def QueryUser():
	f = file("/root/shadowsocksr/mudb.json");
	a= json.load(f);##server,user,port,passwd,used,enable,protoco,canshu,method,obfs,type
	server=getip()
	b=raw_input('输入用户名：')
	for x in a:
		if x[u'user']==b:
			user= x[u'user']
			passwd= x[u'passwd']
			port= x[u'port']
			obfs= x[u'obfs']
			used=x[u'd']
			enable=x[u'transfer_enable']
			u=enable-used
			protocol=x[u'protocol']
			canshu='%d:%s'%(port,passwd)
			method=x[u'method']
			print u"服务器：%s\n用户名：%s\n密码：%s\n端口：%d\n已用流量：%s\n剩余流量：%s\n总流量：%s\n加密方法：%s\n混淆方式：%s\n协议：%s\n单端口多用户协议参数：%s\n"%(server,user,passwd,port,fun(used),fun(u),fun(enable),method,obfs,protocol,canshu)
		else:
			pass
	f.close()
def DelectUser():
	f = file("/root/shadowsocksr/mudb.json");
	a= json.load(f);
	print '输入要删除的用户：'
	user= raw_input()
	x=QueryUserExist(user,a)
	if x:
		del(a[x])
		print '成功删除用户%s'%user
		json.dump(a, open('/root/shadowsocksr/mudb.json', 'w'))
	else :
		print '用户名不存在，请重新输入'
	f.close();
def AddUser():
	f = file("/root/shadowsocksr/mudb.json");
	a= json.load(f);##server,user,port,passwd,used,enable,protoco,canshu,method,obfs,type
	server=getip()
	print '输入选项：\n1，增加单端口多用户端口\n2，添加普通用户'
	b=input()
	if b==1:
		user= raw_input('输入用户：')
		if QueryUserExist(user,a):
			print '用户名已存在，请重新输入'
		else:
			port= input('输入端口(0-65535)：')
			if queryport(port,a):
				print '端口已被占用，请重新输入'
			else:
				passwd= raw_input('输入密码：')
				obfs='http_simple_compatible'
				used=0
				u=0
				enable=input('输入可用流量(GB)：')
				protocol='auth_aes128_sha1'
				method='aes-128-cfb'
				m={'enable':1,'user':user,'passwd':passwd,'port':port,'obfs':obfs,'d':used,'transfer_enable':liuliang(enable),'u':0,'protocol':protocol,'protocol_param':'#','method':method}
				a.append(m)
				json.dump(a, open('/root/shadowsocksr/mudb.json', 'w'))
				print '成功添加多用户端口:%d'%port
				print '连接信息为：\n服务器：%s\n端口：%d\n密码：%s\n加密方法：%s\n协议：%s\n混淆方式：%s\n'%(server,port,passwd,method,protocol,obfs)
	elif b==2:
		user= raw_input('输入用户：')
		if QueryUserExist(user,a):
			print '用户名已存在，请重新输入'
		else:
			port= input('输入端口(0-65535,大于65535仅可使用单端口多用户端口)：')
			if queryport(port,a):
				print '端口已被占用，请重新输入'
			else:
				passwd= raw_input('输入密码：')
				obfs='http_simple_compatible'
				used=0
				u=0
				enable=input('输入可用流量(GB)：')
				protocol='auth_aes128_sha1'
				canshu='%d:%s'%(port,passwd)
				method='aes-128-cfb'
				m={'enable':1,'user':user,'passwd':passwd,'port':port,'obfs':obfs,'d':used,'transfer_enable':liuliang(enable),'u':0,'protocol':protocol,'protocol_param':'','method':method}
				a.append(m)
				json.dump(a, open('/root/shadowsocksr/mudb.json', 'w'))
				print '成功添加用户:%s'%user
				print '连接信息为：\n服务器：%s\n端口：%d\n密码：%s\n加密方法：%s\n协议：%s\n混淆方式：%s\n'%(server,port,passwd,method,protocol,obfs)
				print '单端口多用户协议参数为：%s'%canshu
	f.close();
print '输入选项：\n1，开启服务\n2,关闭服务\n3,添加用户\n4,删除用户\n5,查询所有用户信息\n6,查询单个用户信息\n'
a=input()
if a==1:
	os.system('bash /root/shadowsocksr/run.sh')
	print 'shadowsocksr服务已启动'
elif a==2:
	os.system('bash /root/shadowsocksr/stop.sh')
	print 'shadowsocksr服务已关闭'
elif a==3:
	AddUser()
	os.system('bash /root/shadowsocksr/run.sh')
elif a==4:
	DelectUser()
	os.system('bash /root/shadowsocksr/run.sh')
elif a==5:
	QueryAllUser()
elif a==6:
	QueryUser()
