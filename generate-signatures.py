#! /usr/bin/python

# File: generate-signatures.py
# Description:  It will generate and set up Gmail signatures for multiple users
#               Having a CSV file with user data (name, surname, phone, etc) and
#               a template file (see signature-template.html) it will generate
#               a signature file for each user. Finally, it will use GAM to set
#               up user's Gmail account to use the signature.
# Author: Xabier Ezpeleta - xezpeleta@tknika.eus

import csv
from string import Template
from os.path import join
from os import system

USERS_CSV = 'users.csv'
SIGN_TEMPLATE = 'signature-template.html'
SIGN_DIR = './generated'
GAM_PATH = '/usr/local/bin/gam'

def getUsersInfoFromCSV(csvFile):
  users = []
  print 'Reading user data from %s...' % (csvFile)
  with open(csvFile, 'rb') as f:
    data = csv.reader(f)
    fields = data.next()
    for row in data:
      items = zip(fields, row)
      item = {}
      for (name, value) in items:
        item[name] = value.strip()
      user = item
      users.append(user)
  return users

def modifyUsersInfo(users, item, value):
  for user in users:
    if user[item]:
      user[item] = value % user[item]
  return users

def generateSignatures(users, signsDir):
  print 'Generating signatures in %s...' % (signsDir)
  f = open(SIGN_TEMPLATE)
  src = Template(f.read())

  for user in users:
    r = src.substitute(user)
    filename = join(signsDir, '%s-signature.html' % user['username'])
    print filename
    with open(filename, 'w') as f:
      f.write(r)
      f.close()

def configureSignatures(users, signsDir):
  for user in users:
      filename = join(signsDir, '%s-signature.html' % user['username'])
      cmd = '%s user %s signature file %s html' % (GAM_PATH, user['email'], filename)
      print cmd
      system(cmd)


if __name__ == '__main__':
  users = getUsersInfoFromCSV(USERS_CSV)
  users = modifyUsersInfo(users, 'phone', '(+34) %s -')
  users = modifyUsersInfo(users, 'mobile', '(+34) %s -')
  generateSignatures(users, SIGN_DIR)
  configureSignatures(users, SIGN_DIR)
