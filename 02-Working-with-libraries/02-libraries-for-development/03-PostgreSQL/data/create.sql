CREATE ROLE postgres WITH
  LOGIN
  SUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  REPLICATION
  BYPASSRLS
  ENCRYPTED PASSWORD 'md5204221755ca4f5e119f0701c8658de30';

CREATE TABLE IF NOT EXISTS public.clubs
(
    id bigint NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    league_id bigint NOT NULL,
    CONSTRAINT clubs_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clubs
    OWNER to football;