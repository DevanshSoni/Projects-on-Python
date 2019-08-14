import json
import time
import os
def getinfo(id):
    os.system('cls')
    fp=open(f'Bank/{id}','r')
    value=json.load(fp)
    print(f"UserName is {value['name']}")
    print(f"Password is {value['Password']}")
    print(f"Account Balance is {value['Balance']}")
    fp.close()
    time.sleep(3)
def updateinfo(id):
    os.system('cls')
    print('1 :- Update Account User_name')
    print('2 :- Update Account Password')
    fp=open(f'Bank/{id}','r+')
    value=json.load(fp)
    choice=int(input('Enter your choice'))
    if choice == 1:
        name=input("Enter New User_Name")
        value['name']=name
        print('Records Updated')
    elif choice ==2:
        password=input("Enter New Password")
        value['Password']=password
        print('Records Updated')
    fp.seek(0)
    json.dump(value,fp)
    fp.truncate()
    fp.close()
    time.sleep(3)