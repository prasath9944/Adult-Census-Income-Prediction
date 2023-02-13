import json
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
from adult_income.predictor import ModelResolver
from adult_income.utils import convert_categorical_toNumerical
from adult_income.config import TARGET_COLUMN
from adult_income.logger import logging
import os,sys
from adult_income.exception import IncomeException

resolver=ModelResolver()
transformer_file_path=resolver.get_latest_transformer_path()
model_file_path=resolver.get_latest_model_path()
target_encoder_file_path=resolver.get_latest_target_encoder_path()

transformed=pickle.load(open(transformer_file_path,'rb'))
model=pickle.load(open(model_file_path,'rb'))
scalar=pickle.load(open(target_encoder_file_path,'rb'))
temp=False

app=Flask(__name__)


@app.route('/')
def home():
    logging.info(f"Rendering the Home Page")
    return render_template("home.html")


@app.route('/predict',methods=['POST'])
def predict():
    try:
        cat=[]
        col=[]
        for x in request.form.items():
            col.append(x[0])
            if x[1].isdigit()!=True:
                cat.append(x[0])
        data=[]
        for x in request.form.values():
            if x.isdigit():
                data.append(float(x))
            else:
                data.append(x)
                
        df=pd.DataFrame(data)
        df=df.transpose()
        df.columns=col
        logging.info(f"The Form has the Details {df}")
        
        logging.info(f"Converting the Categorical feature to Numerical feature using label encoding")
        df=convert_categorical_toNumerical(df,cat)
        
        logging.info(f"Transforming the numpy array and scaling the array")
        transformed_ls=transformed.transform(df.to_numpy())
        
        predicted_value=model.predict(transformed_ls)
        actual_value=scalar.inverse_transform(predicted_value)
        logging.info(f"Inverse transfroming the predicted values: {predicted_value} actual values: {actual_value}")
        final_input=actual_value[0]
        return render_template("home.html",prediction_text="The Salary of the Employee predicted is {}".format(final_input))
    except Exception as e:
        raise IncomeException(e,sys)


if __name__=="__main__":  
    app.run(debug=True)