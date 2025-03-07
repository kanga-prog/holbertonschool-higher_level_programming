-- Script to list all TV shows that have no genre linked in the database hbtn_0d_tvshows
-- Each record will display tv_shows.title and tv_show_genres.genre_id as NULL for shows without a genre
-- The results will be sorted by tv_shows.title in ascending order

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- Use LEFT JOIN to include all shows, even those without a genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
-- Filter to only get shows without a genre (genre_id is NULL)
WHERE tv_show_genres.genre_id IS NULL
-- Sort by tv_shows.title in ascending order
ORDER BY tv_shows.title ASC;

