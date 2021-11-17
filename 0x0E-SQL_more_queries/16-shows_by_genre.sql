-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tvs.title, g.name FROM tv_shows tvs
INNER JOIN tv_show_genres tvg
ON tvg.show_id = tvs.id
INNER JOIN tv_genres g
ON g.id = tvg.genre_id
WHERE tvg.genre_id IS NOT NULL
ORDER BY tvs.title, g.name ASC;
