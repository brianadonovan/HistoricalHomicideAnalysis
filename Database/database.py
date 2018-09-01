import mysql.connector
from .db_statements import *


class DatabaseInterface:

    def __init__(self):
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    def most_used_weapon_per_year(self):
        self.execute_statement(fetch_weapon_per_year_sql())
        weapons = []
        years = []
        incident_counts = []
        for (weapon, year, incident_count) in self.cursor:
            weapons.append(weapon)
            years.append(year)
            incident_counts.append(incident_count)
        self.connection.commit()
        return list(zip(weapons, years, incident_counts))

    def handguns_per_year(self):
        self.execute_statement(fetch_handgun_incidents_sql())
        years = []
        incident_counts = []
        for (year, incident_count) in self.cursor:
            years.append(year)
            incident_counts.append(incident_count)
        self.connection.commit()
        return incident_counts, years

    def create_connection(self):
        cnx = mysql.connector.connect(user='bre', password='bre',
                                  host='127.0.0.1',
                                  database='HOMICIDE')
        return cnx

    def execute_statement(self, statement):
        print(statement)
        self.cursor.execute(statement)

    def execute_statement_bind(self, statement, md_value):
        print(statement)
        self.cursor.execute(statement, value=md_value)
