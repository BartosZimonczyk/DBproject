CREATE OR REPLACE FUNCTION game_price() RETURNS TRIGGER AS $$
BEGIN
	NEW.amount = (SELECT price FROM games_platforms WHERE id_gp = NEW.id_gp)/(SELECT value_in_PLN FROM currencies WHERE name = NEW.currency);
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER game_price_trigger BEFORE INSERT ON transactions
	FOR EACH ROW EXECUTE PROCEDURE game_price();

/* Trigger przeliczający cenę danej gry (którą domyślnie podajemy dla każdej gry w złotówkach) na cenę w innej walucie. */

CREATE OR REPLACE FUNCTION transaction_date() RETURNS TRIGGER AS $$
BEGIN
	IF (NEW.date_of_transaction <= (SELECT release_date FROM games_platforms WHERE id_gp = NEW.id_gp) OR NEW.date_of_transaction <= (SELECT account_creation FROM users WHERE id_user = NEW.id_user)) THEN
		NEW.date_of_transaction = '2019-12-07';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER transaction_date_trigger BEFORE INSERT ON transactions
	FOR EACH ROW EXECUTE PROCEDURE transaction_date();

/* Trigger zmieniający nieodpowiednią datę transakcji (czyli taką przed powstaniem konta lub wydaniem gry) na taką pasującą (trigger jest tylko po to żeby losowo wygenerowane dane były dobre, został zastąpiony innym opisanym niżej) */



CREATE OR REPLACE FUNCTION friends_since() RETURNS TRIGGER AS $$
BEGIN
	IF (NEW.since <= (SELECT account_creation FROM users WHERE id_user = NEW.user_1) OR NEW.since <= (SELECT account_creation FROM users WHERE id_user = NEW.user_2)) THEN
		NEW.since = '2019-12-07';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER friends_since_trigger BEFORE INSERT ON friends
	FOR EACH ROW EXECUTE PROCEDURE friends_since();

/* Trigger zmieniający nieodpowiednią datę zawarcia znajomości (czyli taką przed założeniem konta któregoś z  użytkowników) na taką pasującą (trigger jest tylko po to żeby losowo wygenerowane dane były dobre, został zastąpiony innym opisanym niżej)*/

CREATE OR REPLACE FUNCTION game_last_played() RETURNS TRIGGER AS $$
BEGIN
	IF (NEW.last_played <= (SELECT account_creation FROM users WHERE id_user = NEW.id_user) OR NEW.last_played <= (SELECT release_date FROM games_platforms WHERE id_gp = NEW.id_game)) THEN
		NEW.last_played = '2019-12-07';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER game_last_played_trigger BEFORE INSERT ON users_games
	FOR EACH ROW EXECUTE PROCEDURE game_last_played();

/* Trigger zmieniający nieodpowiednią datę ostatniej gry (taką przed powstaniem konta lub wydaniem gry) na pasującą (trigger jest tylko po to żeby losowo wygenerowane dane były dobre, został zastąpiony innym opisanym niżej)*/

CREATE OR REPLACE FUNCTION transaction_date_1() RETURNS TRIGGER AS $$
BEGIN
	IF (NEW.date_of_transaction <= (SELECT release_date FROM games_platforms WHERE id_gp = NEW.id_gp) OR NEW.date_of_transaction <= (SELECT account_creation FROM users WHERE id_user = NEW.id_user)) THEN
		RAISE EXCEPTION 'Data transakcji jest niepoprawna!';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER transaction_date_trigger_1 BEFORE INSERT ON transactions
	FOR EACH ROW EXECUTE PROCEDURE transaction_date_1();

/* Trigger wyrzucający błąd gdy próbujemy wpisać nieodpowiednią datę transakcji. Ten trigger zastępuje wczesniejszy, po tym jak zapełniliśmy bazę losowymi danymi */

CREATE OR REPLACE FUNCTION friends_since_1() RETURNS TRIGGER AS $$
BEGIN
	IF (NEW.since <= (SELECT account_creation FROM users WHERE id_user = NEW.user_1) OR NEW.since <= (SELECT account_creation FROM users WHERE id_user = NEW.user_2)) THEN
		RAISE EXCEPTION 'Data zawarcia znajomości jest niepoprawna!';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER friends_since_trigger_1 BEFORE INSERT ON friends
	FOR EACH ROW EXECUTE PROCEDURE friends_since_1();

/* Trigger wyrzucający błąd gdy próbujemy wpisać nieodpowiednią datę zawarcia znajomości. Ten trigger zastepuje wcześniejszy, po tym jak zapełniliśmy bazę losowymi danymi */

CREATE OR REPLACE FUNCTION game_last_played_1() RETURNS TRIGGER AS $$
BEGIN
	IF (NEW.last_played <= (SELECT account_creation FROM users WHERE id_user = NEW.id_user) OR NEW.last_played <= (SELECT release_date FROM games_platforms WHERE id_gp = NEW.id_game)) THEN
		RAISE EXCEPTION 'Data ostatniej rozgrywki jest niepoprawna!';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER game_last_played_trigger_1 BEFORE INSERT ON users_games
	FOR EACH ROW EXECUTE PROCEDURE game_last_played_1();


/* Trigger wrzucający błąd gdy próbujemy wpisać nieodpowiednią datę ostatniej rozgrywki. Ten trigger zastępuje wcześniejszy, po tym jak zapełniliśmy bazę losowymi danymi*/


CREATE OR REPLACE FUNCTION puberty() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT for_kids FROM games AS g JOIN games_platforms AS gp ON g.game_id = gp.game_id AND NEW.gp_id = gp.gp_id) = false THEN
		IF (EXTRACT(year FROM age(NEW.date_of_transaction,(SELECT date_of_birth FROM users WHERE user_id = NEW.user_id))) < 18) THEN
			RAISE EXCEPTION 'Uzytkownik jest zbyt mlody by kupic ta gre!';
		END IF;
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER puberty_trigger BEFORE INSERT ON transactions
	FOR EACH ROW EXECUTE PROCEDURE puberty();

/* Trigger sprawdzajacy czy uzytkownik jest pelnoletni jesli chce kupic gre dla doroslych */



CREATE OR REPLACE FUNCTION bieda() RETURNS TRIGGER AS $$
BEGIN
	UPDATE users SET amount = amount - (NEW.amount * (SELECT value_in_PLN FROM currencies WHERE name = NEW.currency))/(SELECT value_in_PLN FROM currencies WHERE name = users.currency) WHERE user_id = NEW.user_id;
	IF (SELECT amount FROM users WHERE user_id = NEW.user_id) < 0 THEN
		RAISE EXCEPTION 'Uzytkownika nie stac na ta gre!';
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER bieda_trigger BEFORE INSERT ON transactions
	FOR EACH ROW EXECUTE PROCEDURE bieda();
	

/* Trigger sprawdzajacy czy uzytkownik ma wystarczajaco pieniedzy by kupic dana gre i odejmujacy odpowiednia sume z konta jesli go stac */



CREATE OR REPLACE FUNCTION zakup() RETURNS TRIGGER AS $$
BEGIN
	INSERT INTO users_games(user_id,gp_id,time_spent) VALUES (NEW.user_id, NEW.gp_id,0);
	RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER zakup_trigger AFTER INSERT ON transactions
	FOR EACH ROW EXECUTE PROCEDURE zakup();

UPDATE games SET description = '{}' WHERE game_id = {}


/* Trigger dodajacy gre do biblioteki danego gracza po transakcji */
