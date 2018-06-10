#Trends in Startups
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


