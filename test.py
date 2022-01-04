import os
import sys
import time
import shutil
import zipfile
import logging
import traceback
import urllib.request
# from urllib import request
from configparser import ConfigParser

if os.path.exists('debug.log'):
    os.remove('debug.log') # del old log file

logging.basicConfig(filename='debug.log',level=logging.DEBUG,format="%(asctime)s - %(pathname)s - %(message)s",datefmt=\
    "%Y/%m/%d %H:%M:%S")

os.system("") # fixd print's color bug in Win10

con = ConfigParser()
con_path = os.path.join(os.path.abspath('.'),'config.ini') # config.ini--local config file name
con.read(con_path)

Java_Path = 'Java\\' + con.get('setting','java_file')

Backup_Path = os.getcwd() + "/.minecraft/con_backup/inventoryprofilesnext"
Backup_File1 = ".minecraft\\config\\inventoryprofilesnext"
Con_Backup =".\\.minecraft\\con_backup\\inventoryprofilesnext"
Con_Back_Path = ".\\.minecraft\\con_backup\\"
Del_file = ".minecraft\\config"

# Java_Path = "Java\\jdk-17.0.1_windows-x64_bin.exe"

# try:
#     os.system(Java_Path)
#     sys.exit('install java')
# except:
#     logging.debug(traceback.format_exc())

try:
    if not os.path.exists(Backup_Path):
        os.makedirs(Backup_Path)
        os.system('copy %s %s' % (Backup_File1,Con_Backup))
        shutil.rmtree(Del_file)
        os.makedirs(Del_file)
        os.system('Xcopy %s %s /E/H/C' % (Con_Back_Path,Del_file))
        echo = 'Fix is complete, please run hmcl to start the game.'
        print(echo)
        time.sleep(5)
        sys.exit(echo)
    else:
        os.system('copy %s %s' % (Backup_File1,Con_Backup))
        shutil.rmtree(Del_file)
        os.makedirs(Del_file)
        os.system('Xcopy %s %s /E/H/C' % (Con_Back_Path,Del_file))
        echo = 'Fix is complete, please run hmcl to start the game.'
        print(echo)
        time.sleep(5)
        sys.exit(echo)
except:
    logging.debug(traceback.format_exc())