#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isdir, join

def start_vm():
    mypath = os.environ.get('HOME')+"/Parallels"
    files = listdir(mypath)
    vm = [0]
    c = 0
    print("==================================")
    print("Parallels Desktop 繞過神器")
    print("==================================")
    for fs in files:
        # 產生檔案的絕對路徑
        fullpath = join(mypath, fs)
        if isdir(fullpath):
            vm.append(fs[0:-4])
            c+=1
            print("虛擬機[%d]: %s"%(c,vm[c]))
    print("==================================")
    
    ch = int(input("請選擇要開啟的虛擬機編號： "))

    f = open("password.txt",'r')
    passwd = f.read()
    exploit = "echo %s | sudo -S date 010100002018 && /usr/local/bin/prlctl start '%s'" % (passwd,vm[ch])  
    os.system(exploit)
    time_up = "echo %s | sudo -S systemsetup -setnetworktimeserver time.apple.com" % (passwd)
    os.system(time_up)


if os.path.isfile("password.txt"):
    start_vm()
else:
    passwd = str(input("請輸入密碼:"))
    f = open('password.txt', 'w')
    f.write(passwd)
    f.close()
    start_vm()