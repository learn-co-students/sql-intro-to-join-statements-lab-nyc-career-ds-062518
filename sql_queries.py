# Write your SQL queries inside the strings below.  If you choose to write your queries on multiple lines, make sure to wrap your query inside """triple quotes""".  Use "single quotes" if your query fits on one line.

def select_hero_names_and_squad_names_of_heroes_belonging_to_a_team():
    return """SELECT superheroes.name, squads.name FROM superheroes INNER JOIN squads ON squads.id = superheroes.squad_id;"""

def reformatted_query():
    return """SELECT superheroes.name, team.name FROM superheroes INNER JOIN squads AS team ON team.id = superheroes.squad_id ORDER BY team.name;"""

def all_superheroes():
    return """SELECT superheroes.name, superheroes.superpower, team.name FROM superheroes LEFT JOIN squads AS team ON team.id = superheroes.squad_id ORDER BY team.name;"""

def all_squads():
    return """SELECT team.name, COUNT(superheroes.name) FROM squads AS team LEFT JOIN superheroes ON team.id = superheroes.squad_id GROUP BY team.name;"""
