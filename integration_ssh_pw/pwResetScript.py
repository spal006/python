import paramiko
import sys
import time

sys.path.insert(0, '/Users/Sahoon/Project/python/password_generator')
from PasswordUtil import PasswordUtil



#setting parameters like host IP, username, passwd and number of iterations to gather cmds
HOST = "ec2-18-141-217-71.ap-southeast-1.compute.amazonaws.com"
USER = "ec2-user"
PASS = "passwd"
ITERATION = 1

#A function that logins and execute commands
def fn():
    client1=paramiko.SSHClient()

    #Add missing client key
    client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #connect to switch
    # client1.connect('hst',username=user,password=PW)
    client1.connect(HOST,username=USER)
    print ("SSH connection to %s established" %HOST)

    # #Gather commands and read the output from stdout
    # stdin, stdout, stderr = client1.exec_command('date')

    # # print (type(stdout.read()))
    # print (stdout.read().decode("utf-8"))



    channel = ssh.invoke_shell()
    channelData = ""

    while True:
        if channel.recv_ready():
            channelData += channel.recv(9999)
            os.sytem('cls')
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




