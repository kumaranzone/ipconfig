#!/usr/bin/python - env
'''
MODULE NAME: ipconfig
PURPOSE: To print the network values and ip address based on type of OS
author: muthu kumaran
email: kumaran.developer@outlook.com
'''
import sys,os,time
def ipconfig():
    print "Your OS is ", sys.platform
    if sys.platform == 'win32':        
        print os.system("ipconfig")
    elif sys.platform == 'linux2':
        print os.system("ifconfig")
    time.sleep(5)
if __name__ == '__main__':
    ipconfig()
