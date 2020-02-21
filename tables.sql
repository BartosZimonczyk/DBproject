CREATE TABLE genres(
	name VARCHAR(100) PRIMARY KEY
);

/* 
Tabela enumeracyjna w której znajdują się wszystkie możliwe gatunki gier dostępnych w tej bazie danych.
name: nazwa gatunku
*/


CREATE TABLE currencies (
	name TEXT PRIMARY KEY,
	value_in_PLN DECIMAL(10,4) NOT NULL
);

/*
Tabela enumeracyjna w którą są wszystkie możliwe waluty obsługiwane w tej bazie danych wraz z informacją o ich kursie.
name: nazwa waluty
value_in_PLN: wartość kursu
*/

CREATE TABLE platforms (
	plat_id SERIAL PRIMARY KEY,
	name TEXT UNIQUE
);

/*
Tabela ze wszystkimi platformami obsługiwanymi przez bazę wraz z liczbą osób korzystających z tej platformy.
id_plat: id
name: nazwa platformy
population: liczba osób korzystających z platformy
*/


CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(20) NOT NULL UNIQUE,9
	psswd VARCHAR NOT NULL,
	date_of_birth DATE NOT NULL,
	email VARCHAR(50) NOT NULL UNIQUE,
	currency VARCHAR(5) DEFAULT('PLN') REFERENCES currencies(name) ON DELETE RESTRICT ON UPDATE CASCADE,
	amount DECIMAL(10,2) NOT NULL,
	account_creation DATE NOT NULL
	CHECK (account_creation > date_of_birth)
);

/* Tabela z użytkownikami, zawira informacje na temat nicku, hasła, daty urodzenia, emaila, ilości pieniędzy i waluty której uzywa, a także daty stworzenia konta*/


CREATE TABLE friends (
	user_1 INT REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	user_2 INT REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	since DATE NOT NULL
);

/* Tabela ze znajomościami między użytkownikami oraz datą ich zawarcia */

CREATE TABLE games(
	game_id SERIAL PRIMARY KEY,
	name VARCHAR(200) NOT NULL,
	genre VARCHAR(100) REFERENCES genres(name) ON DELETE RESTRICT ON UPDATE CASCADE,
	for_kids BOOLEAN NOT NULL DEFAULT(true),
	author VARCHAR(100),
	description VARCHAR(1000)
);

/* Tabela zawierająca wszystkie gry, czyli ich nazwę, gatunek, to czy jest +18, kto jest autorem oraz ile osób ją posiada */

CREATE TABLE games_platforms(
	gp_id SERIAL PRIMARY KEY,
	game_id INT REFERENCES games(game_id) ON DELETE CASCADE ON UPDATE CASCADE,
	plat_id INT REFERENCES platforms(plat_id) ON DELETE CASCADE ON UPDATE CASCADE,
	price DECIMAL(10,2),
	release_date DATE,
);

/* Tabela zawierająca informacje o tym jakie gry znajdują się na jakiej platformie, czyli jej nazwę, ile osób ją ma, jej cenę na tej platformie oraz jej datę wydania na tej platfirmie */

CREATE TABLE users_games (
	ug_id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
	gp_id INT REFERENCES games_platforms(gp_id) ON DELETE CASCADE ON UPDATE CASCADE,
	time_spent INT NOT NULL,
	last_played DATE
);

/* Tabela mówiąca kto posiada jakie gry na jakiej paltformie, ile grał w każdą ze swoich gier i kiedy ostatnio w którą z nich grał */


CREATE TABLE transactions (
	t_id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(user_id) ON UPDATE CASCADE,
	amount DECIMAL(10,2),
	currency TEXT REFERENCES currencies(name) ON DELETE RESTRICT ON UPDATE CASCADE,
	date_of_transaction DATE NOT NULL,
	gp_id INT REFERENCES games_platforms(gp_id)
);

/* Tabela trzymająca informacje o dokonanych transakcjach, ich koszcie, walucie w której jej dokonano oraz jej dacie */




INSERT INTO currencies VALUES ('PLN' , 1.0000);
INSERT INTO currencies VALUES ('USD' , 3.8718);
INSERT INTO currencies VALUES ('EUR' , 4.2766);
INSERT INTO currencies VALUES ('CZK' , 0.1679);
INSERT INTO currencies VALUES ('CHF' , 3.9037);
INSERT INTO currencies VALUES ('GBP' , 5.0754);
INSERT INTO currencies VALUES ('JPY' , 3.3200);


INSERT INTO genres VALUES ('FPS'),('RTS'),('MOBA'),('Adventure'),('RPG'),('Soulslike'),('Roguelike'),('Race'),('Action'),('Autobattler'),('Sandbox'),('Cardgame'),('Sport'),('Simulation'),('MMO'),('MMORPG'),('Fantasy'),('Horror'),('Hentai'); 

INSERT INTO platforms(name) VALUES ('Steam');
INSERT INTO platforms(name) VALUES ('Origin');
INSERT INTO platforms(name) VALUES ('Uplay');
INSERT INTO platforms(name) VALUES ('Epic Game Store');
INSERT INTO platforms(name) VALUES ('GOG');
INSERT INTO platforms(name) VALUES ('Blizzard.net');
INSERT INTO platforms(name) VALUES ('Bethesda Launcher');

/* Podstawowe inserty, rzeczy ktore nie beda losowane albo wprowadzane przez uzytkownika pozniej */