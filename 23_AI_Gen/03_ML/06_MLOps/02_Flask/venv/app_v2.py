from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask APP_V2 is running!"

@app.route("/predict", methods=["POST"])
def prediction():
    data = request.get_json()
    # company = data["make"]
    # model_name = data["model"]
    return data

@app.route("/about", methods=["GET"])
def about_us():
    return "This is about us page..."

if __name__ == "__main__":
    app.run(debug=True)