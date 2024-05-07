from flask import Flask,request
import pandas as pd
import numpy as np
import joblib
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)
pickle_in = open('/Users/deepbhattacharjee/Documents/Bank_note_Aunthentication_RandomForest_Docker/BankNote_Authentication_using_RandomForest.pkl','rb')

model=joblib.load(pickle_in)


@app.route('/predict')


def predic_note_authentication():

    """Lets Authenticate the Bank Note
    This is using docstrings for specifications.
    ---
    parameter:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
    """
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')

    prediction=model.predict([[variance,skewness,curtosis,entropy]])
    return "Hello The answer is"+ str(prediction)

@app.route('/predict_file',methods=['POST'])


def predic_note_authentication_file():
    """Lets Authenticate the Bank Note
    This is using docstrings for specifications.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    
    responses:
        200:
            description: The output values
    """
    df_test=pd.read_csv(request.files.get("file"))

    prediction=model.predict(df_test)

    return "The predicted value is"+ str(list(prediction))

if __name__=='__main__':
    app.run()

