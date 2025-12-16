CREATE SCHEMA IF NOT EXISTS sentinel;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS processed;

CREATE TYPE role AS ENUM ('admin', 'user');

CREATE TABLE IF NOT EXISTS sentinel.users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    login TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,

    role role NOT NULL,

    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS raw.users (
    id SERIAL PRIMARY KEY,
    intra TEXT NOT NULL,
    evaluations JSONB,
    fetched_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS processed.users (
    id SERIAL PRIMARY KEY,
    intra TEXT NOT NULL,
    processed_at TIMESTAMP DEFAULT NOW()
);