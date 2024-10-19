
-- Create league table
CREATE TABLE league (
  id SERIAL PRIMARY KEY,  -- PostgreSQL uses SERIAL for auto-incrementing integers
  association VARCHAR(255) NOT NULL,
  first_match DATE NOT NULL,
  champion INT DEFAULT NULL,
  record_player VARCHAR(255) DEFAULT NULL,
  games_recordplayer INT DEFAULT NULL
);

-- Create clubs table
CREATE TABLE clubs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  league_id INT DEFAULT NULL,
  CONSTRAINT club_league_fk FOREIGN KEY (league_id) REFERENCES league (id) ON DELETE SET NULL
);

-- Create player table
CREATE TABLE players (
  id SERIAL PRIMARY KEY,
  club_id INT NOT NULL,
  trikot_no INT DEFAULT NULL,
  name VARCHAR(255) NOT NULL,
  country VARCHAR(255) DEFAULT NULL,
  games INT DEFAULT NULL,
  goals INT DEFAULT NULL,
  assists INT DEFAULT NULL,
  CONSTRAINT player_club_fk FOREIGN KEY (club_id) REFERENCES clubs (id)
);

-- Create game table
CREATE TABLE games (
  id SERIAL PRIMARY KEY,
  matchday INT DEFAULT NULL,
  date DATE DEFAULT NULL,
  time TIME DEFAULT NULL,
  home_club INT NOT NULL,
  guest_club INT NOT NULL,
  goals_home INT DEFAULT NULL,
  goals_guest INT DEFAULT NULL,
  CONSTRAINT game_club_fk1 FOREIGN KEY (home_club) REFERENCES clubs (id),
  CONSTRAINT game_club_fk2 FOREIGN KEY (guest_club) REFERENCES clubs (id)
);

ALTER TABLE IF EXISTS league
    OWNER to football;

ALTER TABLE IF EXISTS clubs
    OWNER to football;

ALTER TABLE IF EXISTS players
    OWNER to football;

ALTER TABLE IF EXISTS games
    OWNER to football;            

COMMIT;

Insert into league (association, first_match, champion, record_player, games_recordplayer)
    VALUES
        ('Die Liga - Fußballverband', '1963-08-24', 1, 'Karl-Heinz Körbel', 602);

Insert into clubs (id, name, league_id) 
    VALUES 
        (1, '1. FC Bayern München', 1),
        (2, 'VfL Wolfsburg', 1);

COMMIT;
