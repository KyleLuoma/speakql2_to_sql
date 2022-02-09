
--Query objective: Display a list of all of the buildings on campus including their names and building number
--Demonstrates: Synonym feature in isolation
--NOTE: There are MANY options here because of the number of synonyms.

--SpeakQL Query option 1:
display building name and buildingnumber
in table building

--SpeakQl Query option 2:
get buildingname, building number 
from table building

--Translated SQL:
SELECT BUILDINGNAME, BUILDING NUMBER
FROM BUILDING



--Query objective: Display a list of room numbers, their building ids, number of wheelchair spaces, and the floor they are on for rooms with wheel chair spots. 
--Special instructions: Specify in this order: FROM SELECT WHERE and try to use SQL keyword syntax.
--Demonstrates: Reordering feature in isolation.

--SpeakQl query:
from room
select roomNumber, buildingId, wheelchairspaces, floor
where wheelchairspaces > 0

--Translated SQL:
SELECT ROOMNUMBER, BUILDINGID, WHEELCHAIRSPACES, FLOOR
FROM ROOM
WHERE WHEELCHAIRSPACES > 0



--Query objective: Look up the department name for department code 'CSE'
--Demonstrates: synonym and reordering features together
-- with a where clause

--SpeakQl Query option 1:
from table department 
show me id and departmentname
where id= 'cse';

--SpeakQl Query option 2:
from table department 
where id= 'cse' 
show me id and departmentname

--Translated SQL:
SELECT ID, DEPARTMENTNAME
FROM DEPARTMENT
WHERE ID = 'CSE'



--Query objective: Display the average room size and capacity for each building 
-- with an average room size (area) greater than 1000:
--Demonstrates: Query partitioned into a speakql join clause and two single-table SFW statements 

--SpeakQl Query
from table room get avg(area) and avg(capacity)
and then from building get buildingname
and then
join room with building on room.buildingid = building.id
group automatically
having avg(area) > 1000;

--Translated SQL
SELECT AVG(ROOM.AREA), AVG(ROOM.CAPACITY), BUILDING.BUILDINGNAME
FROM ROOM
JOIN BUILDING ON ROOM.BUILDINGID = BUILDING.ID
GROUP BY BUILDING.BUILDINGNAME HAVING AVG(AREA) > 1000;



--Query objective: Make a list of buildings and the total number of classrooms in each building. Display the building name, number and count of rooms.
--Demonstrates: Joining two tables an an aggregate function.
--Special instructions: Don't use the JOIN keyword for this query.

--SpeakQl Query
from building get buildingname and buildingnumber
and then from table room display count(id) where buildingid = building.id
group by automatic

--Translated SQL
SELECT BUILDING.BUILDINGNAME, BUILDING.BUILDINGNUMBER, COUNT(ROOM.ID)
FROM BUILDING, ROOM
WHERE(ROOM.BUILDINGID = BUILDING.ID)
GROUP BY BUILDING.BUILDINGNAME, BUILDING.BUILDINGNUMBER


--Query objective: Find out how many courses the CSE department is offering in the Spring 2022 term.
--Demonstrates: Partitioned querying. Focus on the join relationships first, then go back and 
-- think about which elements you want from each table and their associated selection where clauses.
-- Also demonstrates the group by automatic inference feature

-- Courses by each dept for each quarter. use where predicates on different attributes
-- how many courses offered by each department for each quarter since 2020. <--- DO THIS!!!4
-- for courses that are at least two units each

--UNBUNDLED SUBQUERY 

join department with course on department.id = course.deptid
join course with courseoffering on course.id = courseoffering.courseid
join term with courseoffering on term.id = courseoffering.termid
and then
from department get departmentname where id = "cse" -- look for doing a where condition on a different table
and then
from courseoffering get count(id)
and then
from course get nothing where units >= 2 -- <- NEW FEATURE with reserved word to allow for getting nothing but define a where statement
and then
from term get year and termperiod where year >= 2020 and termperiod = "Spring"
group by automatic


--Translated SQL:
SELECT DEPARTMENT.DEPARTMENTNAME, COUNT(COURSEOFFERING.ID), TERM.YEAR, TERM.TERMPERIOD
FROM DEPARTMENT
JOIN COURSE ON DEPARTMENT.ID = COURSE.DEPTID 
JOIN COURSEOFFERING ON COURSE.ID = COURSEOFFERING.COURSEID 
JOIN TERM ON TERM.ID = COURSEOFFERING.TERMID
WHERE(DEPARTMENT.ID = "CSE") AND(TERM.YEAR = 2022 AND TERM.TERMPERIOD = "SPRING")
GROUP BY DEPARTMENT.DEPARTMENTNAME, TERM.YEAR, TERM.TERMPERIOD