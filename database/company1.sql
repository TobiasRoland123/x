DROP TABLE IF EXISTS users;


CREATE TABLE users(
    user_pk             TEXT UNIQUE,
    user_user_name      TEXT UNIQUE,
    user_name           TEXT,
    user_email          TEXT UNIQUE,
    PRIMARY KEY(user_pk)
)WITHOUT ROWID;


INSERT INTO users VALUES('1', 'a', 'A', '@a');
INSERT INTO users VALUES('2', 'b', 'B', '@b');
INSERT INTO users VALUES('3', 'c', 'C', '@c');


-- #####################################

DROP TABLE IF EXISTS pets;

CREATE TABLE pets(
    pet_pk          TEXT UNIQUE,
    pet_type        TEXT UNIQUE,
    PRIMARY KEY(pet_pk)
) WITHOUT ROWID;

INSERT INTO pets VALUES ('1', 'dog');
INSERT INTO pets VALUES ('2', 'cat');



-- #####################################

DROP TABLE IF EXISTS users_pets;

CREATE TABLE users_pets(
    user_fk         TEXT,
    pet_fk          TEXT,

    PRIMARY KEY (user_fk, pet_fk) -- compund key
) WITHOUT ROWID;

INSERT INTO users_pets VALUES('1','1');
INSERT INTO users_pets VALUES('1','2');
INSERT INTO users_pets VALUES('2','2');



-- #####################################


DROP VIEW IF EXISTS v_users_pets;

CREATE VIEW v_users_pets AS
SELECT user_pk, user_name, user_email, pet_type
FROM users
JOIN users_pets ON user_pk = user_fk
JOIN pets ON pet_fk = pet_pk;

SELECT * FROM v_users_pets;

-- SELECT user_pk, user_name, user_email, pet_type
-- FROM users
-- JOIN users_pets ON user_pk = user_fk
-- JOIN pets ON pet_fk = pet_pk;
