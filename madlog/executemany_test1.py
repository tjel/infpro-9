import sys
import cx_Oracle
import os

connection = cx_Oracle.Connection('rt_projekt/projekt@umain')  # dane do logowania
cursor = connection.cursor()

tabofvar = []
tabofvar.append(('0.000', '0.0125', '2015:10:15:09:41:18'))
tabofvar.append(('0.063', '0.0236', '2015:10:15:11:01:12'))
tabofvar.append(('0.126', '0.0351', '2015:10:15:09:31:07'))
tabofvar.append(('0.188', '0.1092', '2015:10:15:11:13:13'))
tabofvar.append(('0.251', '0.2223', '2015:10:15:13:56:56'))
tabofvar.append(('0.314', '0.2392', '2015:10:15:16:38:09'))
tabofvar.append(('0.377', '0.2395', '2015:10:15:19:22:24'))
tabofvar.append(('0.440', '0.4125', '2015:10:15:22:01:09'))
tabofvar.append(('0.503', '0.1751', '2015:10:16:01:19:45'))
tabofvar.append(('0.565', '0.0233', '2015:10:16:04:21:18'))
tabofvar.append(('0.628', '0.0210', '2015:10:16:06:01:19'))


print(tabofvar)
'''
j = 0
for i in tabofvar:
    print(tabofvar[j])
    j += 1'''

reader = open("job_history.txt","r")
lines = []
for line in reader:
    lines.append(line)
    #print line
print lines

cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY:MM:DD:HH24:MI:SS'")
cursor.prepare("INSERT INTO T654 VALUES(:1,:2,:3)")
cursor.executemany(None, tabofvar)
connection.commit()

# DZIALA BEZ JEDNOKRESKOW W LICZBACH
