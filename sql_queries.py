# Write your SQL queries inside the strings below.  If you choose to write your queries on multiple lines, make sure to wrap your query inside """triple quotes""".  Use "single quotes" if your query fits on one line.

def select_hero_names_and_squad_names_of_heroes_belonging_to_a_team():
    return """
            SELECT Superheroes.name, Squads.name
            FROM Superheroes
            JOIN Squads
            ON Squads.id = Superheroes.squad_id;
                """

def reformatted_query():
    return """
            SELECT Superheroes.name, Squads.name AS 'team'
            FROM Superheroes
            JOIN Squads
            ON Squads.id = Superheroes.squad_id
            ORDER BY team ASC;
                """

def all_superheroes():
    return """SELECT Superheroes.name, Superheroes.superpower, Squads.name AS 'team'
                FROM Superheroes
                LEFT JOIN Squads
                ON Squads.id = Superheroes.squad_id
                ORDER BY team ASC; """

def all_squads():
    return """SELECT Squads.name AS 'name', COUNT(Superheroes.squad_id)
                AS 'num_of_members'
                FROM Squads
                LEFT JOIN Superheroes
                ON Squads.id = Superheroes.squad_id
                GROUP BY Squads.name
                ORDER BY Squads.name ASC;
                """
