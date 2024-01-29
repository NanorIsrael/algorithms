DROP TABLE IF EXISTS developers_project;
DROP TABLE IF EXISTS developers;
DROP TABLE IF EXISTS project;

CREATE TABLE developers (
	id INT PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	hourly_rate INT,
	type_of_contract VARCHAR(255),
	started_work DATE,
	stopped_work DATE
);

CREATE TABLE project (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255),
	budget INT,
	start_date DATE,
	end_date DATE
);

CREATE TABLE developers_project (
	developer_id INT,
	project_id INT,
	is_leader BIT,
	date_join DATE,
	FOREIGN KEY (developer_id) REFERENCES developers(id),
	FOREIGN KEY (project_id) REFERENCES project(id)
);
-- declare  john_dev_id int;
-- declare  jane_dev_id int;


-- declare  almanac_id int;
-- declare  greater_grace int;
-- declare  slide_boxes int;
-- declare  defcon int;
INSERT INTO developers(first_name, last_name, hourly_rate, type_of_contract, started_work, stopped_work) VALUES ('John', 'Doe', 20, 'full time', '2018-09-08', NULL);
SET @john_dev_id = LAST_INSERT_ID();

INSERT INTO developers(first_name, last_name, hourly_rate, type_of_contract, started_work, stopped_work) VALUES ('Jane', 'Doe', 12, 'full time', '2019-09-08', NULL);
SET @jane_dev_id = LAST_INSERT_ID();

INSERT INTO developers(first_name, last_name, hourly_rate, type_of_contract, started_work, stopped_work) VALUES ('David', 'Smith', 30, 'part time', '2019-09-08', NULL);
SET @david_dev_id = LAST_INSERT_ID();

INSERT INTO developers(first_name, last_name, hourly_rate, type_of_contract, started_work, stopped_work) VALUES ('Danniella', 'Smith', 20, 'part time', '2020-01-08', NULL);
SET @daniel_dev_id = LAST_INSERT_ID();

INSERT INTO project(name, budget, start_date, end_date) VALUES ('Almanac', 2000, '2019-10-01', '2020-09-01');
SET @almanac_id = LAST_INSERT_ID();

INSERT INTO project(name, budget, start_date, end_date) VALUES ('Greater grace', 2000, '2020-10-01', '2021-09-01');
SET @greater_grace = LAST_INSERT_ID();

INSERT INTO project(name, budget, start_date, end_date) VALUES ('Slide boxes', 2000, '2019-01-01', '2019-12-01');
SET @slide_boxes = LAST_INSERT_ID();

INSERT INTO project(name, budget, start_date, end_date) VALUES ('Defcon', 2000, '2019-01-01', '2019-12-01');
SET @defcon = LAST_INSERT_ID();

INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@john_dev_id, @almanac_id, 1, '2019-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@john_dev_id, @greater_grace, 1, '2020-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@john_dev_id, @slide_boxes, 1, '2019-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@john_dev_id, @defcon, 1, '2020-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@jane_dev_id, @defcon, 0, '2020-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@jane_dev_id, @defcon, 0, '2020-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@david_dev_id, @defcon, 1, '2020-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@daniel_dev_id, @defcon, 0, '2020-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@david_dev_id, @almanac_id, 1, '2019-01-01');
INSERT INTO developers_project(developer_id, project_id, is_leader, date_join) VALUES (@daniel_dev_id, @almanac_id, 0, '2019-01-01');