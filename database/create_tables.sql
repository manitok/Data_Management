CREATE TABLE Movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    watch_date DATE NOT NULL
);

CREATE TABLE PoolVisits (
    id SERIAL PRIMARY KEY,
    club_name VARCHAR(255) NOT NULL,
    duration INT NOT NULL,
    visit_date DATE NOT NULL
);

CREATE TABLE Walks (
    id SERIAL PRIMARY KEY,
    friend_name VARCHAR(255) NOT NULL,
    duration INT NOT NULL,
    walk_date DATE NOT NULL
);

CREATE TABLE DailyActivities (
    activity_date DATE PRIMARY KEY,
    activities TEXT[] NOT NULL,
    time_rating TEXT
);


