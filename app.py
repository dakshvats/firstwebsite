from operator import index
from flask import Flask, render_template, redirect, request, url_for, send_file
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import seaborn as sns
fig,ax = plt.subplots(figsize =(6,6))
ax= sns.set_style(style="darkgrid")
x_1  = [1, 2, 3, 4, 5]
y_1 = [1, 5, 4, 7, 4]


app=Flask(__name__)

@app.route('/')
def index():
    app.route('/')
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/visualize')
def visualiz():    
    return render_template("viz.html")

@app.route('/thanks')
def thanks():    
    return render_template("thanks.html")
 
 
    


if __name__=="__main__":
    app.run(debug=True)                        
