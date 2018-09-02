from flask import Flask
from flask import request
from flask import render_template
from Database.database import DatabaseInterface
from Graphing.graphs import Grapher

app = Flask(__name__)
db = DatabaseInterface()
graph = Grapher()


def insert_value_into(key, value, dictionary):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)


def add_value_into_age_range(age_range, key, value, dictionary):
    if key not in dictionary:
        dictionary[key] = [0, 0, 0, 0, 0]
    dictionary[key][age_range] += value


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def hello_world_post():
    age_range = request.form['age_range']
    relationship = request.form['relationship']
    return age_range

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
    graph_format = {'x_axis': 'Year', 'y_axis': 'Number of Incidents', 'title': 'Homicide Weapons Used by Year'}
    for row in rows:
        weapon_name = row[0]
        year = row[1]
        count = row[2]
        insert_value_into(weapon_name, year, years)
        insert_value_into(weapon_name, count, incidents)
        names = years.keys()

    data = graph.stack_bar(years, incidents, names, graph_format)
    return str(data)


@app.route('/inputtest')
def input_test():
    relationship = request.args.get('relationship')
    perp_age_min = request.args.get('perp_age_min')
    perp_age_max = request.args.get('perp_age_max')
    rows = db.relationship_weapon(relationship, perp_age_min, perp_age_max)
    incidents = {}
    ages = {}
    title = '{0} (Ages {1}-{2}) : Weapons per Victim Ages'.format(relationship, perp_age_min, perp_age_max)
    graph_format = {'x_axis': 'Age Range of Victim (years)',
                    'y_axis': 'Incident Count',
                    'title': title}
    for row in rows:
        weapon = row[0]
        age = row[1]
        count = row[2]
        if age > 1 and age <= 17 not in ages:
            add_value_into_age_range(0, weapon, count, incidents)
        elif age >= 18 and age <= 34 not in ages:
            add_value_into_age_range(1, weapon, count, incidents)
        elif age >= 35 and age <= 50 not in ages:
            add_value_into_age_range(2, weapon, count, incidents)
        elif age >= 51 and age <= 70 not in ages:
            add_value_into_age_range(3, weapon, count, incidents)
        elif age >= 71 and age <= 110 not in ages:
            add_value_into_age_range(4, weapon, count, incidents)
    weapons = incidents.keys()


    for weapon in weapons:
        ages[weapon] = ['1-17', '18-34', '35-50', '51-70', '71-110']
    data = graph.stack_bar(ages, incidents, weapons, graph_format)


@app.route('/pietest')
def pie_test():
    rows = db.status_per_state()
    states = {}
    incidents = {}
    for row in rows:
        solved = row[1]
        state = row[0]
        count = row[2]
        insert_value_into(solved, state, states)
        insert_value_into(solved, count, incidents)
    graph.pie_chart(incidents, states, 'Solved or Unsolved by State')
    return str(states) + "\n\n" + str(incidents)


if __name__ == '__main__':
    app.run()
