-- Script to list all TV shows that have no genre linked in the database hbtn_0d_tvshows
-- Each record will display tv_shows.title and tv_show_genres.genre_id as NULL for shows without a genre
-- The results will be sorted by tv_shows.title in ascending order

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;

