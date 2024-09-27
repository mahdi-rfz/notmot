from flask import Flask , request , jsonify 
import configs

app = Flask(__name__)

@app.route("/notmot/addNote" , methods = ["GET" , "POST"])
def addNote():
    if request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")
        
        data = request.form.get("data")
        userIp = request.remote_addr

        if username in configs.users and password == configs.users[username] :
            return f"hello , {data}"
        else : 
            return "your username or password is incorrect"
    else :
        return "your request method is bad"
    


        
@app.route("/notmot/delNote" , methods = ["GET" , "POST"])
def delNote():
    if request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")

        id = request.form.get("id")
        userIp = request.remote_addr

        if username in configs.users and password == configs.users[username] :
            return "hello"
        else : 
            return "your username or password is incorrect"
    else :
        return "your request method is bad"
    



@app.route("/notmot/listNote" , methods = ["GET" , "POST"])
def listNote():
    if request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")
        
        ip = request.remote_addr

        if username in configs.users and password == configs.users[username] :
            return "hello"
        else : 
            return "your username or password is incorrect"
    else :
        return "your request method is bad"


if (__name__) == ("__main__"):
    app.run(debug=True , host="localhost" , port=4444)
