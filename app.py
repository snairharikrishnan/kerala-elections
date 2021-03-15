import io
import pandas as pd
from flask import Flask, request,render_template,send_file
import matplotlib.pyplot as plt

app=Flask(__name__)

data=pd.read_csv("election_kerala")


@app.route('/result',methods=['POST'])
def result():
    const = int(request.form.get("const"))  
    const_data=data.loc[data.Const_no==const]

    fig, ax = plt.subplots(figsize =(10, 5))  
    ax.barh(const_data.Party,const_data.Vote,color=['red', 'blue', 'orange'],edgecolor='black')
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    ax.invert_yaxis()
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5, 
                 str(round((i.get_width()), 2)),
                 fontsize = 10, fontweight ='bold',
                 color ='grey')
    
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')
 
@app.route('/')
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)