-- Create second_table in hbtn_0c_0 database in MySQL server and add multiples rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- We can also insert each register at a time or all at once (like we do here)
INSERT INTO
    second_table (id, name, score)
VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
