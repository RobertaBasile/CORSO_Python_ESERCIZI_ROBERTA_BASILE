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

CREATE VIEW LinguePerNazione AS
SELECT country.Name AS CountryName, countrylanguage.Language, countrylanguage.Percentage
FROM country
INNER JOIN countrylanguage ON country.Code = countrylanguage.CountryCode;
-- Create una vista chiamata PopulationByContinent 
-- che mostri il nome del continente e 
-- la popolazione totale per ciascun continente.
CREATE VIEW PopulationByContinent AS
SELECT Continent, SUM(Population) AS TotalPopulation
FROM country
GROUP BY Continent

-- Create una vista chiamata CapitalCities che mostri il nome dello stato, 
-- il nome della sua capitale e la lingua ufficiale
CREATE VIEW CapitalCities AS
SELECT country.Name AS CountryName, city.Name AS CapitalName, countrylanguage.Language
FROM country
JOIN city ON country.Capital = city.ID
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE countrylanguage.IsOfficial = 'T';
