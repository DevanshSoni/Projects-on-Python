import os
import json
import time
def sign_up():
    os.system('cls')
    user_name=input("Enter User_Name")
    password=input("Enter Password")
    balance=int(input("Enter Initial Amount"))
    acc_no=None
    data=os.listdir('Bank')
    if data==[]:
        acc_no='1000'                              # Assign 1000 if there is no records in the history
    else:      
        acc_no=str(int(max(data))+1)               # otherwise increment to the next account Number
    data={'name':user_name,'Balance':balance,'Password':password}
    fp=open(f'Bank/{acc_no}','w')               
    json.dump(data,fp)                  
    print("User Successfully Added")
    print(f"Your Account Number {acc_no} and Password {password}, needed at the time of login")
    fp.close()
    time.sleep(2)
    return True                                      #Will return True after Successful Signing Up 
def login(id,password):
    data=os.listdir('Bank')
    if id in data:
        fp=open(f'Bank/{id}','r+')
        value=json.load(fp)
        if value['Password']==password:
            fp.close()
            return True                            #Return True if right password entered by the user
        else:
            fp.close()
            print("You've entered wrong password please try again!!!")
            return False                           #Return False if password is wrong
    else:
        print("No Such Record Exist Prefer Doing sign up")
        return False                               # Return False if user does not exists 