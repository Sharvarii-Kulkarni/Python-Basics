import os
from email.policy import default

print("1. Open\n2.Write\n3.Read\n4.Writeline\n5.readLine\n6.close\n7.rename\n8.Delete file\nchose from 1-8")
userin = eval(input("Enter operation you want to perform: "))

if userin==1:
    f = open("a.txt","w")
    print('File is opened')
elif userin==2:
    f = open("a.txt","w")
    f.write("Hello, I am S")
elif userin==3:
    f = open("a.txt","r")
    rd = f.read()
    print(rd)
elif userin==4:
    f = open("a.txt", "w")
    f.writelines("I am learning python. Its very fun")
elif userin==5:
    f = open("a.txt", "r")
    print(f.readline())
elif userin==6:
    f = open("a.txt", "r")
    f.close()
    print('file  is closed')
elif userin==7:
    os.rename("a.txt","b.txt")
elif userin==8:
    os.remove("a.txt")
else:
    print("enter valid choice")