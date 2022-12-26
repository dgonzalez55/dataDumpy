import argparse
import os
import pyfiglet
from mySQLDumper import mySQLDumper

def clearScreen(): os.system('cls' if os.name == 'nt' else 'clear')

def showTitle():
  clearScreen()
  pyfiglet.print_figlet("DataDumpy.py", font="doom")
  print("MySQL/MariaDB Data Dumper")
  print("Author: @dgonzalez55 a.k.a. MaeseLeGon")
  print("Github: https://github.com/dgonzalez55/dataDumpy")
  print("Version: 1.0.0")
  print("")

def mainMenu():
  print("1. Dump All Databases")
  print("2. Dump Database")
  print("3. Dictionary Attack")
  print("4. Dictionary Attack + Dump All Databases")
  print("5. Exit")
  print("")
  option = input("Select an option: ")
  return option

def loadParams():
  parser = argparse.ArgumentParser(description='DataDumpy.py - MySQL/MariaDB Data Dumper',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  # Just a hack to change the title of default options
  parser._optionals.title = "Basic Options"
  parser.add_argument('--host', dest="hostname", help='Hostname/IP address', required=True)
  parser.add_argument('--port', dest="port", help='Port', required=False, default=3306)
  parser.add_argument('--database', dest="database", help='Database', required=False, default=None)
  parser.add_argument('--user', dest="username", help='Username', required=False, default='root')
  parser.add_argument('--password', dest="password", help='Password', required=False, default='')
  advanced = parser.add_argument_group(title="Advanced Options", description="These options are advanced and may not be needed for most users.")
  advanced.add_argument('--wordlist', dest="wordlist", help='Used when Dictionary Attack selected', required=False, default='wordlist.txt')
  advanced.add_argument("--verbose", dest="verbose", help="Verbose output", action="store_true",required=False)
  advanced.add_argument("--avoid-sysdbs", dest="avoidSysDBs", help="Avoid dumping system databases", action="store_true",required=False)
  advanced.add_argument("--ssl-disabled", dest="ssl_disabled", help="Disable SSL Encryption", action="store_true",required=False)
  return parser.parse_args()

if __name__ == "__main__":
  db = mySQLDumper(**vars(loadParams()))
  showTitle()
  option = mainMenu()
  match option:
    case "1": db.dumpAllDatabases()
    case "2": database = db.currentDatabase if(db.currentDatabase != None) else input("Database: "); db.dumpDatabase(database)
    case "3": db.wordlistAttack()
    case "4": db.wordlistAttack(); db.dumpAllDatabases()

print("Remember this tool is for educational purposes only!")

