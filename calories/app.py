from flask import Flask,request
from flask import render_template
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
model=pickle.load(open("calories.pkl","rb"))
app=Flask(__name__)

@app.route("/")
def task_1():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    a=[float(i) for i in request.form.values()]
    a=np.array([a])
    sol=model.predict(a)[0]
    return render_template("index.html",value=sol)


if __name__=="__main__":
    app.run(debug=True)