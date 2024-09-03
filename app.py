from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#1
@app.route("/users", methods = ["GET"])
def users_get():
    return jsonify({
        "payload" : "success"
    })

#2
@app.route("/user", methods = ["POST"])
def user_post():
    return jsonify({
        "payload" : "success"
    })

#3
@app.route("/user", methods = ["DELETE"])
def user_delete():
    return jsonify({
        "payload" : "success" 
    })

#4
@app.route("/user", methods = ["PUT"])
def user_put():
    return jsonify({
    "payload": "success",
    "error": False
    })

#5
@app.route("/api/v1/users", methods = ["GET"])
def get_users_api():
    return jsonify({
        "payload" : []
    })

#6
@app.route("/api/v1/user", methods = ["POST"])
def post_users_api():
    return jsonify({
        "payload": {
            "email": request.args.get("email"),
            "name": request.args.get("name")
        }
    })


#7
@app.route("/api/v1/user/add", methods = ["POST"])
def post_user_add_api():
    return jsonify({
        "payload":{
        "email": request.form.get("email"),
        "name": request.form.get("name"),
        "id": request.form.get("id")
        }
    })

#8
@app.route("/api/v1/user/create", methods = ["POST"])
def users_create_api():
    data = request.get_json()
    return  jsonify({
        "payload": {
            "email": data["email"],
            "name": data["name"],
            "id": data["id"]
        }
    })
if __name__ == "__main__":
    app.run(debug=True)