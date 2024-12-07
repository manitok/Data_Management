-- Индекс для поля club_name в таблице PoolVisits
CREATE INDEX idx_poolvisits_club_name ON PoolVisits (club_name);

-- Индекс для поля friend_name в таблице Walks
CREATE INDEX idx_walks_friend_name ON Walks (friend_name);

-- Индекс для поля title в таблице Movies
CREATE INDEX idx_movies_title ON Movies (title);