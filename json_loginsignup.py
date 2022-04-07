#################################################################################################################################
            #    >>>>>>>>>>>>>>>>>>>>>>>>>> json with crud  <<<<<<<<<<<<<<<<<<<<<<<<<<<#

import json
import os
day=[]
print("1).signup 2).login")
def signup():
    if  not os.path.exists('pra.json'):

        with open("pra.json",'w') as p:
            json.dump(day,p)

    with open("pra.json",'r') as p:
        d=json.load(p)
        userData = {"name": input("Enter your name: "), "email": input('Enter your email ID: '), "password": input('Enter your password: ')}
        d.append(userData)
        
    with open('pra.json','w') as p4:
        json.dump(d,p4,indent=4)
    print("Sucessfully your signup is done!")



def login():
    with open("pra.json",'r') as p1:
        tast = json.load(p1)
        email = input('Enter your email: ')
        password2=input('Enter your password: ')
        log=0
        for i in tast:
            if (i["email"]==email) and (i["password"]==password2):
                log+=1
        if log==0:
            print('Either of the user detail is wrong, pleaase check it once!!')
        else:
            print('done')



n=int(input("enter the choice: "))
if n==1:
    signup()
elif n==2:
    login()
