import requests
import configs
import socket
import os

def addNote(data):
    url = (f"http://{configs.domain}:{configs.port}/notmot/addNote")

    data = {"username":configs.username ,
             "password":configs.password , 
                "data":data}
    
    response = requests.post(url , data=data)

    if response.ok == True:
        return ["your Note added" , response.text]
    else : 
        return f"You have problem in add note , {response.status_code}"
    



def delNote(id):
    url = (f"http://{configs.domain}:{configs.port}/notmot/delNote")

    data = {"username":configs.username ,
             "password":configs.password , 
                "id":id}
    
    response = requests.post(url , data=data)

    if response.ok == True:
        return ["your Note deleted" , response.text]
    else : 
        return f"You have problem in add note , {response.status_code}"
    




def listNote():
    url = (f"http://{configs.domain}:{configs.port}/notmot/listNote")

    data = {"username":configs.username ,
             "password":configs.password}
    
    response = requests.post(url , data=data)

    if response.ok == True:
        return [response.text]
    else : 
        return f"You have problem in add note , {response.status_code}"
    



def textArt():
    return """ █▄ █ ▄▀▄ ▀█▀ █▄ ▄█ ▄▀▄ ▀█▀
 █ ▀█ ▀▄▀  █  █ ▀ █ ▀▄▀  █ 
"""


def check_internet_connection():
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False
        





def main():
    print("[1] - Add note")
    print("[2] - Del note")
    print("[3] - Show nots")
    print("[4] - EXIT")
    print()

    choose = input(">>>")

    if choose == "1" or choose == "add":
        note = input("Enter your note >>>")
        receive = addNote(note)
        print()
        print(f"{list(receive)[0]} with id : {eval(list(receive)[1])["id"]}")

        print()
        main()
    elif choose == "2" or choose == "del":
        note = input("Enter note id >>>")
        receive = delNote(note)
        print()
        print(f"{list(receive)[0]} with id : {eval(list(receive)[1])["id"]}")

        print()
        main()
    elif choose == "3" or choose == "show":
        receive = listNote()

        for note in eval((list(receive))[0]):
            print(f"ID : {note["id"]} , Note : {note["note"]}")

        print()
        main()
    elif choose == "clear" :
        os.system("clear")
        print(textArt())
        main()
            


if check_internet_connection() == True:
    os.system("clear")
    print(textArt())
    main()
else : 
    os.system("clear")
    print(textArt())
    print("You have problem in your internet connection")