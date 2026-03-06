from flask import Flask, request

with open("cars24_t1.pkl", "rb") as f:
    

app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return "Flask app is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

if __name__ == "__main__":
    app.run(debug=True)