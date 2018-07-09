# Write your SQL queries inside the strings below.  If you choose to write your queries on multiple lines, make sure to wrap your query inside """triple quotes""".  Use "single quotes" if your query fits on one line.

def select_hero_names_and_squad_names_of_heroes_belonging_to_a_team():
    return "SELECT superheroes.name, squads.name FROM superheroes JOIN squads ON superheroes.squad_id = squads.id;"

def reformatted_query():
    return "SELECT superheroes.name, squads.name AS team FROM superheroes JOIN squads ON superheroes.squad_id = squads.id ORDER BY team;"


def all_superheroes():
    return "SELECT superheroes.name, superheroes.superpower, squads.name AS team FROM superheroes LEFT JOIN squads ON superheroes.squad_id = squads.id ORDER BY team;"

def all_squads():
    return "SELECT squads.name, COUNT(superheroes.squad_id) FROM squads LEFT JOIN superheroes ON squads.id = superheroes.squad_id GROUP BY squads.name;"
#squads.name, COUNT(superheroes.squad_id)
