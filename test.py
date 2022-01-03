import os
import sys
import time
import zipfile
import logging
import traceback
import urllib.request
# from urllib import request
from configparser import ConfigParser

if os.path.exists('debug.log'):
    os.remove('debug.log') # del old log file

logging.basicConfig(filename='debug.log',level=logging.DEBUG,format="%(asctime)s - %(pathname)s - %(message)s",datefmt="%Y/%m/%d %H:%M:%S")

os.system("") # fixd print's color bug in Win10

con = ConfigParser()
con_path = os.path.join(os.path.abspath('.'),'config.ini') # config.ini--local config file name
con.read(con_path)

Java_Path = 'Java\\' + con.get('setting','java')

Backup_Path = os.getcwd() + "/.minecraft/con_backup/inventoryprofilesnext"
Backup_File1 = ".minecraft\\config\\inventoryprofilesnext\\inventoryprofiles.json"
Backup_File2 = ".minecraft\\config\\inventoryprofilesnext\\ModIntegrationHints.json"
Con_Backup =".\\.minecraft\\con_backup\\inventoryprofilesnext"

# Java_Path = "Java\\jdk-17.0.1_windows-x64_bin.exe"

try:
    os.system(Java_Path)
    sys.exit('install java')
except:
    logging.debug(traceback.format_exc())

# try:
#     if not os.path.exists(Backup_Path):
#         os.makedirs(Backup_Path)
#         os.system('copy %s %s' % (Backup_File1,Con_Backup))
#         os.system('copy %s %s' % (Backup_File2,Con_Backup))
#     else:
#         os.system('copy %s %s' % (Backup_File1,Con_Backup))
#         os.system('copy %s %s' % (Backup_File2,Con_Backup))
# except:
#     logging.debug(traceback.format_exc())