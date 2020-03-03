-- displays the top 3 of cities temp during July and August order by temp (des)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month > 6 AND month < 9
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
