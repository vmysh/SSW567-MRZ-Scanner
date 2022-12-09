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
    print("Scanning MRZ")
    #Should return line 1 and line 2 

#Requirement 2: Decoding the Strings
def decodeStrings(line1,line2):
    #line1
    passportType=line1[0]
    issCountry=line1[1:4]
    nameHold=line1[4:]
    nameHold=nameHold.replace('<',"")   #Need to get a way to get name separated

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
    
#Requirement3: Encode
def encodeStrings():
    print("code")
    #encode requirement code here

#Requirement4: reporting miss matching information between encode and decode
def reportDifference():
    print("code")
    #Code Here to Report the Differences
   

line1="PUTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<"
line2="L898902C36UTO7408122F1204159ZE184226B<<<<<<<1"
