-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT title FROM tv_shows tvs
WHERE title NOT IN(
	SELECT title FROM tv_shows tvs
	INNER JOIN tv_show_genres tvg
	ON tvs.id = tvg.show_id
	INNER JOIN tv_genres g
	ON g.id = tvg.genre_id
	WHERE g.name = "Comedy"
)
ORDER BY title ASC;
