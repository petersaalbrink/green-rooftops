#!/usr/bin/env python3
import mysql.connector
from mysql.connector import ClientFlag
import numpy as np
import pandas as pd

config = {
    'user': 'trainee_peter',
    'password': 'peter01',
    'host': '104.199.69.152',
    'database': 'mx_traineeship_peter',
    'raise_on_warnings': True,
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem'}

cnx = mysql.connector.connect(**config)
cnx.autocommit = True
cursor = cnx.cursor(buffered=True)

# cursor.execute("SELECT * FROM real_estate_data WHERE gemeentenaam = 'Amsterdam'")
# real_estate_data = [list(row) for row in cursor.fetchall()]

# # kolom toevoegen: zit er een bedrijf op dit adres? 
# # cursor.execute("SELECT * FROM real_estate_data WHERE gemeentenaam = 'Amsterdam'")

# cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'real_estate_data'")
# fields = np.array([list(row) for row in cursor.fetchall()]).ravel()

# df = pd.DataFrame(data=real_estate_data, columns=fields)
# df.index = np.arange(1, len(df) + 1)

# # kolom toevoegen: stadsdeel (adhv wijkcode) in python

# postcodes = {'1000-1018': 'Amsterdam-Centrum',
# '1013-1014': 'Amsterdam-West',
# '1019': 'Amsterdam-Oost',
# '1020-1039': 'Amsterdam-Noord',
# '1040-1049': 'Amsterdam Westpoort',
# '1050-1059': 'Amsterdam-West',
# '1060-1069': 'Amsterdam Nieuw-West',
# '1070-1083': 'Amsterdam-Zuid',
# '1086-1099': 'Amsterdam-Oost',
# '1100-1108': 'Amsterdam-Zuidoost'}

# df.to_csv('real_estate_data.csv', index=False, encoding='utf8')

cursor.close()
cnx.close()
