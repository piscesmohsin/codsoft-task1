import string
import random
#getting password length
len = int(input("Enter password length\n"))

print("Choose Character set for password from these :")
print("1.Digits") 
print("2.Uppercase Letters")
print("3.Lowercase Letters")
print("4.Special Characters") 
print("5.Exit")

characterlist=""
#Getting character set for password 
while True:
    choice=int(input("Enter your choice:")) 
    if(choice==1):
        #Adding digits to possible characters
        characterlist += string.digits
    elif(choice==2):
        # Adding uppercase letters to possible characters
        characterlist += string.ascii_uppercase
    elif(choice==3):
        # Adding lowercase letters to possible characters
        characterlist += string.ascii_lowercase
    elif(choice==4):
        # Adding special characters to possible characters
         characterlist += string.punctuation 
    elif(choice==5):
        break
    else:
        print("Please enter a valid option")

# Initialize an empty list to store password
password=[ ]
for i in range(len):
    # picking a random character from characterlist 
    # randomchar is variable that store randomly choosen characterlist
    randomchar=random.choice(characterlist)
    # appending a random character to password
    password.append(randomchar)
#printing passsword as a string
print("The password is "+" ".join(password))
print("End")    

