
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



--Query objective: Find the average size of all rooms (Similar to Q1)
--Demonstrates: aggregation function access using SpeakQl synonyms

--SpeakQl Query option 1:
show me avg(area) in table room

--SpeakQl Query option :
in table room get avg(area)

--Translated SQL:
SELECT AVG(AREA)
FROM ROOM


--Query objective: Look up the department name for department code 'CSE'
--Demonstrates: synonym and reordering features together
-- with a where clause (Similar to Q2)

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



--Query objective: Get the course id of all courses being offered in 2022 (Similar to Q2)
--Demonstrates: a simple join combined with a where predicate
--NOTE: This shows that the speakql unbundling may not always result in a shorter query

--SpeakQl Query:
join courseoffering with term on courseoffering.termid = term.id
and then
get courseid from courseoffering
and then
get nothing from term where year = 2022

--Translated SQL:
SELECT COURSEOFFERING.COURSEID
FROM COURSEOFFERING
JOIN TERM ON COURSEOFFERING.TERMID = TERM.ID
WHERE(TERM.YEAR = 2022)



--Query objective: Get the days and start time of course offerings for courses in room with id 'CENTR 206' 
-- and term with id 'FALL2021' (Similar to Q3)
--Demonstrates the use of a where predicate

--SpeakQl Query:
in table courseoffering 
find ondays and starttime 
where roomid = 'CENTR 206' and termid = 'FALL2021'

--Translated SQL:
SELECT ONDAYS, STARTTIME
FROM COURSEOFFERING
WHERE ROOMID = 'CENTR 206' AND TERMID = 'FALL2021'



--Query objective: Display a list of room numbers, their building ids, number of wheelchair spaces, and the floor they are on for rooms with wheel chair spots. 
--Special instructions: Specify in this order: FROM SELECT WHERE and try to use SQL keyword syntax.
--Demonstrates: Reordering feature in isolation (Similar to Q3)

--SpeakQl query:
from room
select roomNumber, buildingId, wheelchairspaces, floor
where wheelchairspaces > 0

--Translated SQL:
SELECT ROOMNUMBER, BUILDINGID, WHEELCHAIRSPACES, FLOOR
FROM ROOM
WHERE WHEELCHAIRSPACES > 0



--Query objective: Display the average room size and capacity for each building. (Similar to Q4)
-- with an average room size (area) greater than 1000:
--Demonstrates: Query partitioned into a speakql join clause and two single-table SFW statements 

--SpeakQl Query
from table room get the avg(area) and avg(capacity)
and then 
from building get buildingname
and then
join room with building on room.buildingid = building.id
and then
group automatically
having avg(area) > 1000;

--Translated SQL
SELECT AVG(ROOM.AREA), AVG(ROOM.CAPACITY), BUILDING.BUILDINGNAME
FROM ROOM
JOIN BUILDING ON ROOM.BUILDINGID = BUILDING.ID
GROUP BY BUILDING.BUILDINGNAME 
HAVING AVG(AREA) > 1000;



--Query objective: Find out the total number of courses offered by UCSD in term SPRING2020 (Hint, use the count function)
--Demonstrates aggregation with a where predicate on a single table (Similar to Q5)

--SpeakQl query:
what is the count of (courseid) 
in table courseoffering 
where termid = "SPRI2020"

--Translated SQL:
SELECT COUNT(COURSEID)
FROM COURSEOFFERING
WHERE TERMID = "SPRI2020"



--Query objective: What is the ending time and number of classes for each ending time of
--the course offerings? (Similar to Q6)
--Demonstrates: Singular aggregation and group-by. Can use this to show SQL and SpeakQl options.

--SpeakQl query option 1:
what is the endtime and count of (courseid) in courseoffering
group automatically

--SpeakQl query option 2:
in table courseoffering 
find endtime and count(courseid) 
group by endtime

--Translated SQL:
SELECT ENDTIME, COUNT(COURSEID)
FROM COURSEOFFERING
GROUP BY ENDTIME


--Query objective: Using the room table, find the total number of wheelchair spaces and the average square feet per classroom for
--classrooms with at least one wheelchair space.
--Group by each building and building floor. No need for building name, building ID is sufficient.
--(Similar to Q7)
--Demonstrates: multiple aggregations on the same table and the group by automatic feature

--SpeakQl query:
in table room 
show me buildingid, floor, 
    the count of (wheelchairspaces), 
    the sum of (capacity) 
    and the avg (area) 
where wheelchairspaces > 0
group by automatic

--Translated SQL
SELECT BUILDINGID, FLOOR, COUNT(WHEELCHAIRSPACES), SUM(CAPACITY), AVG(AREA)
FROM ROOM
WHERE WHEELCHAIRSPACES > 0
GROUP BY BUILDINGID, FLOOR



--Query objective: Find out how many courses the CSE department is offering in the Spring 2022 term.
-- (Similar to Q9)
--Demonstrates: Unbundled querying. Focus on the join relationships first, then go back and 
-- think about which elements you want from each table and their associated selection where clauses.
-- Also demonstrates the group by automatic inference feature

-- Courses by each dept for each quarter. use where predicates on different attributes
-- how many courses offered by each department for each quarter since 2021.
-- for courses that are more than four units each

--UNBUNDLED SUBQUERY 

join department with course on department.id = course.deptid
and then
join course with courseoffering on course.id = courseoffering.courseid
and then
join term with courseoffering on term.id = courseoffering.termid
and then
from department get departmentname 
and then
from courseoffering get count(id)
and then
from course get nothing where units > 4
and then
from term get year and termperiod where year >= 2021
and then
group by automatic order by year


--Translated SQL:
SELECT DEPARTMENT.DEPARTMENTNAME, COUNT(COURSEOFFERING.ID), TERM.YEAR, TERM.TERMPERIOD
FROM DEPARTMENT
JOIN COURSE ON DEPARTMENT.ID = COURSE.DEPTID 
JOIN COURSEOFFERING ON COURSE.ID = COURSEOFFERING.COURSEID 
JOIN TERM ON TERM.ID = COURSEOFFERING.TERMID
WHERE(DEPARTMENT.ID = "CSE") AND(TERM.YEAR = 2022 AND TERM.TERMPERIOD = "SPRING")
GROUP BY DEPARTMENT.DEPARTMENTNAME, TERM.YEAR, TERM.TERMPERIOD


--Query objective: Make a list of buildings and the total number of classrooms in each building. 
--Display the building name, number and count of rooms. (Similar to Q11)
--Demonstrates: Joining two tables an an aggregate function.
--Special instructions: Don't use the JOIN keyword for this query.

--SpeakQl Query
from building get buildingname and buildingnumber
and then 
from table room display count(id) where buildingid = building.id
and then
group by automatic

--Translated SQL
SELECT BUILDING.BUILDINGNAME, BUILDING.BUILDINGNUMBER, COUNT(ROOM.ID)
FROM BUILDING, ROOM
WHERE(ROOM.BUILDINGID = BUILDING.ID)
GROUP BY BUILDING.BUILDINGNAME, BUILDING.BUILDINGNUMBER