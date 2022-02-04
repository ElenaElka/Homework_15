import sqlite3

with sqlite3.connect ('animal.db') as con:
    cur = con.cursor()
    query = """
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
            WHERE colors2 NOT NULL
            );
            
        CREATE TABLE animals_colors (
            animal_id INT,
            color_id INT
            );
            
        INSERT INTO animals_colors(
        SELECT animals.animal_id,
               colors.name
        FROM animals
        JOIN colors ON animal.color1=colors.name
        UNION
        SELECT animals.animal_id,
               colors.name
        FROM animals
        JOIN colors ON animal.color2=colors.name
        );
        
        
        CREATE TABLE data_outcomes(
            id INT PRIMARY KEY AUTOINCREMENT,
            outcome_id INT,
            animal_id INT,
            age_upon_outcome INT,
            outcome_subtype VARCHAR (100),
            outcome_type VARCHAR (30),
            outcome_month INT,
            outcome_year INT
            );
                    
        INSERT INTO data_outcomes (animal_id, age_upon_outcome, outcome_subtype, outcome_type, outcome_month, outcome_year)
        SELECT animal_id, age_upon_outcome, outcome_subtype, outcome_type, outcome_month, outcome_year
        FROM animals;
        
       
        CREATE TABLE data_animals_breed (
            id INT PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (20)
            );
            
        INSERT INTO data_animals_breed (name)
        SELECT distinct breed
        FROM animals   
        

        CREATE TABLE data_animals_patient(
           id INT PRIMARY KEY AUTOINCREMENT,
           animal_id VARCHAR (10),
           type_id INT,
           name VARCHAR (30),
           animal_type VARCHAR (30),
           breed_id INT,
           date_of_birth DATE
           );
           
        INSERT INTO data_animals_patient (animal_id, name, animal_type, breed_id, date_of_birth)
        SELECT DISTINCT animal_id, animals.name, animals.animal_types, breed_id, date_of_birthday
        FROM animals
        LEFT JOIN data_animals_breed ON animals.breed=name;
    
    """

    cur.execute(query)