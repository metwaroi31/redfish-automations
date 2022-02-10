import subprocess
import ast
from .CURL_command import *

class redfishClient():
    def __init__(self, iLO_host, ilO_password):
        self.port = 443
        self.iLO_host = iLO_host
        self.ilO_password = ilO_password
        self.ilO_user = "Administrator"        

    def login(self):
        
        url = "https://" + self.iLO_host + "/redfish/v1/SessionService/Sessions/"
        
        extra_options = ['-i', '-k', 'X', '-s']
        data = {"UserName": self.ilO_user, "Password": self.ilO_password}
        headers = ["Content-Type: application/json", "OData-Version: 4.0"]
        login_command = construct_command(headers, data, url, extra_options)
        login_command = get_grep(login_command, "Token")
        
        command_output = subprocess.run(login_command, capture_output=True)
        output, err, return_code = command_output.stdout, command_output.stderr, command_output.returncode
        
        self.token = output
        return self.token

    def update_firmware(self, image_file):
        # data = {
        #     "ImageURI" : image_file
        # }
        # update_command = ['redfishtool', 'raw', 'POST', \
        #                         '/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate/', \
        #                             '-t', self.token, '-d', str(data)]
        #                             extra_options = ['-i', '-k', 'X', '-s']
        extra_options = ['-i', '-k', 'X', '-s']
        url = "https://" + self.iLO_host + "/redfish/v1/SessionService/Sessions/"
        data = {}
        headers = ["Cookie: sessionKey=" + str(self.token), "OData-Version: 4.0"]
        file_options = ["UpdateRepository=true", "UpdateTarget=true", "ETag=atag", "Section=0", "sessionKey" + str(self.token), "file=" + image_file ]
        update_command = construct_command(headers, data, url, extra_options, file_options)
        command_output = subprocess.run(update_command, capture_output=True)

        output, err, return_code = command_output.stdout, command_output.stderr, command_output.returncode
        if return_code == 0:
            return True
        else :
            raise  ValueError(err)
        