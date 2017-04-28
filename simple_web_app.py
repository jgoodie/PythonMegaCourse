#!/usr/local/bin/python3
import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN
from flask import Flask, render_template

app=Flask(__name__)    
@app.route('/')
def home():
    return render_template("home.html")
    #return "Hello World!"

@app.route('/about/')
def about():
    return render_template("about.html")
    #return "This is the about page!"
    
@app.route('/plot/')
def plot():
    start=datetime.datetime(2017,1,1)
    end=datetime.datetime(2017,4,27)
    df=data.DataReader(name="HTHIY",data_source="yahoo",start=start,end=end)
    def inc_dec(c,o):
        if c>o:
            val="Increase"
        elif o>c:
            val="Decrease"
        else:
            val="Equal"
        return val
    df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
    df["Middle"]=(df.Open+df.Close)/2
    df["Height"]=abs(df.Open-df.Close)
    p=figure(x_axis_type='datetime',width=1000,height=300,responsive=True)
    p.title.text="Hitachi, Ltd. (HTHIY)"
    p.grid.grid_line_alpha=0.3
    hours_12_ms=12*60*60*1000
    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"], hours_12_ms, df.Height[df.Status=="Increase"],
           fill_color="#CCFFFF",line_color="black")
    p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"], hours_12_ms, df.Height[df.Status=="Decrease"],
           fill_color="#FF3333",line_color="black")
    script1,div1 = components(p)
    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files[0]
    return render_template("plot.html", script1=script1, div1=div1, cdn_css=cdn_css, cdn_js=cdn_js)

if __name__=="__main__":
    app.run(debug=True)