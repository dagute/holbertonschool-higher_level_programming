-- displays the average temperature (Fahrenheit) by city order by temper (desc)
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
