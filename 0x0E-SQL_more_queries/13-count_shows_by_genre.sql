-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre, COUNT(tvg.genre_id) AS number_of_shows
FROM tv_genres g
INNER JOIN tv_show_genres tvg
ON tvg.genre_id = g.id
GROUP BY tvg.genre_id
ORDER BY number_of_shows DESC;
