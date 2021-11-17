-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tvs.title FROM tv_shows tvs
INNER JOIN tv_show_genres tvg
ON tvs.id = tvg.show_id
INNER JOIN tv_genres g
ON g.id = tvg.genre_id
WHERE g.name = "Comedy"
ORDER BY tvs.title ASC;
