from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to store user data
user_data = {
    "user_id": "123",
    "name": "John Doe",
    "email": "john.doe@example.com"
}

@app.route("/")
def index():
    return "Welcome to the Flask app!"

@app.route("/get-user")
def get_user():
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

if __name__ == '__main__':
    app.run(debug=True)
