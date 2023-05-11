from flask import Flask,render_template,request
app=Flask(__name__,template_folder="templates")
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

import pickle
model=pickle.load(open("credit_project.pkl","rb"))
standard_scaler=pickle.load(open("standard_scaler.pkl","rb"))

@app.route("/")
def fun():
    return render_template('index.html')
@app.route("/predict",methods=["GET","POST"])
def func1():
    a= [i for i in request.form.values()]
    a= [int(j) if j.isdigit() else float(j) for j in a]
    a=np.array(a).reshape(1,-1)
    res=standard_scaler.fit_transform(a)
    sol=model.predict(res)[0]
    if sol==0:
        return render_template("index.html",value="Bad Transaction")
    elif sol==1:
        return render_template("index.html", value="Good Transaction")
if __name__=="__main__":
    app.run(debug=True)