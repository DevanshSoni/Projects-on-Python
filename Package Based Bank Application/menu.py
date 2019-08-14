from Auth import *
from operation import *
from db import *
import os
def main_menu():
    os.system('cls')
    li=['1 :- Login','2 :- Sign_Up','3 :- Exit']
    ch=1
    while ch!=3:
        for i in li:
            print(i)
        ch=int(input("Select from the options above"))
        if ch==1:
            acc_no=input("Enter Acc_No to access your account")
            password=input("Enter Password")
            check=login(acc_no,password)
            if check:
                sub_menu(acc_no)
        elif ch==2:
            sign_up()
    else:
        print("Thank You for using our Services have a nice day :-)")
def sub_menu(id):
    os.system('cls')
    option=1
    while(option!=6):
        print('1 :- Debit Amount')
        print('2 :- Credit Amount')
        print('3 :- Check Balance')
        print('4 :- Account Information')
        print('5 :- Update Account Info.')
        print('6 :- Log out')
        option=int(input())
        if option ==1 :
            debit(id)
        elif option==2:
            credit(id)
        elif option ==3:
            checkbal(id)
        elif option ==4:
            getinfo(id)
        elif option==5:
            updateinfo(id)
    else:
        print(logout())
        time.sleep(4)