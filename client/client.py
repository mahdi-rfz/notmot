import requests
import configs

url = "http://localhost:4444/notmot/addNote"

data = {"username":"mahdi" , "password":"root" , "data":"my name is mahdi and welcome"}

respone = requests.post(url , data=data)

print(type(respone.status_code))


def addNote(data):
    url = (f"http://{configs.domain}:4243/notmot/addNote")

    data = {"username":configs.username ,
             "password":configs.password , 
                "data":data}
    
    response = requests.post(url , data=data)

    if str(respone.status_code) == "200":
        return ["your Note added" , respone.text]
    else : 
        return "You have problem in add note"
    



def delNote(id):
    url = (f"http://{configs.domain}:4243/notmot/delNote")

    data = {"username":configs.username ,
             "password":configs.password , 
                "id":id}
    
    response = requests.post(url , data=data)

    if str(respone.status_code) == "200":
        return ["your Note deleted" , respone.text]
    else : 
        return "You have problem in del note"
    




def listNote(id):
    url = (f"http://{configs.domain}:4243/notmot/listNote")

    data = {"username":configs.username ,
             "password":configs.password}
    
    response = requests.post(url , data=data)

    if str(respone.status_code) == "200":
        return [respone.text]
    else : 
        return "You have problem in receive notes"