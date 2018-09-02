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


def fetch_status_per_state_sql():
    return 'SELECT STATE, CRIME_SOLVED, COUNT(STATE) from HOMICIDE GROUP BY STATE, CRIME_SOLVED'


def fetch_relationship_age_sql(relationship, perp_age_min, perp_age_max):
    return 'SELECT WEAPON, VICTIM_AGE, COUNT(WEAPON) ' \
           'FROM HOMICIDE ' \
           "WHERE RELATIONSHIP = '{0}' AND " \
           'PERPETRATOR_AGE >= {1} AND ' \
           'PERPETRATOR_AGE <= {2} ' \
           'GROUP BY WEAPON, VICTIM_AGE '.format(relationship, perp_age_min, perp_age_max)

