
--Query objective: Display a list of all of the buildings on campus including their 
--names and building number
--Demonstrates: Synonym feature in isolation
--NOTE: There are MANY options here because of the number of synonyms.

--SpeakQL Query option 1:
display buildingname and buildingnumber
in building

--SpeakQl Query option 2:
get buildingname, buildingnumber 
from table building

--SpeakQl Query option 3:
get buildingname and buildingnumber 
from the building table

--SpeakQL Query option 4:
in the building table 
show me buildingname and buildingnumber

--Translated SQL:
SELECT BUILDINGNAME, BUILDING NUMBER
FROM BUILDING



--Query objective: Find the average area of all rooms (Similar to Q1)
--Demonstrates: aggregation function access using SpeakQl synonyms

--SpeakQl Query option 1:
what is the avg (area) in the room table

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
where id = 'cse';

--SpeakQl Query option 2:
from table department 
where id = 'cse' 
show me id and departmentname

--SpeakQl query option 3:
find id and departmentname 
in the department table 
where id = 'cse'

--Translated SQL:
SELECT ID, DEPARTMENTNAME
FROM DEPARTMENT
WHERE ID = 'CSE'



--Query objective: Get the course id of all courses being offered in 2022 (Similar to Q2)
--Demonstrates: a simple join combined with a where predicate
--NOTE: This shows that the speakql unbundling may not always result in a shorter query

--SpeakQl Query option 1:
join courseoffering with term on courseoffering.termid = term.id
and then
get courseid from courseoffering
and then
get nothing from term where year = 2022

--SpeakQl Query option 2:

join the courseoffering table with the term table on courseoffering.termid = term.id
and then
from courseoffering show me courseid
and then
get nothing from the term table where year = 2022

--Translated SQL:
SELECT COURSEOFFERING.COURSEID
FROM COURSEOFFERING
JOIN TERM ON COURSEOFFERING.TERMID = TERM.ID
WHERE(TERM.YEAR = 2022)



--Query objective: Get the days and start time of course offerings for courses in 
-- room with id 'CENTR 206' 
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



--Query objective: Display a list of room numbers, their building ids, number of 
--wheelchair spaces, and the floor they are on for rooms with wheel chair spots. 
--Special instructions: Specify in this order: FROM SELECT WHERE and try to use 
--SQL keyword syntax.
--Demonstrates: Reordering feature in isolation (Similar to Q3)

--SpeakQl query:
from room
select roomNumber, buildingId, wheelchairspaces, floor
where wheelchairspaces > 0

--Translated SQL:
SELECT ROOMNUMBER, BUILDINGID, WHEELCHAIRSPACES, FLOOR
FROM ROOM
WHERE WHEELCHAIRSPACES > 0



--Query objective: Display the building name, average room area and average capacity for each building with an average room size (area) greater than 1000:
--Demonstrates: Query partitioned into a speakql join clause and two single-table
-- SFW statements 

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

--SpeakQl query option 1:
in table room 
show me buildingid, floor, 
    the count of (wheelchairspaces), 
    the sum of (capacity) 
    and the avg (area) 
where wheelchairspaces > 0
group by automatic

--SpeakQl query option 2:
get buildingid, floor, the count of (wheelchairspaces), the sum of (capacity) and the avg of (area)
from the room table
where wheelchairspaces > 0
group automatically


--Translated SQL
SELECT BUILDINGID, FLOOR, COUNT(WHEELCHAIRSPACES), SUM(CAPACITY), AVG(AREA)
FROM ROOM
WHERE WHEELCHAIRSPACES > 0
GROUP BY BUILDINGID, FLOOR



--Query objective: Fetch the faculty name, course title, course units, and start time for courses taught by either Jdavie Crop
-- or Anabelle Handman or Cahra Scrammage or Gloriane Betke (Similar to Q8)
--Demonstrates two table join and an WHERE IN condition

--SpeakQl Query option 1:
join the course table with the courseoffering table on course.id = courseoffering.courseid
and then
from the courseoffering table where facultyname in ("Jdavie Crop", "Anabelle Handman", "Cahra Scrammage", "Gloriane Betke")
show me facultyname and starttime
and then
from the course table get title and units 
and then
order by facultyname

--SpeakQl Query option 2:
get facultyname, title, units and starttime 
from the course table 
joined with the courseoffering table on course.id = courseoffering.courseid 
where facultyname in ("Jdavie Crop", "Anabelle Handman", "Cahra Scrammage", "Gloriane Betke")
and then
order by facultyname

--SpeakQl Query option 3:
in the courseoffering table get facultyname and starttime 
where facultyname is in ("Jdavie Crop", "Anabelle Handman", "Cahra Scrammage", "Gloriane Betke")
and then
get title and units from the course table where course.id = courseoffering.id
and then
order by facultyname


--Translated SQL (options 1 and 2):
SELECT COURSEOFFERING.FACULTYNAME, COURSEOFFERING.STARTTIME, COURSE.TITLE, COURSE.UNITS
FROM COURSEOFFERING
JOIN COURSE ON COURSE.ID = COURSEOFFERING.COURSEID
WHERE(COURSEOFFERING.FACULTYNAME IN("JDAVIE CROP", "ANABELLE HANDMAN", "CAHRA SCRAMMAGE", "GLORIANE BETKE")) 
ORDER BY FACULTYNAME

--Translated SQL (option 3):
SELECT COURSEOFFERING.FACULTYNAME, COURSEOFFERING.STARTTIME, COURSE.TITLE, COURSE.UNITS
FROM COURSEOFFERING, COURSE
WHERE(COURSEOFFERING.FACULTYNAME IN("JDAVIE CROP", "ANABELLE HANDMAN", "CAHRA SCRAMMAGE", "GLORIANE BETKE")) 
    AND(COURSE.ID = COURSEOFFERING.COURSEID) 
ORDER BY FACULTYNAME




--Query objective: Find out how many courses the CSE department is offering in the Spring 2022 term.
-- (Similar to Q9)
--Demonstrates: Unbundled querying. Focus on the join relationships first, then go back and 
-- think about which elements you want from each table and their associated selection where clauses.
-- Also demonstrates the group by automatic inference feature

-- Courses by each dept for each quarter. use where predicates on different attributes
-- how many courses offered by each department for each quarter since 2021.
-- for courses that are more than four units each

--UNBUNDLED SUBQUERY 

--SpeakQl Query Option 1:
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

--SpeakQl Query option 2:
join the department table with the course table on department.id = course.deptid
and then
join the course table with courseoffering on course.id = courseoffering.courseid
and then
join the term table with the courseoffering table on term.id = courseoffering.termid
and then
get departmentname from the department table
and then
find the count of (id) in the courseoffering table
and then
get no columns from the course table where units > 4
and then
from the term table find year and termperiod where year >= 2021
and then
group by automatic
order by year


--Translated SQL:
SELECT DEPARTMENT.DEPARTMENTNAME, COUNT(COURSEOFFERING.ID), TERM.YEAR, TERM.TERMPERIOD
FROM DEPARTMENT
JOIN COURSE ON DEPARTMENT.ID = COURSE.DEPTID 
JOIN COURSEOFFERING ON COURSE.ID = COURSEOFFERING.COURSEID 
JOIN TERM ON TERM.ID = COURSEOFFERING.TERMID
WHERE(DEPARTMENT.ID = "CSE") AND(TERM.YEAR = 2022 AND TERM.TERMPERIOD = "SPRING")
GROUP BY DEPARTMENT.DEPARTMENTNAME, TERM.YEAR, TERM.TERMPERIOD



--Query objective: Fetch all fields for the rooms that have 2 wheelchair spaces, 
--or have a seating capacity greater than 40, or that are on the first floor. 
--Get only the first 10 records. (Similar to Q10)
--Demonstrates: Application of multiple OR predicates to a single table

--SpeakQl Query
in the room table
find *
where wheelchairspaces = 2 or capacity > 40 or floor = 1
limit 10

--Translated SQL:
SELECT *
FROM ROOM
WHERE WHEELCHAIRSPACES = 2 OR CAPACITY > 40 OR FLOOR = 1 LIMIT 10



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



--Query objective: Display the building name, building number, room number, course title, and start time for courses offered by the CSE department in Fall of 2021 
--sorted by building number (Similar to Q12)
--Demonstrates: Join of five different tables with selections across four and a where condition applied to a table without columns in the query.

--SpeakQl Query option 1 (All joins first then selections and projections):
join the building table with the room table on building.id = room.buildingid
and then
join the room table with the courseoffering table on room.id = courseoffering.roomid
and then
join the term table with the courseoffering table on term.id = courseoffering.termid
and then
join the course table with the courseoffering table on course.id = courseoffering.courseid
and then
from the building table display buildingname and buildingnumber
and then
from the room table show me roomNumber
and then
from the course table show me title where deptid = "cse"
and then
from the courseoffering table get ondays and starttime
and then
get no columns from the term table where year = 2021 and termperiod = "fall"
and then
order by title

--SpeakQl Query option 2a (Alternate between joins and selections and projections):
get buildingname and buildingnumber from the building table
and then
join the building table with the room table on room.buildingid = building.id
and then
get roomnumber from the room table
and then
join the room table with the courseoffering table on room.id = courseoffering.roomid
and then
get ondays and starttime from the courseoffering table
and then
join the courseoffering table with the term table on term.id = courseoffering.termid
and then
from term where year = 2021 and termperiod = "fall" display no columns
and then
join the course table with the courseoffering table on course.id = courseoffering.courseid
and then 
get title from the course table where deptid = "cse"
and then
order by title

--SpeakQl query option 2b (Less verbose, but same order)
get buildingname and buildingnumber from building
and then
join building with room on room.buildingid = building.id
and then
from table room get roomnumber
and then
join room with courseoffering on room.id = courseoffering.roomid
and then
from courseoffering show me ondays and starttime
and then
join courseoffering with term on term.id = courseoffering.termid
and then
display no columns from term where year = 2021 and termperiod = "fall"
and then
join course with courseoffering on course.id = courseoffering.courseid
and then
display title from course where deptid = "cse"
and then
order by title

--SpeakQl query option 3 (No joins, only where conditions)
get buildingname and buildingnumber from the building table
and then
get roomnumber from the room table where buildingid = building.id
and then
get ondays and starttime from the courseoffering table where roomid = room.id
and then
get no columns from the term table where year = 2021 and termperiod = "fall" and id = courseoffering.termid
and then
get title from course where deptid = "cse" and id = courseoffering.courseid
and then
order by title

--Translated SQL (option 1):
SELECT BUILDING.BUILDINGNAME, BUILDING.BUILDINGNUMBER, ROOM.ROOMNUMBER, COURSE.TITLE, COURSEOFFERING.ONDAYS, COURSEOFFERING.STARTTIME
FROM BUILDING
JOIN ROOM ON BUILDING.ID = ROOM.BUILDINGID 
JOIN COURSEOFFERING ON ROOM.ID = COURSEOFFERING.ROOMID 
JOIN TERM ON TERM.ID = COURSEOFFERING.TERMID 
JOIN COURSE ON COURSE.ID = COURSEOFFERING.COURSEID
WHERE(COURSE.DEPTID = "CSE") AND(TERM.YEAR = 2021 AND TERM.TERMPERIOD = "FALL") 
ORDER BY TITLE

--Translated SQL (option 2):
SELECT BUILDING.BUILDINGNAME, BUILDING.BUILDINGNUMBER, ROOM.ROOMNUMBER, COURSEOFFERING.ONDAYS, COURSEOFFERING.STARTTIME, COURSE.TITLE
FROM BUILDING
JOIN ROOM ON ROOM.BUILDINGID = BUILDING.ID 
JOIN COURSEOFFERING ON ROOM.ID = COURSEOFFERING.ROOMID 
JOIN TERM ON TERM.ID = COURSEOFFERING.TERMID 
JOIN COURSE ON COURSE.ID = COURSEOFFERING.COURSEID
WHERE(TERM.YEAR = 2021 AND TERM.TERMPERIOD = "FALL") AND(COURSE.DEPTID = "CSE") 
ORDER BY TITLE

--Translated SQL (option 3):
SELECT BUILDING.BUILDINGNAME, BUILDING.BUILDINGNUMBER, ROOM.ROOMNUMBER, COURSEOFFERING.ONDAYS, COURSEOFFERING.STARTTIME, COURSE.TITLE
FROM BUILDING, ROOM, COURSEOFFERING, TERM, COURSE
WHERE(ROOM.BUILDINGID = BUILDING.ID) 
    AND(COURSEOFFERING.ROOMID = ROOM.ID) 
    AND(TERM.YEAR = 2021 AND TERM.TERMPERIOD = "FALL" AND TERM.ID = COURSEOFFERING.TERMID) 
    AND(COURSE.DEPTID = "CSE" AND COURSE.ID = COURSEOFFERING.COURSEID) 
ORDER BY TITLE