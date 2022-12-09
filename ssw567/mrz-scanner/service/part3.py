'''
    1) The system shall be able to scan the MRZ of a travel document using a hardware device scanner and get
       the information in MRZ as two strings (line 1 and line 2 from the above Figure). Note that you do not 
       need to worry about the implementation of the hardware device. But you need to define this method for 
       the software part. This means that you define an empty method for this function. 
    2) The system shall be able to decode the two strings from specification #1 into their respective fields
       and identify the respective check digits for the fields, following the same format in the above example.
    3) The system shall be able to encode travel document information fields queried from a database into the 
       two strings for the MRZ in a travel document. This is the opposite process compared to specification #2. 
       Assume that the database function is not ready. But for testing purposes, you need to define a method for 
       database interaction and leave it empty.
    4) The system shall be able to report a mismatch between certain information fields and the check digit. The
       system shall report where the miss match happened, i.e. which information field does not match its respective check digit.


       Example Line 1: PUTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<
                       P UTO ERIKSSON ANNA MARIA
       Example Line 2: L898902C36UTO7408122F1204159ZE184226B<<<<<<< 1
                       L898902C3 6 UTO 740812 2 F 120415 9 ZE184226B <<<<<<< 1 
'''
import string

#Variable Initialization
#line1 variables
passportType=""
issCountry=""
nameHold=""

#line1 variables
passNum=-1
countrCode=""
birthDate=-1
gender=""
expDate=-1
persNum=-1

#check variables
check1=-1
check2=-1
check3=-1
check4=-1

#Requirement 1: Function mocking the hardware device scanner 
def scanMRZ():
    print("- - - Scanning MRZ - - -")
    scanInfo="P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
    return scanInfo
    #Should return line 1 and line 2 

#Requirement 2: Decoding the Strings
def decodeStrings(line1,line2):
    line1Array=[]
    line2Array=[]
    #line1
    passportType=line1[0]
    issCountry=line1[1:4]
    nameHold=line1[4:]
    nameHold=nameHold.replace('<',"")   #Need to get a way to get name separated
    #creating Array for Comparison Purposes
    line1Array.append(passportType)
    line1Array.append(issCountry)
    line1Array.append(nameHold)

    #line2
    passNum=line2[0:9]
    check1=line2[9]
    countrCode=line2[10:13]
    birthDate=line2[13:19]
    check2=line2[19]
    gender=line2[20]
    expDate=line2[21:27]
    check3=line2[27]
    persNum=line2[28:]
    persNum=persNum.replace('<',"")
    check4=persNum[-1]
    persNum=persNum[:-1]
    #creating Array for Comparison Purposes
    line2Array.append(passNum)
    line2Array.append(check1)
    line2Array.append(countrCode)
    line2Array.append(birthDate)
    line2Array.append(check2)
    line2Array.append(gender)
    line2Array.append(expDate)
    line2Array.append(check3)
    line2Array.append(persNum)
    line2Array.append(check4)

    return line1Array, line2Array
    
#Requirement3: Encode
#function to mock a call to a database to return information 
def getFromDatabase():
    dbInfo=["P","UTO","ERIKSSON","ANNA","MARIA","L898902C3", "UTO",740812, "F",120415,"ZE184226B"]
    return dbInfo


#Veronika is working on this function right now
#Passing an array of the information from Line 2 of the MRZ into this function
#The structure of the array can be changed, but the indexes would have to change too

#Array used for testing, delete later!!!!
testarray = ["P","UTO","ERIKSSON","ANNA","MARIA","L898902C3", "UTO",740812, "F",120415,"ZE184226B"]
def calcCheck(line2arr): 
    #Assigning number values to letters
    #can only have 1 letter at a time
    values = dict()
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 10
    #print(values["C"])

    #breaking up strings/numbers into arrays of characters
    def split(info):
        splitChar = []
        if type(info) is str:
            for letter in info:
                splitChar.append(letter)
        else:
            #splitChar = [int(a) for a in str(info)]
            splitChar = list(map(int, str(info)))

        return splitChar

    #this function assigns numeric values to letters/number
    #pass in an array that represents the split characters of a term (like DOB or passport #)
    #this split array is generated by split(), which ceates a splitChar array
    #the output is an array (numericVal) of the corresponding number values, type int
    def assignVal(splitArr):
        numericVal = []
        for value in splitArr:
            if (value == "1" or value == "2" or value == "3" or value == "4" or value == "5" or value == "6" or value == "7" or value == "8" or value == "9" or value == "0"):
                numericVal.append(int(value))
            elif type(value) is int:
                numericVal.append(value)
            else:
                numericVal.append(values[value])

        return numericVal

    #this function calculates the final check number
    #takes in the resulting array of ints (numericVal[]) from assignVal() function
    #multiplies each number by weighting factor 7,3,1
    #sums all numbers
    #takes mod10 of the sum
    #the result is an integer value - the check digit
    def finalCheckDig(numArr):
        multFactors = []
        i = 0
        while i < len(numArr):
            multFactors.append(numArr[i]*7)
            multFactors.append(numArr[i+1]*3)
            multFactors.append(numArr[i+2]*1)
            i = i + 3

        sum = 0
        for num in multFactors:
            sum += num

        checkDig = sum%10
        return checkDig


    #check digit for passport number (initially a string)
    passportNo = finalCheckDig(assignVal(split(line2arr[5])))

    #check digit for birth date (initially a number)
    birthday = finalCheckDig(assignVal(split(line2arr[7])))


    #check digit for expiration date (initially a number)
    expiration = finalCheckDig(assignVal(split(line2arr[9])))


    #check digit for personal number (initially a string)
    personalNo = finalCheckDig(assignVal(split(line2arr[10])))

    #array with final 4 check digits [passport, DOB, exp, personal #]
    checkDigits = [passportNo, birthday, expiration, personalNo]
    #delete print statement after!!!
    print(checkDigits)
    return checkDigits

def encodeStrings(dbInfo):
    mrzLine1=""
    mrzLine2=""
    dbLine1=dbInfo[0:3]
    dbLine2=dbInfo[3:]
    print(dbLine1)
    print(dbLine2)
    #encode requirement code here