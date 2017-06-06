from flask import *
import pandas

app = Flask(__name__)

@app.route("/tables")
def show_tables():
    data = pandas.read_csv("dummy_data.csv")
    data.set_index(['Name'], inplace=True)
    data.index.name=None
    #females = data.loc[data.Gender=='F']
    #males = data.loc[data.Gender=='M']
    #return render_template('view.html',tables=[females.to_html(classes='female'),males.to_html(classes='male')], titles = ['na', 'Female Surfers', 'Male Surfers'])
    return render_template('view.html',tables=[data.to_html(classes='all_surfers')],titles = ['na', 'All Surfers'])

if __name__ == "__main__":
    app.run(debug=True)