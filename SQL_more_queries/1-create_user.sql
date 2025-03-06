-- Create the user 'user_0d_1' if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to 'user_0d_1' on all databases and tables
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost'
WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;
