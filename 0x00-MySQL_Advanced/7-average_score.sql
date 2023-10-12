-- Create stored procedure ComputeAverageScoreForUser
-- computes and stores average score for a student
-- Takes 1 input user_id, a users.id

DELIMITER $$;
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN userId INT)
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections
    WHERE correction.user_id = userId) WHERE id = userId;
END $$;
DELIMITER ;
