# Made By Khackers Comunity
import AminoLab
import samino
from threading import Thread
import os
tn = """
                    _             _____  
    /\             (_)           |  __ \ 
   /  \   _ __ ___  _ _ __   ___ | |__) |
  / /\ \ | '_ ` _ \| | '_ \ / _ \|  ___/ 
 / ____ \| | | | | | | | | | (_) | |     
/_/    \_\_| |_| |_|_|_| |_|\___/|_|                             
"""
sl = """
0: Exit                          1: Get ComId & ChatId
2: Normal Messages Spam          3: Unseen Messages Spam
4: Spam Leave And Join Chat      5: Accounts join chat
6: Accounts Leave Chat           7: Accounts join Comunity
8: Accounts Leaves Comunity      9: Get ComId & UserId
10: Accounts Follow User         11: Accounts Unfollow User
12: Accounts Send Normal Message 13: Accounts Send Unseen Message       
"""
def get_comid_k():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    url = input('Enter Chat Link: ')
    comid = client.get_from_link(url).ndc_Id
    ndc = client.get_from_link(url).object_Id
    print(f"\nThe comId: {comid}\nThe Id: {ndc}\n")
    while True:
        lv = input("Do You Want To Go Back(Y/N)?: ")
        if lv=="Y" or lv=="y":
            tool()
            break
        elif lv=="N" or lv=="n":
            os.system("exit")
            break
        else:
            print(f"Worng Char: {lv}")
def U_message_spam():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")
    client.auth(email=email,password=password)
    url = input('Enter Chat Link: ')
    comid = client.get_from_link(url).ndc_Id
    chatid = client.get_from_link(url).object_Id
    msg = input("Type Message: ")
    while True:
        Thread(target=client.send_message(comid,chatid,msg,109)).start()
def N_message_spam():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")
    client.auth(email=email,password=password)
    url = input('Enter Chat Link: ')
    comid = client.get_from_link(url).ndc_Id
    chatid = client.get_from_link(url).object_Id
    msg = input("Type Message: ")
    while True:
        Thread(target=client.send_message(comid,chatid,msg,0)).start()
def leave_and_join_spam():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")
    client.auth(email=email,password=password)
    url = input('Enter Chat Link: ')
    comid = client.get_from_link(url).ndc_Id
    chatid = client.get_from_link(url).object_Id
    while True:
        Thread(target=client.join_thread(comid,chatid)).start()
        Thread(target=client.leave_thread(comid,chatid)).start()
def accounts_join_chat():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    chat = input('chat link: ')
    comid = client.get_from_link(chat).ndc_Id
    chatid = client.get_from_link(chat).object_Id
    password = input('password: ')
    for email in open('emails.txt').read().split():
        print(email)
        Thread(target=client.auth(email=email,password=password)).start()
        Thread(target=client.join_thread(comid,chatid)).start()
def accounts_leave_chat():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    chat = input('chat link: ')
    comid = client.get_from_link(chat).ndc_Id
    chatid = client.get_from_link(chat).object_Id
    password = input('password: ')
    for email in open('emails.txt').read().split():
        print(email)
        Thread(target=client.auth(email=email,password=password)).start()
        Thread(target=client.leave_thread(comid,chatid)).start()
def accounts_join_com():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    comid = input("Enter comId: ")
    password = input('password: ')
    for email in open('emails.txt').read().split():
        print(email)
        Thread(target=client.auth(email=email,password=password)).start()
        Thread(target=client.join_community(comid)).start()
def accounts_leave_com():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    comid = input("Enter comId: ")
    password = input('password: ')
    for email in open('emails.txt').read().split():
        print(email)
        Thread(target=client.auth(email=email,password=password)).start()
        Thread(target=client.leave_community(comid)).start()
def accounts_follow_user():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    uuuu = input("Enter User Link: ")
    comid = client.get_from_link(uuuu).ndc_Id
    userid = client.get_from_link(uuuu).object_Id
    password = input('password: ')
    for email in open('emails.txt').read().split():
        print(email)
        Thread(target=client.auth(email=email,password=password)).start()
        Thread(target=client.follow_user(comid,userid)).start()
def accounts_unfollow_user():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    uuuu = input("Enter User Link: ")
    comid = client.get_from_link(uuuu).ndc_Id
    userid = client.get_from_link(uuuu).object_Id
    password = input('password: ')
    for email in open('emails.txt').read().split():
        print(email)
        Thread(target=client.auth(email=email,password=password)).start()
        Thread(target=client.unfollow_user(comid,userid)).start()
def get_userid():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    url = input('Enter User Link: ')
    comid = client.get_from_link(url).ndc_Id
    userId = client.get_from_link(url).object_Id
    print(f"\nThe comId: {comid}\nThe Id: {userId}\n")
    while True:
        lv = input("Do You Want To Go Back(Y/N)?: ")
        if lv=="Y" or lv=="y":
            tool()
            break
        elif lv=="N" or lv=="n":
            os.system("exit")
            break
        else:
            print(f"Worng Char: {lv}")
def Accounts_send_message():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    password = input("Enter Password: ")
    chat = input("Enter Chat Link: ")
    comid = client.get_from_link(chat).ndc_Id
    chatid = client.get_from_link(chat).object_Id
    msg = input("Type Message: ")
    for email in open('emails.txt').read().split():
        Thread(target=client.auth(email=email,password=password))
        Thread(target=client.send_message(comid,chatid,msg,0))
def Accounts_send_nmessage():
    os.system("clear")
    print(tn)
    client = AminoLab.Client()
    password = input("Enter Password: ")
    chat = input("Enter Chat Link: ")
    comid = client.get_from_link(chat).ndc_Id
    chatid = client.get_from_link(chat).object_Id
    msg = input("Type Message: ")
    for email in open('emails.txt').read().split():
        Thread(target=client.auth(email=email,password=password))
        Thread(target=client.send_message(comid,chatid,msg,109))
def tool():
    os.system("clear")
    print(tn)
    print(sl)
    while True:
        choose = int(input("Type Number: "))
        if choose==0:
            os.system("exit")
        elif choose==1:
            get_comid_k()
            break
        elif choose==2:
            N_message_spam()
            break
        elif choose==3:
            U_message_spam()
            break
        elif choose==4:
            leave_and_join_spam()
            break
        elif choose==5:
            accounts_join_chat()
            break
        elif choose==6:
            accounts_leave_chat()
            break
        elif choose==7:
            accounts_join_com()
            break
        elif choose==8:
            accounts_leave_com()
            break
        elif choose==9:
            get_userid()
            break
        elif choose==10:
            accounts_follow_user()
            break
        elif choose==11:
            accounts_unfollow_user()
            break
        elif choose==12:
            Accounts_send_message()
            break
        elif choose==13:
            Accounts_send_nmessage()
            break
        else:
            print("Worng Number: "+choose)
tool()
