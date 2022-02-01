import db_connector
import mysql.connector


commands = []

# Department(deptId, departmentName)
department_table = """CREATE TABLE IF NOT EXISTS department (
                    id int NOT NULL AUTO_INCREMENT,
                    departmentName varchar(255),
                    primary key(id)
                    )"""

commands.append(department_table)

# Course(courseId, deptId, title, number, units)
course_table = """CREATE TABLE IF NOT EXISTS course (
                id int NOT NULL AUTO_INCREMENT,
                deptId int NOT NULL,
                title varchar(255),
                number int,
                units int,
                primary key(id)
                )"""

commands.append(course_table)

# CourseOffering(offeringId, courseId, termId, facultyName, locationId, roomNumber, onDays, startTime, endTime, capacity)
course_offering_table = """CREATE TABLE IF NOT EXISTS courseOffering (
                        id int NOT NULL AUTO_INCREMENT,
                        courseId int NOT NULL,
                        termId int NOT NULL,
                        locationId int NOT NULL,
                        facultyName varchar(255),
                        roomNumber varchar(255),
                        onDays varchar(255),
                        startTime time(6),
                        endTime time(6),
                        capacity int,
                        primary key(id)
                        )"""

commands.append(course_offering_table)

# Term(termId, startDate, endDate, termPeriod)
term_table = """CREATE TABLE IF NOT EXISTS term (
             id int NOT NULL AUTO_INCREMENT,
             startDate date,
             endDate date,
             termPeriod varchar(12),
             primary key(id)
             )"""

commands.append(term_table)

# Location(locationId, buildingNumber, buildingName)
course_location_table = """CREATE TABLE IF NOT EXISTS courseLocation (
                        id int NOT NULL AUTO_INCREMENT,
                        buildingNumber varchar(32),
                        buildingName varchar(255),
                        primary key(id)
                        )"""

commands.append(course_location_table)


for command in commands:
    try:
        cnx = db_connector.get_speakql_university_connector()
        cursor = cnx.cursor()
        result = cursor.execute(command)
        print("Table created successfully ")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")