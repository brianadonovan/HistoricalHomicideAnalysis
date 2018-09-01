def fetch_weapon_per_year_sql():
    return 'SELECT WEAPON, Year, COUNT(weapon) ' \
           'from HOMICIDE ' \
           "WHERE WEAPON != 'Unknown'" \
           'GROUP BY weapon, year ' \
           'order by COUNT(weapon) desc'


def fetch_handgun_incidents_sql():
    return 'SELECT Year, COUNT(weapon) ' \
           'from HOMICIDE ' \
           "WHERE WEAPON = 'Handgun'" \
           'GROUP BY weapon, year ' \
           'order by Year asc'

