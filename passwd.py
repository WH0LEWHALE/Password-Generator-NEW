import string
import random
 
charlength = int(input("Enter password length: "))
 
print('''
Choose character set for password from here : 
         1. Digits/Numbers
         2. Letters
         3. Special Characters
         4. Exit/Leave or see the results
''')
 
charList = ""
 
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
        charList += string.ascii_letters
    elif(choice == 2):
        charList += string.digits
    elif(choice == 3):
        charList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(charlength):
    randchar = random.choice(charList)
    password.append(randchar)
 
print("Your random password is " + "".join(password))
