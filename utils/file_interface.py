import pandas as pd

def get_input_list(csv_file):
    df = pd.read_csv(csv_file)
    ip_list = []
    pwd_list = []
    for i in range(0, df.shape[0]):
        ip_list.append(df.iloc[i, 0])
        pwd_list.append(df.iloc[i, 1])
    print (ip_list)
    print (pwd_list)
    return ip_list, pwd_list
    