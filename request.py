import urllib3
import numpy as np
import pandas as pd

# запрос данных из сети
http = urllib3.PoolManager()
url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
resp = http.request('GET', url)
data = resp.data.decode('utf-8')

# объявлению пустых массивов
array_ip =  np.array([])
array_date =  np.array([])
array_way =  np.array([])
array_numbers = np.array([])
array_dash = np.array([])
array_user_agent = np.array([])

array_lines =  data.split("\n") #  разбиение данных на строки

# разбиение строк на отдельные фрагменты и запись фрагментов в ряды
for i in range(len(array_lines)-1):
    temp = array_lines[i].split(" - - ")
    array_ip = np.append(array_ip, temp[0])
    split_temp = temp[1].split("\"")
    array_date = np.append(array_date, split_temp[0])
    array_way = np.append(array_way, split_temp[1])
    array_numbers = np.append(array_numbers, split_temp[2])
    array_dash = np.append(array_dash, split_temp[3])
    array_user_agent = np.append(array_user_agent, split_temp[5])
    print(i)

# сборка рядов в таблицу
df_log = pd.DataFrame({"ip": array_ip, "date" : array_date, "way" : array_way,
                       "numbers" : array_numbers, "dash" : array_dash, "user agent" : array_user_agent})

export_csv = df_log.to_csv(r'log file.csv', index=None, header=True)











