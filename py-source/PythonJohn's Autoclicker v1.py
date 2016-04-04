#!/usr/bin/python

import win32api, win32con
import time, sys
import httplib, urllib


def checkforupdates():
  try:
    params = urllib.urlencode({'p': 'autoclicker', 'v': 1})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    http = httplib.HTTPConnection("pythonjohn.com", 80, timeout=5 )
    http.request( "POST", "/checkforupdates.php", params, headers )
    response = http.getresponse()
    data = response.read()
    http.close()
  except Exception, e:
    data = "We could not reach the server, check your internet connection or firewall."

  return data

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def headers():
  print '\n\n\n\n'
  print 'Simple AutoClicker By John Minton cjohnweb@gmail.com\n\n'
  print 'Get more cool Python Scripts from http://pythonjohn.com/\n\n' 
  print '***********************************************************\n'
  sys.stdout.write('Checking for updates: ')
  data = checkforupdates()
  print data + '\n\n***********************************************************'
  print '\n\n'
  print 'Press left CTRL to rapid left-click mouse button\n\n'
  print 'Press right CTRL to close program\n\n' 

def autoclicker():
  while True:
  
    while win32api.GetAsyncKeyState(win32con.VK_LCONTROL):
      print 'Left CTRL'
      a, b = win32api.GetCursorPos()
      click(a, b)
      time.sleep(0.01)
  
    if win32api.GetAsyncKeyState(win32con.VK_RCONTROL):
      exit()

def main():
  headers()
  autoclicker()  

main()

exit()
