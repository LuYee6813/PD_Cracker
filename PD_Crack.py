#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isdir, join

mypath = os.environ.get('HOME')+"/Parallels"
files = listdir(mypath)
vm=[0]

c=0
print("==================================")
print("Parallels Desktop 繞過神器")
print("==================================")
os.system("open /Applications/Parallels\ Desktop.app")
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)
  if isdir(fullpath):
    # 添加虛擬機到陣列和變數
    vm.append(f[0:-4])
    os.environ['vm'+str(c)] = str(f[0:-4])
    print("虛擬機#"+str(c)+"：", vm[c])
  c=c+1
print("==================================")

# 儲存編號變數
ch = int(input("請選擇要開啟的虛擬機編號#:"))
# 儲存密碼變數
passwd = str(input("請輸入密碼："))  
os.environ['passwd']=str(passwd)


# 漏洞利用
exploit = "echo $passwd | sudo -S date 010100002018 && /usr/local/bin/prlctl start $vm" + str(ch)
os.system(exploit)
os.system("echo $passwd | sudo -S systemsetup -setnetworktimeserver time.apple.com")

