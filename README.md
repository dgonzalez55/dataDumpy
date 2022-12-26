[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT) ![Stable Release](https://img.shields.io/badge/stable_release-1.0.0-blue.svg)

![logo](https://raw.githubusercontent.com/dgonzalez55/dataDumpy/main/logo.png "DataDumpy Logo")

Disclaimer: **FOR EDUCATIONAL PURPOSE ONLY! The contributors do not assume any responsibility for the use of this tool.**

# DataDumpy - A simple MySQL/MariaDB Data Dumper 🧑‍💻
Developed by David González [dgonzalez55](https://github.com/dgonzalez55/)

Latest Release: v1.0.0. December 26, 2022

License: MIT

This product is subject to the terms detailed in the license agreement.

If you have any questions, comments or concerns regarding DataDumpy, please consult the documentation prior to contacting one of the developers. Your feedback is always welcome. 

##  Contents 🧰

* About DataDumpy
* Installation
* Example Usage
* Usage 

## About DataDumpy ℹ

DataDumpy is a red team tool that could be used to extract all data from a MySQL/Maria DB target within only SELECT permissions avoiding all typical problems of using common tools such as mysqldump. Moreover, it allows to perform classic dictionary attacks against our dbms in order to retrieve any unknown password. Finally, it offer some interesting features like deactivating ssl checks (mandatory for testing old systems) or skipping system databases from the dumping process.


### Features
* Common MySQL/MariaDB wordlist provided.
* Dump all databases.
* Dump a single database.
* Perform a Dictionary Attack.
* Mix a Dictionary Attack and Dump all Databases.
* CSV format for dumps.
* Error control.

## Installation ⚙️

1. Fork/Clone/Download this repo

    `git clone https://github.com/dgonzalez55/dataDumpy.git`

2. Navigate to the directory

    `cd dataDumpy`

3. Create a virtual environment for this project

    `python -m venv venv`

4. Load the virtual environment
   - On Windows Powershell: `.\venv\Scripts\activate.ps1`
   - On Linux and Git Bash: `source venv/bin/activate`
  
5. Run `pip install -r requirements.txt`

6. Run the dataDumpy.py script

    `python dataDumpy.py <target_options>`

## Example Usage ✌

Using dataDumpy.py to dump from a localhost with known credentials, skipping system databases and verbose activated.

```
$ ./python dataDumpy.py --host localhost --user root --password root --avoid-sysdbs --verbose

```

## Usage 🛠
```
usage: dataDumpy.py [-h] --host HOSTNAME [--port PORT] [--database DATABASE] [--user USERNAME] [--password PASSWORD] [--wordlist WORDLIST] [--verbose] [--avoid-sysdbs] [--ssl-disabled]

DataDumpy.py - MySQL/MariaDB Data Dumper

Basic Options:
  -h, --help           show this help message and exit
  --host HOSTNAME      Hostname/IP address (default: None)
  --port PORT          Port (default: 3306)
  --database DATABASE  Database (default: None)
  --user USERNAME      Username (default: root)
  --password PASSWORD  Password (default: )

Advanced Options:
  These options are advanced and may not be needed for most users.

  --wordlist WORDLIST  Used when Dictionary Attack selected (default: wordlist.txt)
  --verbose            Verbose output (default: False)
  --avoid-sysdbs       Avoid dumping system databases (default: False)
  --ssl-disabled       Disable SSL Encryption (default: False)

```

