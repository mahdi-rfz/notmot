from flask import Flask

app = Flask(__name__)

@app.route("/api/show_planer" , methods = ["POST"])
def show_planer():
    pass

@app.route("/api/show_note" , methods = ["POST"])
def show_note():
    pass

@app.route("/api/add_plan" , methods = ["POST"])
def add_plan():
    pass

@app.route("/api/add_note" , methods = ["POST"])
def add_note():
    pass

@app.route("/api/switch_status" , methods = ["POST"])
def switch_status():
    pass

@app.route("/api/check_status" , methods = ["POST"])
def check_status():
    pass

@app.route("/api/delete_plan" , methods = ["POST"])
def delete_plan():
    pass

@app.route("/api/delete_note" , methods = ["POST"])
def delete_note():
    pass

if __name__ == ("__main__") :
    app.run()