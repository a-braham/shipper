import json
import requests
import psycopg2
import psycopg2.extras
from sys import argv

class _CoreConfig(object):
  def __init__(self, **kwargs):
    conn = psycopg2.connect(
      cursor_factory=psycopg2.extras.RealDictCursor,
      user='dom',
      password='00rat18tus',
      host='localhost',
      port='5432'
      **kwargs
      )

    cur = conn.cursor()
    cur.execute("SELECT * FROM table_one")
    results = cur.fetchall()
    print(results)

class Core(object):
  def __init__(self, *args):
    self.db = args

  def spreadsheet(self):
    config = _CoreConfig(
      database = self.db
    )

  def db2db(self):
    for db in self.db:
      config = _CoreConfig(
        database = db
      )
    
if __name__ == "__main__":
  Core(argv)