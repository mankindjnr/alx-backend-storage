-- createa stored procedure that computes and store
-- the average score for a student
-- average can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE num_scores INT;

    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    SELECT COUNT(*) INTO num_scores
    FROM corrections
    WHERE user_id = user_id;

    IF num_scores > 0 THEN
        UPDATE users
        SET average_score = total_score / num_scores
        WHERE id = user_id;
    END IF;
END //

DELIMITER ;
