import redfish
import subprocess
import redfish

login_account = "root"
login_password = "password123456"
iLO_host = "https://127.0.0.1"
REDFISH_OBJ = redfish.RedfishClient(base_url=iLO_host,username=login_account, \
                          password=login_password)

# Login into the server and create a session
REDFISH_OBJ.login(auth="session")

# Do a GET on a given path
response = REDFISH_OBJ.get("/redfish/v1/systems/", None)

# Print out the response
sys.stdout.write("%s\n" % response)

# Logout of the current session
REDFISH_OBJ.logout()
