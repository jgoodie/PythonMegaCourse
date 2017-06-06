import datetime, time, pandas
from geopy.geocoders import Nominatim
from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global fn
    if request.method=='POST':
        file=request.files["file"]
        #filecontent=file.read()
        nom = Nominatim(scheme='http')
        try:
            df = pandas.read_csv(file)
            if not 'Address' in df.columns:
                return render_template('index.html', text="You need to have an address column labeled 'Address' ")
            df = df.set_index("ID")
            df["Coordinates"]=df["Address"].apply(nom.geocode)
            df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
            df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
            df=df.drop("Coordinates",1)
            currtime = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
            fn="uploaded-" + currtime + "-" + file.filename
            # file.save(secure_filename(fn))
            df.to_csv(fn, sep=',')
    #         with open(fn, "a") as f:
    #             f.write("\nThis was added at " + currtime + "\n")
            #print(df)
            # return render_template("success.html", data=df.to_html(), btn="download.html")
            #print(df.to_html())
            #return render_template("success.html", btn="download.html", tables=[df.to_html(classes='all_coordinates')],titles = ['na', 'Coordinates'])
            return render_template("success.html", btn="download.html", tables=[df.to_html(classes='all_coordinates')],titles = ['na', 'Coordinates'])
        except:
            return render_template('index.html', text="Make sure your file is properly formatted")
        return render_template('index.html', text="You need to have an address column labeled 'Address' ")

@app.route("/download")
def download():
    return send_file(fn, attachment_filename="yourfile.txt", as_attachment=True)


if __name__ == '__main__':
    app.debug=True
    # app.run(port=8000)
    app.run()
