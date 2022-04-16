#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from os import listdir
from os.path import isdir, join

# get current user directory
mypath = os.environ.get('HOME')+"/Parallels"

# get all data on mypath
files = listdir(mypath)

# virtual machine list
vm=[0]

c=0
print("==================================")
print("Parallels Desktop 繞過神器")
print("==================================")
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)

  if isdir(fullpath):
    vm.append(f[0:-4])
    print("虛擬機#"+str(c)+"：", vm[c])
  c=c+1

print("==================================")

ch = int(input("請選擇要開啟的虛擬機編號#:"))
os.environ["vmname"]="'"+vm[ch]+"'"



passwd = str(input("請輸入密碼："))  
os.environ['passwd']=str(passwd)



os.system("bash -c 'echo 正在開啟 $vmname'")

if ch == 1:
  os.system("echo $passwd | sudo -S date 010100002018 && /usr/local/bin/prlctl start 'Ubuntu＿20.04.2＿ARM64'")
elif ch == 2:
  os.system("echo $passwd | sudo -S date 010100002018 && /usr/local/bin/prlctl start 'Kali＿Linux'")
elif ch == 3:
  os.system("echo $passwd | sudo -S date 010100002018 && /usr/local/bin/prlctl start 'Windows＿11'")

os.system("echo $passwd | sudo -S systemsetup -setnetworktimeserver time.apple.com")

os.system("exit")