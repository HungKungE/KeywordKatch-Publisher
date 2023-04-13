import pymysql
import sys
import logging

#RDS INFO
host = "localhost" # end point
port = 3306
username = "root"
database = "findvibe_db"
password = "findvibe1"

# function

def connectionRDS():
  try:
    conn=pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, use_unicode=True, charset="utf8")
    cursor = conn.cursor()
  except Exception as e:
    logging.error("RDS연결 실패:"+str(e))
    sys.exit(1)

  return conn, cursor

def getAllUserInfo(cursor):
  query = "SELECT * FROM user_info"

  cursor.execute(query)
  result = cursor.fetchall()

  return result