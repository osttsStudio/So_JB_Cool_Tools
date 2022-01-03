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

Bat_res = os.getcwd() + "/.minecraft/update.bat" # a bat file for updating itself and config, and supports deleting unnecessary files

# load local config
con = ConfigParser()
con_path = os.path.join(os.path.abspath('.'),'config.ini') # config.ini--local config file name
con.read(con_path)

Java_Path = 'Java\\' + con.get('setting','java_file')
Update_Url = "http://" + con.get('url','server')

# Con_res = os.getcwd() + "./config_new.ini" # config_new.ini--server config file name
# Url_server = con.get('url','server')
# Con_url = Url_server + "/config.ini" # config file url

# try:
#     request.urlretrieve(Con_url,Con_res)

# except:
#     logging.debug(traceback.format_exc())

# try:
#     if not os.path.exists(con_path):
#         print("""\033[1;31;40m配置文件config.ini不存在，请联系管理员。
# The config.ini does not exist, please contact the administrator.\033[0m""")
#         input("Press Enter to exit.")
#         os.remove('config_new.ini')
#         sys.exit('config file not found')

# except:
#     logging.debug(traceback.format_exc())

# con_server = ConfigParser()
# con_server_path = os.path.join(os.path.abspath('.'),'config_new.ini') # config_new.ini--server config file name
# con_server.read(con_server_path)
# Ver_local = con.get('ver','version')
# Ver_server = con_server.get('ver','version')

try:
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

except:
    logging.debug(traceback.format_exc())

try:
    os.system(Java_Path)
    sys.exit('install java')
except:
    logging.debug(traceback.format_exc())

Backup_Path = os.getcwd() + "/.minecraft/con_backup/inventoryprofilesnext"
Backup_File1 = ".minecraft\\config\\inventoryprofilesnext\\inventoryprofiles.json"
Backup_File2 = ".minecraft\\config\\inventoryprofilesnext\\ModIntegrationHints.json"
Con_Backup =".\\.minecraft\\con_backup\\inventoryprofilesnext"

try:
    if not os.path.exists(Backup_Path):
        os.makedirs(Backup_Path)
        os.system('copy %s %s' % (Backup_File1,Con_Backup))
        os.system('copy %s %s' % (Backup_File2,Con_Backup))
    else:
        os.system('copy %s %s' % (Backup_File1,Con_Backup))
        os.system('copy %s %s' % (Backup_File2,Con_Backup))
except:
    logging.debug(traceback.format_exc())

try:
    Unzip1 = zipfile.ZipFile("./mc_lib_1181.zip", mode='r')
    for names in Unzip1.namelist():
        Unzip1.extract(names, './.minecraft')  # unzip to .minecraft
        Unzip1.close()

    time.sleep(2)
    os.remove('mc_lib_1181.zip')
except:
    logging.debug(traceback.format_exc())