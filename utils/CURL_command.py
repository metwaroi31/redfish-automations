def construct_command(headers, data, url, extra_options, file_options=None):
    # curl -i -k -X POST --data '{"UserName": "Administrator", "Password": "'"$ilopw"'"}' --header "Content-Type: application/json"
    #      --header "OData-Version: 4.0" https://$bmcip/redfish/v1/SessionService/Sessions/ -s | grep Token

    command_to_execute = ["curl"]
    for option in extra_options:
        command_to_execute.append(option)
    
    for header in headers:
        command_to_execute.append("--header")
        command_to_execute.append(header)
    if file_options is not None:
        print (file_options)
        for file_option in file_options:
            command_to_execute.append("-F")
            command_to_execute.append(file_option)
    command_to_execute.append("--data")
    command_to_execute.append(str(data))
    command_to_execute.append(url)
    
    return command_to_execute

def get_grep (command, grep_option):
    command.append ("| grep " + grep_option)
    return command
