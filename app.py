from flask import Flask , request , url_for

app = Flask(__name__)





@app.route("/notmot/add_note" , methods = ["GET" , "POST"])
def addNote():
    pass




@app.route("/notmot/del_note" , methods = ["GET" , "POST"])
def delNote():
    pass



@app.route("/notmot/cli_nots" , methods = ["GET" , "POST"])
def cliNots():
    pass



@app.route("/notmot/nots" , methods = ["GET" , "POST"])
def nots():
    pass


if (__name__) == ("__main__"):
    app.run()