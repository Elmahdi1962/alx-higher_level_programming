-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
USE hbtn_0c_0;
SELECT city, MAX(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
LIMIT 3;
