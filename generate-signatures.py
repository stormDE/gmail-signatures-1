#! /usr/bin/python

#import sys
import csv
from string import Template
from os.path import join
from os import system

USERS_CSV = 'users.csv'
SIGN_DIR = './generated'

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

def generateSignatures(users, signsDir):
  print 'Generating signatures in %s...' % (signsDir)
  f = open('signature-template.html')
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
      cmd = '/usr/bin/python ../../gam.py user %s signature file %s' % (user['email'], filename)
      print cmd
      system(cmd)


if __name__ == '__main__':
  users = getUsersInfoFromCSV(USERS_CSV)
  generateSignatures(users, SIGN_DIR)
  configureSignatures(users, SIGN_DIR)
