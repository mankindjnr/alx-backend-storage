-- createa stored procedure that computes and store
-- the average score for a student
-- average can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
       IN user_id INT
)
BEGIN
	DECLARE student_name VARCHAR(255);
	DECLARE average FLOAT;

	SELECT name INTO student_name
	FROM projects
	WHERE id = user_id;
	
	SELECT AVG(score) INTO average
	FROM corrections
	WHERE user_id = user_id;

	IF EXISTS (SELECT * FROM users WHERE id = user_id) THEN
	   UPDATE users
	   SET average_score = average
	   WHERE id = user_id;
	ELSE
		INSERT INTO users(id, name, average_score)
		VALUES (user_id, student_name, average);
	END IF;
END //

DELIMITER ;
