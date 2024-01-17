-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT city.`id`, city.`name`, state.`name` FROM `cities` AS city
INNER JOIN `states` as state ON city.`state_id` = state.`id`
ORDER BY city.`id`;
