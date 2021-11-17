-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(rate) AS rating FROM tv_shows tvs
LEFT JOIN tv_show_ratings tvsr
ON tvs.id = tvsr.show_id
GROUP BY tvs.id
ORDER BY rating DESC;

