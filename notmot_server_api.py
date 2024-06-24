from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route('/api/show_planer', methods=['POST'])
def show_planer():
    if "plan_id" not in request.form:
        return jsonify({'error': 'No plan provided'}), 400
    plan_id = request.form["plan_id"]
    #write query

@app.route('/api/show_note', methods=['POST'])
def show_note():
    if "note_id" not in request.form:
        return jsonify({'error': 'No note provided'}), 400
    note_id = request.form["note_id"]
    #write query


@app.route('/api/add_plan', methods=['POST'])
def add_plan():
    if "plan_text" not in request.form:
        return jsonify({'error': 'No plan provided'}), 400
    plan_text = request.form["plan_text"]
    #write query


@app.route('/api/add_note', methods=['POST'])
def add_note():
    if "note_text" not in request.form:
        return jsonify({'error': 'No note provided'}), 400
    note_text = request.form["note_text"]
    #write query


@app.route("/api/switch_status" , methods = ["POST"])
def switch_status():
    if "switch_status" not in request.form:
        return jsonify({'error': 'No note provided'}), 400
    switch_status = request.form["switch_status"]
    #write query

@app.route("/api/check_status" , methods = ["POST"])
def check_status():
    if "check_status" not in request.form:
        return jsonify({'error': 'No status provided'}), 400
    check_status = request.form["check_status"]
    #write query

@app.route("/api/delete_plan" , methods = ["POST"])
def delete_plan():
    if "delete_plan_id" not in request.form:
        return jsonify({'error': 'No status provided'}), 400
    delete_plan_id = request.form["delete_plan_id"]
    #write query

@app.route("/api/delete_note" , methods = ["POST"])
def delete_note():
    if "delete_note_id" not in request.form:
        return jsonify({'error': 'No status provided'}), 400
    delete_note_id = request.form["delete_note_id"]
    #write query

if __name__ == ("__main__") :
    app.run(debug=True)