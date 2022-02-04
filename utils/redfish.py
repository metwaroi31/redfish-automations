import subprocess
import ast

class redfishClient():
    def __init__(self, iLO_host, ilO_password):
        self.port = 443
        self.iLO_host = iLO_host
        self.ilO_password = ilO_password
        self.ilO_user = "root"        

    def login(self):
        login_command = ['redfishtool', 'SessionService', '-a', 'login', \
                                    '-r' + str(self.iLO_host) + ':' + str(self.port), '-u', str(self.ilO_user), '-p', str(self.ilO_password),\
                                    '-S', 'Never']
        command_output = subprocess.run(login_command, capture_output=True)
        output, err, return_code = command_output.stdout, command_output.stderr, command_output.returncode
        if return_code == 0:
            self.token = ast.literal_eval(output.decode('utf-8'))['X-Auth-Token']
        else :
            raise ValueError ("Internet connection problems, please retry for host " + self.iLO_host)
        return self.token

    def update_firmware(self, image_file):
        data = {
            "ImageURI" : image_file
        }
        update_command = ['redfishtool', 'raw', 'POST', \
                                '/redfish/v1/UpdateService/Actions/UpdateService.SimpleUpdate/', \
                                    '-t', self.token, '-d', str(data)]
        command_output = subprocess.run(update_command, capture_output=True)

        output, err, return_code = command_output.stdout, command_output.stderr, command_output.returncode
        print (output)
        print (err)
        print (return_code)
        return
