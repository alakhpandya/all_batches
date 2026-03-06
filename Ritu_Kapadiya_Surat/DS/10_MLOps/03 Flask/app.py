from flask import Flask, request

# print(__name__)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask app is running!"

@app.route("/contact", methods=["POST"])
def contact_us():
    data = request.json
    return f"""Hi {data["fname"]}!
    Thanks for updating your mobile number. Your new number is: {data["mobile"]}.
    Our executive from {data["city"]} will contact you soon.
"""

if __name__ == "__main__":
    app.run(debug=True)