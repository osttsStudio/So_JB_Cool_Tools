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

Bat_res = os.getcwd() + "/.minecraft/update.bat"
# a bat file for updating itself and config, and supports deleting unnecessary files

# load local config
con = ConfigParser()
con_path = os.path.join(os.path.abspath('.'),'config.ini') # config.ini--local config file name
con.read(con_path)

Backup_Path = os.getcwd() + "/.minecraft/con_backup/inventoryprofilesnext"
Backup_File = ".minecraft\\config\\inventoryprofilesnext"
Con_Backup =".\\.minecraft\\con_backup\\inventoryprofilesnext"
Con_Back_Path = ".\\.minecraft\\con_backup\\"
Del_file = ".minecraft\\config"

Java_Path = 'Java\\' + con.get('setting','java_file')
Position = input('''
Are you in Chinese mainland? Yse=1 No=2
Press number:
''')

# Con_res = os.getcwd() + "./config_new.ini" # config_new.ini--server config file name
# Url_server = con.get('url','server')
# Con_url = Url_server + "/config.ini" # config file url

# try:
#     request.urlretrieve(Con_url,Con_res)

# except:
#     logging.debug(traceback.format_exc())

try:
    Choose = int(input('''
┌─────────────────────────────────────────────┐
│              So ** Cool Tools        v0.0.2 │ 
├─────────────────────────────────────────────┤
│Please choose function.                      │
│1.更新客户端 Update client                   │
│2.安装JAVA Install Java                      │
│3.修复崩溃bug Fix crash bug                  │
│4.下载mc库文件 Download mc lib file          │
├─────────────────────────────────────────────┤
│   Takahashiharuki SHDocter       2022/01/08 │
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

        if Position == 1:
            Update_Url = "http://" + con.get('url', 'server_cn')
        elif Position != 1:
            Update_Url = "http://" + con.get('url', 'server_os')
            Zip_url = Update_Url + "/files/chii_update_1181.zip"
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
        os.system(Bat_res)
        sys.exit('update is successful')

# Start java installer
    if Choose == 2:
        if not os.path.exists(con_path):
            print("""\033[1;31;40m配置文件config.ini不存在，请联系管理员。
    The config.ini does not exist, please contact the administrator.\033[0m""")
            input("Press Enter to exit.")
            sys.exit('config file not found')
        os.system(Java_Path)
        sys.exit('start java installer successful')

# Try to fix the bug that hmcl crashes when starting the game at sometimes(1.18.x only)
    if Choose == 3:
        if not os.path.exists(Backup_Path):
            os.makedirs(Backup_Path)

        os.system('copy %s %s' % (Backup_File,Con_Backup))
        shutil.rmtree(Del_file)
        os.makedirs(Del_file)
        os.system('Xcopy %s %s /E/H/C' % (Con_Back_Path,Del_file))
        echo = 'Fix is complete, please run hmcl to start the game.'
        print(echo)
        time.sleep(5)
        sys.exit(echo)

# Download and unzip the mc1.18.1 lib file
    if Choose == 4:
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
        if Position == 1:
            Update_Url = "http://" + con.get('url', 'server_cn')
        elif Position != 1:
            Update_Url = "http://" + con.get('url', 'server_os')
            Zip_url = Update_Url + "/files/mc_lib_1181.zip"
            urllib.request.urlretrieve(Zip_url,"./mc_lib_1181.zip",report)

            Unzip1 = zipfile.ZipFile("./mc_lib_1181.zip", mode='r')
            for names in Unzip1.namelist():
                Unzip1.extract(names, './.minecraft')  # unzip to .minecraft
            Unzip1.close()

        time.sleep(2)
        os.remove('mc_lib_1181.zip')
        print("""\n\033[5;36;40m更新中，如有疑问请联系管理员，请等待。
Updating, please contact the administrator if you have any questions, please wait.\033[0m\n""")
        time.sleep(2)
        sys.exit('Download lib file is successful')
except:
    logging.debug(traceback.format_exc())