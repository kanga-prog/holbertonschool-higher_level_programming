-- Script to list all TV shows and their associated genre IDs from the database hbtn_0d_tvshows
-- The result includes shows without genres, displaying NULL for the genre_id if no genre is linked
-- The results are sorted by TV show title (ascending) and genre_id (ascending)

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

