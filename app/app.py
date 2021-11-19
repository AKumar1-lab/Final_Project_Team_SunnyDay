from flask import Flask, render_template, request
from ML_model import predict_ghi

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        zipcode = int(request.form["zipcode"])
        monthly_bill = float(request.form["mon_elec_bill"])
  
        prediction = predict_ghi(zipcode,monthly_bill)
        ghi = f"{round(prediction[0][0],2)} sun hours/day"
        r2_score = round(prediction[2],3)
        
        lat=prediction[1][0][0]
        lng=prediction[1][0][1]
        county=f"{prediction[5][0][0]}, {prediction[5][0][1]}"

        yearly_bill = prediction[4]
        daily_elec_use = prediction[3][0][0]/365
        ac_capacity = daily_elec_use/prediction[0][0]
        dc_capacity = ac_capacity*1.24
        num_panels = int((dc_capacity*1000)/300)+1
        sys_cost_est = num_panels*300*2.68*.74
        payback_period_years = f"{round(sys_cost_est/yearly_bill,2)} years"

        return render_template("results.html", results=ghi, coords=[lng,lat], r2=r2_score, zip=zipcode, payback=payback_period_years, county=county, sys_cost=round(sys_cost_est,2))