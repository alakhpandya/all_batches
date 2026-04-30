from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<h1>Flask app is running in docker!!</h1>"

@app.route("/contact", methods=["GET"])
def contact_us():
    return "<h1>Contact Us Page is under construction...</h1>"


@app.route("/api", methods=["POST"])
def collect_data():
    data = request.json
    first_name = data["fname"]
    last_name = data["lname"]
    return f"Hello Mr. {last_name}! I am glad that you are here. Well {first_name}, I want to draw your attention to the fact that we are still working on this project..."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    make = data["make"]
    model = data["model"]
    # here we will call our ML Model to predict the price of the car that has above features and our ML Model will return the price of that car, say it is 10,00,000
    price = "1000000"
    return price

# app.run()

if __name__ == "__main__":
    # app.run()
    app.run(port=8000, debug=True, host="0.0.0.0")