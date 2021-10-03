import paramiko
import sys
import os
import time
from password_generator import PasswordUtil



#setting parameters like host IP, username, passwd and number of iterations to gather cmds
HOST = "10.200.105.38"
USER = "pyadmin"
PASS = "F93z#oRu"
ITERATION = 1

#A function that logins and execute commands
def fn():
    client1=paramiko.SSHClient()

    #Add missing client key
    client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #connect to switch
    client1.connect(HOST,username=USER,password=PASS)
    # client1.connect(HOST,username=USER)
    print ("SSH connection to %s established" %HOST)

    # #Gather commands and read the output from stdout
    # stdin, stdout, stderr = client1.exec_command('date')

    # # print (type(stdout.read()))
    # print (stdout.read().decode("utf-8"))



    channel = client1.invoke_shell()
    channelData = str()
    channel.send('password')
    while True:
        if channel.recv_ready():
            channelData += channel.recv(9999).decode('utf-8')
            os.system('cls')
            print ("##### Device Output #####")
            print (channelData)
            print ("#####      END      #####")
        else:
            continue

        if channelData.endswith("Enter old password:"):
            channel.send(PASS)
            channel.send('\n')
        elif channelData.endswith("Enter new password:"):
            passwObj = PasswordUtil(10,'1,2,3,4')
            password = passwObj.generatePassword()
            channel.send(password)
            channel.send('\n')
        elif channelData.endswith("SSH connection to 10.200.105.38 established"):
            channel.send('\n')
        elif channelData.endswith("Enter session number to resume or press <Enter> to start a new one:"):
            channel.send('\n')
        else:
            host = raw_input('Want to exit then type \'exit;\'?')
            channel.send(host)
            channel.send('\n')


    client1.close()
    print ("Logged out of device %s" %HOST)

# #for loop to call above fn x times. Here x is set to 3
for x in range(ITERATION):
    fn()
    print ("%s Iteration/s completed" %(x+1))
    print ("********")
    time.sleep(5) #sleep for 5 seconds
    print ("DONE!!!!!!!")




