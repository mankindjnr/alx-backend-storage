-- createa stored procedure that computes and store
-- the average score for a student
-- average can be a decimal
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
       IN user_id INT
)
BEGIN
	DECLARE average DECIMAL(5, 2);
	SELECT AVG(score) INTO average
	FROM corrections
	WHERE user_id = user_id;

	INSERT INTO users(id, average_score)
	VALUES (user_id, average);
END //

DELIMITER ;
