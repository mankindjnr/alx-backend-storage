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
	DECLARE average DECIMAL(5, 2);

	SELECT name INTO student_name
	FROM projects
	WHERE id = user_id;
	
	SELECT AVG(score) INTO average
	FROM corrections
	WHERE user_id = user_id;

	INSERT INTO users(id, name, average_score)
	VALUES (user_id, student_name, average);
END //

DELIMITER ;
