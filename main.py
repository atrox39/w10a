import json
import sys
from os import system
import ctypes

if not ctypes.windll.shell32.IsUserAnAdmin():
  print('Need user administrator permission for program operation')
  system('pause')
  sys.exit(0)

servers = ['kms.digiboy.ir', 'kms.msguides.com']
file = open('keys.json', 'r')
keys = json.loads(file.read())
listOS = list(keys.keys())
file.close()

def mainMenu():
  global listOS
  system('cls')
  print('Select OS to activate')
  for i in range(0, len(listOS)):
    print('{}.- {}'.format((i + 1), listOS[i]))
  print('{}.- Exit'.format(len(listOS) + 1))
  selection = input('Type num of selection: ')
  return int(selection) - 1

def osTypeMenu(key: str):
  global keys
  system('cls')
  print('Select OS Type')
  osType = list(keys[key].keys())
  for i in range(0, len(osType)):
    print('{}.- {}'.format(i + 1, osType[i]))
  selection = int(input('Select os type: '))
  return osType[selection - 1]

def osSubversionMenu(os: str, key: str):
  global keys
  system('cls')
  print('Select OS Subversion')
  osSubversion = list(keys[os][key].keys())
  for i in range(0, len(osSubversion)):
    print('{}.- {}'.format(i + 1, osSubversion[i]))
  selection = int(input('Select os subversion: '))
  return osSubversion[selection - 1]

def osKeyMenu(os: str, osType: str, osSubversion: str):
  global keys
  system('cls')
  print('Select OS Key')
  all = list(keys[os][osType][osSubversion])
  for i in range(0, len(all)):
    print('{}.- {}'.format(i + 1, all[i]))
  selection = int(input('Select os Key: '))
  return all[selection - 1]

def osServerMenu():
  global servers
  system('cls')
  print('Select OS activation server')
  for i in range(0, len(servers)):
    print('{}.- {}'.format(i + 1, servers[i]))
  selection = int(input('Select os server: '))
  return servers[selection - 1]

def start():
  global listOS
  global keys
  menu = True
  while menu:
    selection = mainMenu()
    osSelection = listOS[selection]
    if (selection == -1):
      menu = False
      break
    osType = osTypeMenu(osSelection)
    osSubversion = osSubversionMenu(osSelection, osType)
    osKey = osKeyMenu(osSelection, osType, osSubversion)
    server = osServerMenu()
    system('slmgr /ipk {}'.format(osKey))
    system('slmgr /skms {}'.format(server))
    system('slmgr /ato')
    input('Successfully if not correctly activate please re run program and select another key or activation server')
    break

if __name__ == '__main__':
  start()