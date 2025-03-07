-- Liste des genres et du nombre de shows associés
-- Tri décroissant par nombre de shows
-- Groupement par genre
-- Groupement par genre

SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;

