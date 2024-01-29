DROP FUNCTION if exists AddBonus;

DELIMITER $$

CREATE FUNCTION AddBonus ()
RETURNS CHAR(50) DETERMINISTIC
BEGIN
RETURN 'HELLO WORLD';
END;
$$

DELIMITER ;


DROP PROCEDURE IF EXISTS AddBonus;

-- DELIMITER $$

-- CREATE PROCEDURE AddBonus (IN user_id CHAR(255), project_name CHAR(255), score INT)
-- BEGIN
-- UPDATE users SET average_score = score WHERE users.id = user_id;
-- DECLARE project_id INT;
-- SELECT COALESCE(
-- (SELECT id FROM projects WHERE name = project_name),
--  (INSERT INTO projects (name) VALUES (project_name) RETURNING id)) 
--  INTO project_id;
-- END;
-- $$

-- DELIMITER ;

DELIMITER $$

CREATE PROCEDURE AddBonus (IN user_id CHAR(255), project_name CHAR(255), score INT)
BEGIN
    UPDATE users SET users.average_score = score WHERE users.id = user_id;

    SET @project_id = COALESCE((SELECT id FROM projects WHERE name = project_name), 0);

    IF @project_id = 0 THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @project_id = LAST_INSERT_ID();
    END IF;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
END;
$$

DELIMITER ;


-- SELECT CONCAT(user_id, ' ', project_name);

-- SELECT hello('world')
-- call AddBonus('1233', 'almanac', 90)
-- select AddBonus()