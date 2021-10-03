from PasswordUtil import PasswordUtil

def main():
    #input the length of password
    length = int(input('\nEnter the length of password (>8): '))
    #input the condition for password
    print ("1. Include Symbols \n2. Include Numbers \n3. Include lower case \n4. Include upper case \n ")
    choiceOption = str(input('\nEnter Choice Comma Separate: '))
    # finalFiter = populateFilter(choiceOption)

    # Should not allow below 8 digit password
    if (length < 8):
        print("Password should not be less than 8 characters.")
        main()
    else:
        # password = generatePassword(length,finalFiter)
        # Class implementation :
        passwObj = PasswordUtil(length,choiceOption)
        password = passwObj.generatePassword()
        print  ("Password : " + password)


#main class
if __name__ == '__main__':
    print('Welcome to Password generator!')
    main()
