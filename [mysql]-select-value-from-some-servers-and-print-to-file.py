# PYTHON SCRIPT, tested on v3.4.4
# SELECT hstate from several servers and WRITE results/errors to file

import mysql.connector
import sys
import datetime
from mysql.connector import errorcode

# servers configurations
srv1 = ["nazwa_serwera1", "127.0.0.1", "3006"]
srv2 = ["nazwa_serwera2", "127.0.0.1", ""]
srv3 = ["nazwa_serwera3", "127.0.0.1", "3006"]
srv4 = ["nazwa_serwera4", "127.0.0", "3006"]
srv5 = ["nazwa_serwera5", "127.0.0.1", "3006"]

srvs=[srv1,srv2,srv3,srv4,srv5]

def state(n,h,p,f):
# Try to connect
 try:
  cnx = mysql.connector.connect(user='root',
                                host=h,
                                port=p,
								pass='pass',
                                database='dbname')
 except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      f.write("Something is wrong with your user name or password")
      f.close()
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
      f.write("Database does not exist")
      f.close()
  else:
      f.write(err)
      f.close()
 else:
    f.write("location: "+n+' ('+ h +':'+p +') : ')

    cursor = cnx.cursor()
 query = ("SELECT open, value FROM state ORDER BY date DESC LIMIT 1")
 res =cursor.execute(query)
 for res in cursor.fetchall():
    f.write(str(res) + '\n')
 cursor.close()
 cnx.close()

def trycs(param,f):
    try:
        state(param[0],param[1],param[2],f)
    except:
        f.write("location: "+ param[0] + ' (' + param[1] + ':' + param[2] + ')'+ " Problem z po³¹czeniem do serwera." '\n')

def make():
    # Create new file
    filename = "Report__ " + datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S" + ".txt")

    f = open(filename, 'w+')

    f.write(
        "  REPORT DATE: " + datetime.datetime.now().strftime("%d/%m/%y-%H:%M:%S") + '\n' + '\n')

    for i in range(len(srvs)):
      trycs(srvs[i],f)

    f.close()
    raise SystemExit()

make()

