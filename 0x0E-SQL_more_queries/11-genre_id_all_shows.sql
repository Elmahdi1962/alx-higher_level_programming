--  that lists all shows contained in the database hbtn_0d_tvshows
SELECT tvs.title, tvg.genre_id FROM tv_shows tvs
LEFT JOIN tv_show_genres tvg
ON tvg.show_id = tvs.id OR tvg.show_id = NULL
ORDER BY tvs.title, tvg.genre_id ASC;
