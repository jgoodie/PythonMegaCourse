#!/usr/local/opt/python3/bin/python3

import pandas
from bokeh.charts import Scatter
from bokeh.plotting import figure, output_file, show

df = pandas.DataFrame(columns=["X-Axis","Y-Axis"])
df["X-Axis"]=[1,2,3,4,5]
df["Y-Axis"]=[5,6,4,5,3]
p=Scatter(df,x="X-Axis",y="Y-Axis", title="Temperature Observations", xlabel="Day of Observations", ylabel="Temperature")

output_file("Scatter_charts.html")
show(p)

p=figure(plot_width=500, plot_height=500, title="Earthquakes")
# p.circle([1,2,3,4,5],[3,4,6,1,7],size=12,color="red",alpha=0.5)
# p.triangle([1,2,3,4,5],[3,4,6,1,7],size=12,color="red",alpha=0.5)
# p.circle([1,2,3,4,5],[3,4,6,1,7],size=[8,12,14,16,18],color="red",alpha=0.5)
p.circle([1,2,3,4,5],[3,4,6,1,7],size=[i*2 for i in [8,12,14,16,18]],color="red",alpha=0.5)
show(p)
output_file("Scatter_plotting.html")
