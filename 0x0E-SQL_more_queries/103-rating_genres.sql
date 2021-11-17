-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT name, SUM(rate) AS rating FROM tv_genres g
INNER JOIN tv_show_genres tvg
ON tvg.genre_id = g.id
INNER JOIN tv_shows tvs
ON tvs.id = tvg.show_id
INNER JOIN tv_show_ratings tvsr
ON tvsr.show_id = tvs.id
GROUP BY g.name
ORDER BY rating DESC;
