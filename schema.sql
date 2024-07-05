-- CREATE USERS TABLE
CREATE TABLE IF NOT EXISTS public.users (
    id serial4 NOT NULL,
    "name" text NOT NULL,
    "admin" bool DEFAULT false NULL,
    active bool DEFAULT true NOT NULL,
    phone int4 NULL,
    registration_date date NOT NULL,
    total_messages_weight int4 DEFAULT 0 NOT NULL,
    email text NULL,
    CONSTRAINT users_pk PRIMARY KEY (id)
);

-- CREATE MESSAGES TABLE WITH USERS RELATION
CREATE TABLE IF NOT EXISTS public.messages (
    id serial4 NOT NULL,
    "type" text NOT NULL,
    weight int4 NOT NULL,
    "date" date NULL,
    user_id serial4 NOT NULL,
    CONSTRAINT messages_pk PRIMARY KEY (id),
    CONSTRAINT messages_users_fk FOREIGN KEY (user_id) REFERENCES public.users(id)
);
