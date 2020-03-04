-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN
(SELECT DISTINCT tv_shows.id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id = 5)
ORDER BY tv_shows.title;
