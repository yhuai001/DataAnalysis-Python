#Ride Share Reviews
SELECT * FROM trips;

SELECT * FROM riders;

SELECT * FROM cars;

SELECT * FROM riders 
CROSS JOIN cars;

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