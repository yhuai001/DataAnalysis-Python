SELECT *
FROM startups;

SELECT COUNT(name)
FROM startups;

SELECT SUM(valuation)
FROM startups;

SELECT MAX(raised)
FROM startups;

SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

SELECT MIN(founded)
FROM startups;

SELECT AVG(valuation)
FROM startups;

SELECT category, AVG(valuation)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation),2)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation),2)
FROM startups
GROUP BY 1
ORDER BY 2;

SELECT  category, COUNT(name)
FROM startups
GROUP BY 1
HAVING COUNT(name) > 3;

SELECT location, AVG(employees)
FROM startups
GROUP BY 1
HAVING AVG(employees) > 500;

------------------------------------------------------------------------
SELECT * FROM trips;

SELECT * FROM riders;

SELECT * FROM cars;

SELECT * FROM riders 
CROSS JOIN cars;
------------------------------------------------------------------------
SELECT trips.date, 
   trips.pickup, 
   trips.dropoff, 
   trips.type, 
   trips.cost,
   riders.first, 
   riders.last,
   riders.username
FROM trips
LEFT JOIN riders 
  ON trips.rider_id = riders.id;


SELECT trips.id, 
	 trips.date, 
   trips.pickup, 
   trips.dropoff, 
   trips.type, 
   trips.cost,
   cars.model,
   cars.OS,
   cars.status
FROM trips
JOIN cars 
	ON trips.car_id = cars.id;
  

SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

SELECT AVG(cost)
FROM trips;

SELECT *
FROM riders
WHERE total_trips < 500;

SELECT COUNT(*)
FROM cars
WHERE status = 'active';

SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;