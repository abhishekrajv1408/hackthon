from flask import Flask,request,jsonify
from  modle import predict1
import pandas as pd

app=Flask(__name__)



@app.route("/",methods=['POST'])
def bike():
    quantity=request.form.get('quantity')
    volume=request.form.get('volume')
    distance=request.form.get('distance')
    d={'Quantity':[quantity],
       'Volume (m^3)':[volume],
        'Distance from India (m)':[distance]  
    }
    data=pd.DataFrame(d)
    result= predict1(data)
    result=result.tolist()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
