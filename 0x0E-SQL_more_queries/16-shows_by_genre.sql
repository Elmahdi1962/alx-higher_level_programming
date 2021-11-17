-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tvs.title, g.name FROM tv_shows tvs
LEFT JOIN tv_show_genres tvg
ON tvg.show_id = tvs.id
LEFT JOIN tv_genres g
ON g.id = tvg.genre_id
ORDER BY tvs.title, g.name ASC;
