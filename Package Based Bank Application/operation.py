import json
import time
import os
def credit(id):
    os.system('cls')
    fp=open(f'Bank/{id}','r+')
    value=json.load(fp)
    amt=int(input("Enter Amount to be credited"))
    if amt>0:
        value['Balance']+=amt
    else:
        fp.close()
        print("Please Enter Valid Amount to be Credited")
    fp.seek(0)
    json.dump(value,fp)
    print("Amount Credited Successfully")
    fp.truncate()
    fp.close()
    time.sleep(3)
def debit(id):
    os.system('cls')
    fp=open(f'Bank/{id}','r+')
    value=json.load(fp)
    amt=int(input("Enter Amount to be Debited"))
    if value['Balance']<amt:
        print("Insufficient Balance")
    elif amt<1:
        print("Enter Valid Amount To be debited")
    else:
        value['Balance']-=amt
    fp.seek(0)
    json.dump(value,fp)
    print("Amount Debited Successfully")
    fp.truncate()
    fp.close()
    time.sleep(3)
def checkbal(id):
    os.system('cls')
    fp=open(f'Bank/{id}','r')
    value=json.load(fp)
    print(f"Available Balance in your Account is {value['Balance']}")
    fp.close()
    time.sleep(3)
def logout():
    os.system('cls')
    return "Logging Out See you Again"
