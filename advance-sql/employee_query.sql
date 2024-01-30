-- SELECT
--     p.name AS project_name,
--     d.first_name,
--     d.last_name,
--     d.hourly_rate,
--     CASE
--         WHEN dp.is_leader = 1 THEN 'Project leader'
--         ELSE 'Developer'
--     END AS role
-- FROM
--     developers d
-- JOIN
--     developers_project dp ON d.id = dp.developer_id
-- JOIN
--     project p ON dp.project_id = p.id
-- WHERE
-- 	d.hourly_rate >= (SELECT AVG(hourly_rate) FROM developers)
-- 	AND YEAR(d.start_date) = 2019
-- ORDER BY
-- 	p.name ASC, role DESC\G;

SELECT CURRENT_DATE;