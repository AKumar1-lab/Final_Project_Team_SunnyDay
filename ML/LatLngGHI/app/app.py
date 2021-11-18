from flask import Flask, render_template, request
from ML_model import predict_ghi

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])
  
        prediction = predict_ghi(latitude,longitude)

        print(prediction)
        return render_template("results.html", results=prediction)