CREATE TABLE Partido (
    Id int NOT NULL,
    Fecha DATETIME,
    EquipoLocal nvarchar(255),
    EquipoVisitante varchar(255),
    City nvarchar(255) NOT NULL,
    CONSTRAINT PK_Partido PRIMARY KEY (Id)
);

INSERT INTO Partido (Id,Fecha,EquipoVisitante,EquipoLocal,Campo) 
values (3,'1000-01-01 00:00:00',"Real Madrid","Bernabeu","Logrono");

UPDATE Partido set EquipoVisitante="Real Betis Balonpié" where id=2;  

select Id,Fecha from Partido;

select * from Partido where EquipoVisitante="Valladolid";

CREATE TABLE Equipo (
    Id int NOT NULL,
    Nombre nvarchar(255) NOT NULL,
    NumJugadores int NOT NULL,
    Ciudad nvarchar(255) NOT NULL,
    CONSTRAINT PK_Equipo PRIMARY KEY (Id)
);

INSERT INTO Equipo values(1,"Barcelona", 17,"Logrono");

--Muestrame de los partidos con mas de 3 goles, el número de jugadores
SELECT p.*,e.NumJugadores
FROM Partido AS p
JOIN Equipo AS e ON p.EquipoVisitante = e.Nombre
WHERE p.Goles>3;