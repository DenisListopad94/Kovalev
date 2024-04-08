import sqlite3

with sqlite3.connect('C:\\Users\\USER\\Desktop\\hw\\db\\second_hw.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM movies WHERE release BETWEEN 2015 AND 2020 ''')
    films_between_2015_2020 = cursor.fetchall()
    cursor.execute('''    SELECT DISTINCT directors.*
FROM directors LEFT JOIN movies
ON movies.director_id  = directors.director_id 
WHERE movies.director_id is NULL''')
    directors_without_films = cursor.fetchall()  
    cursor.execute('''SELECT DISTINCT actors.*
FROM actors LEFT JOIN actors_movies                                     
ON actors.actors_id  = actors_movies.actors_id 
WHERE actors_movies.actors_id is NULL
    ''')
    actors_without_films = cursor.fetchall()
    cursor.execute('''SELECT actors.name, actors.surname
FROM actors
JOIN Bank_accounts
ON Bank_accounts.actors_id = actors.actors_id
ORDER BY Bank_accounts.finance DESC LIMIT 5
    ''')
    most_payed_actors = cursor.fetchall()
    cursor.execute('''SELECT DISTINCT name, surname, director_id
FROM directors 
WHERE director_id in 
(SELECT director_id
FROM movies
GROUP BY director_id
HAVING count(movies.director_id) = 1)
    ''')
    directors_with_one_film = cursor.fetchall()
    cursor.execute('''SELECT DISTINCT name, surname, actors_id
FROM actors 
WHERE actors_id in 
(SELECT actors_id
FROM actors_movies
GROUP BY actors_id
HAVING count(actors_movies.actors_id) = 1)
    ''')
    actors_with_one_film = cursor.fetchall()
print(actors_with_one_film)