CREATE OR REPLACE FUNCTION insert_into_movies(
    p_title VARCHAR,
    p_genre VARCHAR,
    p_watch_date DATE
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO Movies (title, genre, watch_date)
    VALUES (p_title, p_genre, p_watch_date);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insert_into_poolvisits(
    p_club_name VARCHAR,
    p_duration INT,
    p_visit_date DATE
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO PoolVisits (club_name, duration, visit_date)
    VALUES (p_club_name, p_duration, p_visit_date);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insert_into_walks(
    p_friend_name VARCHAR,
    p_duration INT,
    p_walk_date DATE
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO Walks (friend_name, duration, walk_date)
    VALUES (p_friend_name, p_duration, p_walk_date);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_all_dailyactivities()
RETURNS TABLE (activity_date DATE, activities TEXT[], time_rating TEXT) AS $$
BEGIN
    RETURN QUERY SELECT * FROM DailyActivities;
END;
$$ LANGUAGE plpgsql;
