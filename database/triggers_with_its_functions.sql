CREATE OR REPLACE FUNCTION update_daily_activities_after_movie()
RETURNS TRIGGER AS $$
BEGIN
    -- Проверяем, существует ли запись с датой из новой строки в таблице DailyActivities
    IF NOT EXISTS (
        SELECT 1 
        FROM DailyActivities 
        WHERE activity_date = NEW.watch_date
    ) THEN
        -- Если строки с указанной датой нет, создаем новую запись
        INSERT INTO DailyActivities (activity_date, activities, time_rating)
        VALUES (NEW.watch_date, ARRAY[NEW.title], 'мало');
    ELSE
        -- Если строка с датой уже существует, обновляем массив activities
        UPDATE DailyActivities
        SET activities = activities || NEW.title
        WHERE activity_date = NEW.watch_date;

        -- Пересчитываем time_rating на основе количества элементов в activities
        UPDATE DailyActivities
        SET time_rating = CASE
            WHEN array_length(activities, 1) <= 5 THEN 'мало'
            WHEN array_length(activities, 1) > 5 AND  array_length(activities, 1) < 10 THEN 'хорошо'
            WHEN array_length(activities, 1) >= 10 THEN 'отлично'
        END
        WHERE activity_date = NEW.watch_date;
    END IF;

    RETURN NEW; -- Возвращаем новую строку
END;
$$ LANGUAGE plpgsql;



CREATE TRIGGER after_movie_insert
AFTER INSERT ON Movies
FOR EACH ROW
EXECUTE FUNCTION update_daily_activities_after_movie();



CREATE OR REPLACE FUNCTION update_daily_activities_after_pool_visit()
RETURNS TRIGGER AS $$
BEGIN
    -- Проверяем, существует ли запись с датой из новой строки в таблице DailyActivities
    IF NOT EXISTS (
        SELECT 1 
        FROM DailyActivities 
        WHERE activity_date = NEW.visit_date
    ) THEN
        -- Если строки с указанной датой нет, создаем новую запись
        INSERT INTO DailyActivities (activity_date, activities, time_rating)
        VALUES (NEW.visit_date, ARRAY[NEW.club_name], 'мало');
    ELSE
        -- Если строка с датой уже существует, обновляем массив activities
        UPDATE DailyActivities
        SET activities = activities || NEW.club_name
        WHERE activity_date = NEW.visit_date;

        -- Пересчитываем time_rating на основе количества элементов в activities
        UPDATE DailyActivities
        SET time_rating = CASE
            WHEN array_length(activities, 1) <= 5 THEN 'мало'
            WHEN array_length(activities, 1) > 5 AND  array_length(activities, 1) < 10 THEN 'хорошо'
            WHEN array_length(activities, 1) >= 10 THEN 'отлично'
        END
        WHERE activity_date = NEW.visit_date;
    END IF;

    RETURN NEW; -- Возвращаем новую строку
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER after_pool_visit_insert
AFTER INSERT ON PoolVisits
FOR EACH ROW
EXECUTE FUNCTION update_daily_activities_after_pool_visit();




CREATE OR REPLACE FUNCTION update_daily_activities_after_walk()
RETURNS TRIGGER AS $$
BEGIN
    -- Проверяем, существует ли запись с датой из новой строки в таблице DailyActivities
    IF NOT EXISTS (
        SELECT 1 
        FROM DailyActivities 
        WHERE activity_date = NEW.walk_date
    ) THEN
        -- Если строки с указанной датой нет, создаем новую запись
        INSERT INTO DailyActivities (activity_date, activities, time_rating)
        VALUES (NEW.walk_date, ARRAY[NEW.friend_name], 'мало');
    ELSE
        -- Если строка с датой уже существует, обновляем массив activities
        UPDATE DailyActivities
        SET activities = activities || NEW.friend_name
        WHERE activity_date = NEW.walk_date;

        -- Пересчитываем time_rating на основе количества элементов в activities
        UPDATE DailyActivities
        SET time_rating = CASE
            WHEN array_length(activities, 1) <= 5 THEN 'мало'
            WHEN array_length(activities, 1) > 5 AND  array_length(activities, 1) < 10 THEN 'хорошо'
            WHEN array_length(activities, 1) >= 10 THEN 'отлично'
        END
        WHERE activity_date = NEW.walk_date;
    END IF;

    RETURN NEW; -- Возвращаем новую строку
END;
$$ LANGUAGE plpgsql;




CREATE TRIGGER after_walk_insert
AFTER INSERT ON Walks
FOR EACH ROW
EXECUTE FUNCTION update_daily_activities_after_walk();




