#guess the password.... 3 numbers.

import random
password= random.randint(100,999)
print(password)
#uncomment the above line for displaying the password if needed.
rep=True
while rep==True:
    choice= input("\n\n Enter your choice\n")
    if choice==password:
        print("Password is correct! Welcome!")
        rep=False
        print(">>")
    else:
        print("Invalid Password! Try again! ")
