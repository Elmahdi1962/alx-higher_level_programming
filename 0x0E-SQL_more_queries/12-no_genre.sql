-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tvs.title, tvg.genre_id FROM tv_shows tvs
LEFT JOIN tv_show_genres tvg
ON tvg.show_id = tvs.id
WHERE tvg.genre_id IS NULL
ORDER BY tvs.title, tvg.genre_id ASC;
