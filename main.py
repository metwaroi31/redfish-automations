import redfish
import subprocess
import redfish
from utils.redfish import redfishClient
from config import *
from utils.file_interface import get_input_list

ip_list, pwd_list = get_input_list(INPUT_IP_LIST)
for i in range(0, len(ip_list)):
    login_password = pwd_list[i]
    iLO_host = ip_list[i]

    server = redfishClient(iLO_host, login_password)
    try :
        print (server.login())
        server.update_firmware(VME_FILE_URL)
    except ValueError as err:
        print (err)
