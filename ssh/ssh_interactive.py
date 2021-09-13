import paramiko
import sys
import time


#setting parameters like host IP, username, passwd and number of iterations to gather cmds
HOST = "host"
USER = "user"
PASS = "passwd"
ITERATION = 3

#A function that logins and execute commands
def fn():
  client1=paramiko.SSHClient()

  #Add missing client key
  client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  #connect to switch
  # client1.connect('hst',username=user,password=PW)
  client1.connect(HOST,username=USER)
  print ("SSH connection to %s established" %HOST)

  #Gather commands and read the output from stdout
  stdin, stdout, stderr = client1.exec_command('date')

  # print (type(stdout.read()))
  print (stdout.read().decode("utf-8"))
  client1.close()
  print ("Logged out of device %s" %HOST)

#for loop to call above fn x times. Here x is set to 3
for x in range(ITERATION):
  fn()
  print ("%s Iteration/s completed" %(x+1))
  print ("********")
  time.sleep(5) #sleep for 5 seconds