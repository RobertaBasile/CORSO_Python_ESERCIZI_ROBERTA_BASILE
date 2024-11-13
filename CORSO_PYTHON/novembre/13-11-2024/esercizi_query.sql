SELECT country.Name AS CountryName, COUNT(city.ID) AS NumberOfCities
FROM city
JOIN country ON city.CountryCode = country.Code
GROUP BY country.Name
ORDER BY NumberOfCities 

SELECT country.Name AS CountryName, country.LifeExpectancy, country.GovernmentForm 
FROM country WHERE country.GovernmentForm = '%Republic%' AND country.LifeExpectancy > 70 
ORDER BY country.LifeExpectancy DESC;

-- Si vuole recuperare dal database le lingue parlate per nazione con la rispettiva percentuale di utilizzo; 
-- create un vista sulla base di questa query

SELECT country.Name AS CountryName, countrylanguage.Language, countrylanguage.Percentage
FROM country
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode;

CREATE VIEW ESEMPIO AS 
SELECT country.Name AS CountryName, countrylanguage.Language, countrylanguage.Percentage 
FROM country JOIN countrylanguage ON country.Code = countrylanguage.CountryCode;