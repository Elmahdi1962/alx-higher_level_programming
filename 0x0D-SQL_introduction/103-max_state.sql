-- Write a script that displays the max temperature of each state (ordered by State name).
USE hbtn_0c_0
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
