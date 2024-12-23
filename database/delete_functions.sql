CREATE OR REPLACE FUNCTION delete_movie_by_title_and_date(
    p_title VARCHAR,
    p_watch_date DATE
) RETURNS VOID AS $$
BEGIN
    DELETE FROM Movies
    WHERE title = p_title AND watch_date = p_watch_date;

    IF EXISTS (
        SELECT 1
        FROM DailyActivities
        WHERE activity_date = p_watch_date
    ) THEN
        UPDATE DailyActivities
        SET activities = array_remove(activities, p_title)
        WHERE activity_date = p_watch_date;

        UPDATE DailyActivities
        SET time_rating = CASE
            WHEN array_length(activities, 1) <= 5 THEN 'мало'
            WHEN array_length(activities, 1) > 5 AND  array_length(activities, 1) < 10 THEN 'хорошо'
            WHEN array_length(activities, 1) >= 10 THEN 'отлично'
        END
        WHERE activity_date = p_watch_date;
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_poolvisit_by_name_and_date(
    p_club_name VARCHAR,
    p_visit_date DATE
) RETURNS VOID AS $$
BEGIN
    DELETE FROM PoolVisits
    WHERE club_name = p_club_name AND visit_date = p_visit_date;

    IF EXISTS (
        SELECT 1
        FROM DailyActivities
        WHERE activity_date = p_visit_date
    ) THEN
        UPDATE DailyActivities
        SET activities = array_remove(activities, p_club_name)
        WHERE activity_date = p_visit_date;

        UPDATE DailyActivities
        SET time_rating = CASE
            WHEN array_length(activities, 1) <= 5 THEN 'мало'
            WHEN array_length(activities, 1) > 5 AND  array_length(activities, 1) < 10 THEN 'хорошо'
            WHEN array_length(activities, 1) >= 10 THEN 'отлично'
        END
        WHERE activity_date = p_visit_date;
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION delete_walk_by_name_and_date(
    p_friend_name VARCHAR,
    p_walk_date DATE
) RETURNS VOID AS $$
BEGIN
    DELETE FROM Walks
    WHERE friend_name = p_friend_name AND walk_date = p_walk_date;

    IF EXISTS (
        SELECT 1
        FROM DailyActivities
        WHERE activity_date = p_walk_date
    ) THEN
        UPDATE DailyActivities
        SET activities = array_remove(activities, p_friend_name)
        WHERE activity_date = p_walk_date;

        UPDATE DailyActivities
        SET time_rating = CASE
            WHEN array_length(activities, 1) <= 5 THEN 'мало'
            WHEN array_length(activities, 1) > 5 AND  array_length(activities, 1) < 10 THEN 'хорошо'
            WHEN array_length(activities, 1) >= 10 THEN 'отлично'
        END
        WHERE activity_date = p_walk_date;
    END IF;
END;
$$ LANGUAGE plpgsql;

