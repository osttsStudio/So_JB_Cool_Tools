import logging
import os
import shutil
import sys
import time
import traceback
import urllib.request
import zipfile
from configparser import ConfigParser
from urllib import request

if os.path.exists('debug.log'):
    os.remove('debug.log') # del old log file
if os.path.exists('config.ini'):
    os.remove('config.ini') # del old config file

logging.basicConfig(filename='debug.log',level=logging.DEBUG,format="%(asctime)s - %(pathname)s - %(message)s",datefmt=\
"%Y/%m/%d %H:%M:%S")

os.system("") # fixd print's color bug in Win10

# load local config

ConServer = ConfigParser()
#ConServerPath = os.path.join(os.path.abspath('.'),'mc_tools.ini') # config.ini--local config file name
ConServer.read('mc_tools.ini')

ConServerUrl = ConServer.get('setting','Server')
ConServerRes = os.getcwd() + "./config.ini"

try:
    request.urlretrieve(ConServerUrl,ConServerRes)
except:
    logging.debug(traceback.format_exc())

con = ConfigParser()
#Con_Path = os.path.join(os.path.abspath('.'),'config.ini') # config.ini--local config file name
con.read('config.ini')

backupPath = con.get('variable','Backup_Path')
backupFile = con.get('variable','Backup_File')
conBackup = con.get('variable','Con_Backup')
conBackPath = con.get('variable','Con_Back_Path')
delFile = con.get('variable','Del_file')

Backup_Path = os.getcwd() + backupPath
Backup_File = os.getcwd() + backupFile
Con_Backup = os.getcwd() + conBackup
Con_Back_Path = os.getcwd() + conBackPath
Del_File = os.getcwd() + delFile

Java_Path = 'Java\\' + con.get('setting','java_file')
batRes = con.get('variable','Bat_Res')
Bat_Res = os.getcwd() + batRes

LocalVersion = ConServer.get('setting','Version')
ServerVerion = con.get('setting','Version')
# a bat file for updating itself and config, and supports deleting unnecessary files

# Con_res = os.getcwd() + "./config.ini" # config_new.ini--server config file name
# Url_server = con.get('url','server')
# Con_url = Url_server + "/config.ini" # config file url

try:
    if not os.path.exists('config.ini'):
        print("""\033[1;31;40m配置文件config.ini不存在，请联系管理员。
The config.ini does not exist, please contact the administrator.\033[0m""")
        input("Press Enter to exit.")
        os.remove('config.ini')
        sys.exit('config file not found')

    if not os.path.exists('mc_tools.ini'):
        print("""\033[1;31;40m配置文件mc_tools.ini不存在，请联系管理员。
The config.ini does not exist, please contact the administrator.\033[0m""")
        input("Press Enter to exit.")
        os.remove('config.ini')
        sys.exit('config file not found')

    Choose = int(input('''
┌─────────────────────────────────────────────┐
│              So ** Cool Tools        v0.0.5 │ 
├─────────────────────────────────────────────┤
│Please choose function.                      │
│1.更新客户端 | Update client                  │
│2.安装JAVA | Install Java                     │
│3.修复崩溃bug | Fix crash bug                 │
├─────────────────────────────────────────────┤
│   Takahashiharuki SHDocter       2022/02/23 │
├─────────────────────────────────────────────┤
│                 新年快乐~~~                 │
│              Happy new year~~~              │
└─────────────────────────────────────────────┘
请输入数字并按回车确认:
Please enter a number and press enter to confirm:
'''))

# con_server = ConfigParser()
# con_server_path = os.path.join(os.path.abspath('.'),'config_new.ini') # config_new.ini--server config file name
# con_server.read(con_server_path)
# Ver_local = con.get('ver','version')
# Ver_server = con_server.get('ver','version')


# Download update file
    if Choose == 1:
        if LocalVersion == ServerVerion:
            print("""\n\033[5;36;40m目前已经是最新版本。
It's the latest version.\033[0m\n""")
        if LocalVersion != ServerVerion:
            print("""\n\033[5;36;40m下载中，请等待。
Downloading, please wait.\033[0m\n""")

            def report(blocknum, blocksize, totalsize):
                readsofar = blocknum * blocksize
                if totalsize > 0:
                    percent = readsofar * 1e2 / totalsize
                    s = "\r%5.1f%% %*d / %d" % (percent, len(str(totalsize)), readsofar, totalsize)
                    sys.stderr.write(s)
                    if readsofar >= totalsize:
                        sys.stderr.write("\n")
                else: # total size is unknown
                    sys.stderr.write("read %d\n" % (readsofar,))

            Zip_url = con.get('url', 'server') + "/files/chii_update_1181.zip"
            urllib.request.urlretrieve(Zip_url,"./chii_update_1181.zip",report)

            Unzip = zipfile.ZipFile("./chii_update_1181.zip", mode='r')
            for names in Unzip.namelist():
                Unzip.extract(names, './.minecraft')  # unzip to .minecraft
            Unzip.close()

            time.sleep(2)
            os.remove('chii_update_1181.zip')
            print("""\n\033[5;36;40m更新中，如有疑问请联系管理员，请等待。
Updating, please contact the administrator if you have any questions, please wait.\033[0m\n""")
            time.sleep(2)
            os.remove('config.ini')
            os.system(Bat_Res)
            sys.exit('update is successful')

# Start java installer
    if Choose == 2:
        os.system(Java_Path)
        os.remove('config.ini')
        sys.exit('start java installer successful')

# Try to fix the bug that hmcl crashes when starting the game at sometimes(1.18.x only)
    if Choose == 3:
        if not os.path.exists(Backup_Path):
            os.makedirs(Backup_Path)

        os.system('copy %s %s' % (Backup_File,Con_Backup))
        shutil.rmtree(Del_File)
        os.makedirs(Del_File)
        os.system('Xcopy %s %s /E/H/C' % (Con_Back_Path,Del_File))
        echo = 'Fix is complete, please run hmcl to start the game.'
        print(echo)
        os.remove('config.ini')
        time.sleep(5)
        sys.exit(echo)

    elif Choose != 1 and 2 and 3:
        echo1 = 'Number is error，please restart the software and select again'
        print(echo1)
        os.remove('config.ini')
        input('Press Enter to quit.')
        sys.exit(echo1)

except:
    logging.debug(traceback.format_exc())