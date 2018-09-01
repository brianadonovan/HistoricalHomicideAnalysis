from flask import Flask
from Database.database import DatabaseInterface
from Graphing.graphs import Grapher

app = Flask(__name__)
db = DatabaseInterface()
graph = Grapher()

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dbtest')
def db_test():
    return str(db.most_used_weapon_per_year())

@app.route('/graphtest')
def graph_test():
    incidents, years = db.handguns_per_year()
    graph.scatter_plot(years, incidents, "Handgun Incidents")

@app.route('/stacktest')
def stack_test():
    rows = db.most_used_weapon_per_year()
    years = {}
    incidents = {}
    for row in rows:
        weapon_name = row[0]
        year = row[1]
        count = row[2]
        if weapon_name not in years:
            years[weapon_name] = []
        if weapon_name not in incidents:
            incidents[weapon_name] = []
        years[weapon_name].append(year)
        incidents[weapon_name].append(count)
        names = years.keys()

    data = graph.stack_bar(years, incidents, names, "Weapons per Year")
    return str(data)

if __name__ == '__main__':
    app.run()
