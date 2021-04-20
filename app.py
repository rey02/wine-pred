from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import pickle
import numpy as np
import argparse
from pywebio import start_server

app = Flask(__name__)

model = pickle.load(open('Wine Quality Prediction.pkl','rb'))



def predict():
    
    fixed_acidity= input("Enter the fixed acidity", type=FLOAT)
    volatile_acidity= input("Enter the volatile acidity content", type=FLOAT)
    citric_acid= input("Enter the citric acid content", type=FLOAT)
    residual_sugar=input("Enter the sugar content", type=FLOAT)
    chlorides= input("Enter the chloride content", type=FLOAT)
    free_sulfur_dioxide= input("Enter the free sulpher di-oxide content", type=FLOAT)
    total_sulfur_dioxide= input("Enter the total sulpher di-oxide content", type=FLOAT)
    density= input("Enter the Density (Mass per unit volume", type=FLOAT)
    pH_content=input("Enter the pH content", type=FLOAT)
    sulphates= input("Enter the sulphate content", type=FLOAT)
    alcohol= input("Enter the alcohol content", type=FLOAT)
    

    prediction = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH_content, sulphates, alcohol]])
    output = round(prediction[0], 2)
    
    put_markdown('# **Prediction**')
    
    if (output==2):
        put_text('The Quality of the wine is good')
        
    elif (output==1):
        put_text('The Quality of the wine fair')
        
    else:
        put_text('The Quality of the wine is poor')
        
    

"""  if output < 0:
        put_text("Sorry You can't sell this Car")

    else:
        put_text('You can sell this Car at price:',output)"""

app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    
    parser= argparse.ArgumentParser()
    parser.add_argument("-p","--port", type=int, default=8080)
    args=parser.parse_args()
    
    start_server(predict, port=args.port)
    
   # app.run(host='localhost', debug=True, port=80)

    #predict()


#visit http://localhost/tool to open the PyWebIO application.