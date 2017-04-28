from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

start=datetime.datetime(2017,1,1)
end=datetime.datetime(2017,4,27)
# data.DataReader?
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

# output_file("CS.html")
# show(p)
script1,div1 = components(p)
cdn_js=CDN.js_files
cdn_css=CDN.css_files
