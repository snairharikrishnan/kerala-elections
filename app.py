import io
import pandas as pd
import seaborn as sns
from flask import Flask, request,render_template,send_file
import matplotlib.pyplot as plt
import math

app=Flask(__name__)

data=pd.read_csv("assembly")
lok_clean=pd.read_csv("lok_sabha")

@app.route('/result',methods=['POST'])
def result():
    const = int(request.form.get("const"))  
    
    ass=data.loc[data.Const_no==const,["Party","Vote"]].reset_index(drop=True)
    par=lok_clean.loc[lok_clean.Const_no==const,["Party","Vote"]].reset_index(drop=True)
    ass["Year"]=2016
    par["Year"]=2019
    vote_share=ass.append(par).reset_index(drop=True)

    fig, ax = plt.subplots(figsize =(15,8))   
    ax=sns.barplot(x="Year", y="Vote", hue="Party", data=vote_share)
    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
     
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
     
    # Add padding between axes and labels
    ax.xaxis.set_tick_params(pad = 20)
    ax.yaxis.set_tick_params(pad = 20)
    plt.title(data.loc[data.Const_no==const,"Const_name"].unique()[0],
              fontsize = 25,fontweight ='bold')
    ax.legend(loc='upper center', frameon=False)
    
    # Add annotation to bars
    for i in ax.patches:
        height=i.get_height()
        if not math.isnan(height):
            ax.annotate(str(int(height)), (i.get_x(),height), xytext=(0, 10), textcoords='offset points',fontsize = 15,fontweight ='bold')
    
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')
 
@app.route('/')
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)