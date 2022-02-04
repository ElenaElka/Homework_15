CREATE TABLE data_colors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50)
);

INSERT INTO data_colors (name)
SELECT *
FROM (
SELECT distinct (color1)
FROM animals
UNION
SELECT distinct (color2)
FROM animals
WHERE animals.color2 NOT NULL
);

CREATE TABLE animals_colors (
        animal_id INT,
        color_id INT
);

INSERT INTO animals_colors
SELECT an.animal_id,
       data_colors.name
FROM animals an
JOIN data_colors ON an.color1=data_colors.name
UNION
SELECT an.animal_id,
       data_colors.name
FROM animals an
JOIN data_colors ON an.color2=data_colors.name
;



CREATE TABLE data_outcomes(
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        outcome_id INT,
        animal_id INT,
        age_upon_outcome INT,
        outcome_type VARCHAR (30),
        outcome_month INT,
        outcome_year INT,
        outcome_subtype VARCHAR (100)
);

INSERT INTO data_outcomes (animal_id, age_upon_outcome, outcome_type, outcome_month, outcome_year, outcome_subtype)
SELECT animal_id, age_upon_outcome, outcome_type, outcome_month, outcome_year, outcome_subtype
FROM animals;


CREATE TABLE data_animals_breed (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50)
);

INSERT INTO data_animals_breed (name)
SELECT distinct breed
FROM animals


CREATE TABLE data_animal_result(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id VARCHAR (10),
        animal_type VARCHAR (20),
        name VARCHAR (30),
        date_of_birth DATE,
        breed  VARCHAR (50)
);

INSERT INTO data_animal_result (animal_id, animal_type, name, date_of_birth, breed)
SELECT DISTINCT animal_id, animals.animal_type, animals.name, date_of_birth, breed
FROM animals
LEFT JOIN data_animals_breed ON animals.breed=breed

