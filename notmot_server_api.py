from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route('/api/show_planer', methods=['POST'])
def show_planer():
    if "plan_id" not in request.form:
        return jsonify({"Eror": "Your request format is incorrect(use plan_id in request)"}), 400
    plan_id = request.form["plan_id"]
    return plan_id

@app.route('/api/show_note', methods=['POST'])
def show_note():
    if "note_id" not in request.form:
        return jsonify({"Eror": "Your request format is incorrect(use note_id in request)"}), 400
    note_id = request.form["note_id"]
    return note_id


@app.route('/api/add_plan', methods=['POST'])
def add_plan():
    if "plan_text" not in request.form:
        return jsonify({"Eror": "Your request format is incorrect(use plan_text in request)"}), 400
    plan_text = request.form["plan_text"]
    return plan_text


@app.route('/api/add_note', methods=['POST'])
def add_note():
    if "note_text" not in request.form:
        return jsonify({"Eror": "Your request format is incorrect(use note_text in request)"}), 400
    note_text = request.form["note_text"]
    return note_text


@app.route("/api/switch_status" , methods = ["POST"])
def switch_status():
    if "switch_status" not in request.form:
        return jsonify({"Eror": "Your request format is incorrect(use switch_status in request)"}), 400
    switch_status = request.form["switch_status"]
    return switch_status


@app.route("/api/check_status" , methods = ["POST"])
def check_status():
    if "check_status" not in request.form:
        return jsonify({"Eror": "Your request format is incorrect(use check_status in request)"}), 400
    check_status = request.form["check_status"]
    return check_status


@app.route("/api/delete_plan" , methods = ["POST"])
def delete_plan():
    if "delete_plan_id" not in request.form:
        return jsonify({"Eror": "Your request format is incorrect(use delete_plan_id in request)"}), 400
    delete_plan_id = request.form["delete_plan_id"]
    return delete_plan_id


@app.route("/api/delete_note" , methods = ["POST"])
def delete_note():
    if "delete_note_id" not in request.form:
        return jsonify({"Eror": "Your request format is incorrect(use delete_note in request)"}), 400
    delete_note_id = request.form["delete_note_id"]
    return delete_note_id


@app.route("/api/email_reminder", methods=["POST"])
def email_reminder():
    # Check if 'email' and 'note' are in the form data
    if 'email' not in request.form or 'note' not in request.form:
        return jsonify({"Error": "Your request format is incorrect (use 'email' and 'note' in request)"}), 400

    email = request.form["email"]
    note = request.form["note"]

    return jsonify({"email": email, "note": note}), 200

if __name__ == ("__main__") :
    app.run(debug=True)