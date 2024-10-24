
CREATE TABLE Trainers (
    TrainerID INT AUTO_INCREMENT PRIMARY KEY ,
    TrainerName VARCHAR(50) NOT NULL,
    Age INT
);

INSERT INTO Trainers (TrainerName,Age) values ("Patxi",19);
INSERT INTO Trainers (TrainerName,Age) values ("Paco",12);
INSERT INTO Trainers (TrainerName,Age) values ("Pepe",8);
INSERT INTO Trainers (TrainerName,Age) values ("Goku",99);

CREATE TABLE Pokemons (
    PokemonID INT AUTO_INCREMENT PRIMARY KEY,
    PokemonName VARCHAR(50) NOT NULL,
    TrainerID INT,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE SET NULL
);

INSERT INTO Pokemons (PokemonName,TrainerID) values ("RAICHI",1);
INSERT INTO Pokemons (PokemonName,TrainerID) values ("Jujanchi",1);
INSERT INTO Pokemons (PokemonName,TrainerID) values ("Raticate",2);

CREATE TABLE Badges (
    BadgeID INT AUTO_INCREMENT PRIMARY KEY,
    BadgeName VARCHAR(50) NOT NULL,
    TrainerID INT UNIQUE,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE
);

INSERT INTO Badges (BadgeName,TrainerID) values ("PRIMERO GYM",1);
INSERT INTO Badges (BadgeName,TrainerID) values ("SEGUNDO GYM",2);
INSERT INTO Badges (BadgeName,TrainerID) values ("TERCER GYM",3);


CREATE TABLE Abilities (
    AbilityID INT AUTO_INCREMENT PRIMARY KEY,
    AbilityName VARCHAR(50) NOT NULL
);

INSERT INTO Abilities (AbilityName) values ("dAMP");
INSERT INTO Abilities (AbilityName) values ("FireStrake");
INSERT INTO Abilities (AbilityName) values ("Joga Bonit");


CREATE TABLE PokemonAbilities (
    PokemonID INT,
    AbilityID INT,
    PRIMARY KEY (PokemonID, AbilityID),
    FOREIGN KEY (PokemonID) REFERENCES Pokemons(PokemonID) ON DELETE CASCADE,
    FOREIGN KEY (AbilityID) REFERENCES Abilities(AbilityID) ON DELETE CASCADE
);

INSERT INTO PokemonAbilities (PokemonID,AbilityID) values (1,1);
INSERT INTO PokemonAbilities (PokemonID,AbilityID) values (2,2);
INSERT INTO PokemonAbilities (PokemonID,AbilityID) values (3,3);

CREATE TABLE Battles (
    BattleID INT AUTO_INCREMENT PRIMARY KEY,
    Trainer1ID INT,
    Trainer2ID INT,
    WinnerTrainerID INT,
    BattleDate DATETIME,
    FOREIGN KEY (Trainer1ID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE,
    FOREIGN KEY (Trainer2ID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE,
    FOREIGN KEY (WinnerTrainerID) REFERENCES Trainers(TrainerID) ON DELETE SET NULL
);


INSERT INTO Battles (Trainer1ID,Trainer2ID,WinnerTrainerID,BattleDate) values (1,2,1,NOW());
INSERT INTO Battles (Trainer1ID,Trainer2ID,WinnerTrainerID,BattleDate) values (2,3,2,NOW());
INSERT INTO Battles (Trainer1ID,Trainer2ID,WinnerTrainerID,BattleDate) values (1,3,3,NOW());

CREATE TABLE BattlePokemons (
    BattleID INT,
    PokemonID INT,
    TrainerID INT,
    PRIMARY KEY (BattleID, PokemonID),
    FOREIGN KEY (BattleID) REFERENCES Battles(BattleID) ON DELETE CASCADE,
    FOREIGN KEY (PokemonID) REFERENCES Pokemons(PokemonID) ON DELETE CASCADE,
    FOREIGN KEY (TrainerID) REFERENCES Trainers(TrainerID) ON DELETE CASCADE
);

INSERT INTO BattlePokemons (BattleID,PokemonID,TrainerID) values (1,2,1);
INSERT INTO BattlePokemons (BattleID,PokemonID,TrainerID) values (2,3,2);
INSERT INTO BattlePokemons (BattleID,PokemonID,TrainerID) values (1,3,3);


--Select all trainers.
SELECT * FROM Trainers;
--Find all Pokémon names.
SELECT PokemonName FROM Pokemons;
--Count the number of Pokémon each trainer has.
SELECT t.TrainerName,Count(p.PokemonID) as numPokemons
FROM Trainers AS t
LEFT JOIN Pokemons AS p ON p.TrainerID = t.TrainerID
GROUP BY  t.TrainerID,t.TrainerName;
--List all badges with their corresponding trainer names.
SELECT b.BadgeName, t.TrainerName
FROM Badges AS b
LEFT JOIN Trainers AS t ON b.TrainerID = t.TrainerID;
--Get all abilities.
SELECT * FROM PokemonAbilities;
--Find all battles and their winners.
--Get all Pokémon associated with a specific battle (e.g., BattleID = 1).
--Retrieve all Pokémon of a specific trainer (e.g., TrainerID = 1).
--List all trainers who have at least one badge.
--Count the number of battles each trainer has participated in.


--List all badges and trainers who have them, including trainers without badges (LEFT JOIN).
--Find all trainers and their Pokémon, including trainers without Pokémon (LEFT JOIN).
--Get a list of trainers and their badges, including badges without trainers (RIGHT JOIN).
--Combine trainers who have at least one Pokémon and those who have badges (UNION).
--Get all trainers who have Pokémon or badges (INTERSECT).
--Find all trainers with their Pokémon and abilities using multiple joins.
--Find the trainer with the most Pokémon.
--List all battles that occurred on a specific date (e.g., '2024-01-01').
--Retrieve all Pokémon names along with their abilities.
--Get all trainers who won a battle.


--Scalar Subquery: Find the number of badges for a specific trainer (e.g., TrainerID = 1).
--Multiple-Row Subquery: Retrieve all trainers who have more Pokémon than the average number of Pokémon per trainer.
--Correlated Subquery: List all trainers who have more Pokémon than the trainer with the least number of Pokémon.
--Correlated Subquery: Find all battles where Trainer1 has more Pokémon than Trainer2.
--Multiple-Row Subquery: List all Pokémon that have abilities not held by any Pokémon in a specific battle (e.g., BattleID = 1).
