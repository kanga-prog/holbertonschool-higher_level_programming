-- Create the table unique_id if it doesn't exist
CREATE TABLE IF EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
