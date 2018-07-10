
def select_hero_names_and_squad_names_of_heroes_belonging_to_a_team():
    return """SELECT superheroes.name, squads.name FROM superheroes
    JOIN squads ON squads.id = superheroes.squad_id"""

def reformatted_query():
    return """SELECT superheroes.name, squads.name AS team FROM superheroes
    JOIN squads ON squads.id = superheroes.squad_id ORDER by team"""

def all_superheroes():
    return """SELECT superheroes.name, superheroes.superpower, squads.name AS team FROM superheroes
    LEFT OUTER JOIN squads ON squads.id = superheroes.squad_id ORDER by team"""

def all_squads():
    return """SELECT squads.name, count(superheroes.name) AS num_of_members FROM squads
    LEFT OUTER JOIN superheroes ON squads.id = superheroes.squad_id GROUP BY squads.name ORDER by squads.name"""
