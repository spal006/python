import random
import string
import array
import re

#Password Primary values
LOCASE_CHARACTERS = string.ascii_lowercase
UPCASE_CHARACTERS = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation

class PasswordUtil:

    # init method or constructor
    def __init__(self, length, choiceoption):
        self.length = length
        self.filter = self.__populateFilter(choiceoption)

    def generatePassword(self):
        # Constants
        regex = r"(cisco)|(admin)"

        # get one each possible characters for password to meet the minimum requirement
        RAND_DIGIT = random.choice(DIGITS)
        RAND_UPPER = random.choice(UPCASE_CHARACTERS)
        RAND_LOWER = random.choice(LOCASE_CHARACTERS)
        RAND_SYMBOL = random.choice(SYMBOLS)

        #get a list of all possible charcters
        COMBINED_LIST = self.__populateCombinedList()
        TEMP_PASS = self.__populateTempPass()

        if COMBINED_LIST == '':
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

        if TEMP_PASS == '':
            TEMP_PASS = RAND_DIGIT + RAND_UPPER + RAND_LOWER + RAND_SYMBOL

        for x in range(self.length - 4):
            TEMP_PASS = TEMP_PASS + random.choice(COMBINED_LIST)

            # each time new char added it will resuffle to avoid same combination
            temp_pass_list = array.array('u', TEMP_PASS)
            random.shuffle(temp_pass_list)

        #create the password
        password = "".join(temp_pass_list)

        #check for blacklist keyword, in case present regenerate pw
        if (re.search(regex, password, re.MULTILINE)):
            generatePassword(self.length,finalFiter)

        return password

    def __populateTempPass(self):
        TEMP_PASS = ''
        filter = self.filter
        if 'symbol' in filter and filter['symbol']:
            TEMP_PASS = random.choice(SYMBOLS)
        if 'number' in filter and filter['number']:
            TEMP_PASS = TEMP_PASS + random.choice(DIGITS)
        if 'lower_case' in filter and filter['lower_case']:
            TEMP_PASS = TEMP_PASS + random.choice(LOCASE_CHARACTERS)
        if 'upper_case' in filter and filter['upper_case']:
            TEMP_PASS = TEMP_PASS + random.choice(UPCASE_CHARACTERS)

        return TEMP_PASS

    def __populateCombinedList(self):
        COMBINED_LIST = ''
        filter = self.filter
        if 'symbol' in filter and filter['symbol']:
            COMBINED_LIST = SYMBOLS
        if 'number' in filter and filter['number']:
            COMBINED_LIST = COMBINED_LIST + DIGITS
        if 'lower_case' in filter and filter['lower_case']:
            COMBINED_LIST = COMBINED_LIST + LOCASE_CHARACTERS
        if 'upper_case' in filter and filter['upper_case']:
            COMBINED_LIST = COMBINED_LIST + UPCASE_CHARACTERS

        return COMBINED_LIST

    def __populateFilter(self,choiceOption):
        finalFilter = {}
        optionList = choiceOption.split(',')
        if len(optionList) > 0:
            for option in optionList:
                option.strip()
                if str(option) == '':
                    continue
                if int(option) == 1:
                    finalFilter['symbol'] = True
                elif int(option) == 2:
                    finalFilter['number'] = True
                elif int(option) == 3:
                    finalFilter['lower_case'] = True
                elif int(option) == 4:
                    finalFilter['upper_case'] = True
        return finalFilter
