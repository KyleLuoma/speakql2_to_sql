import db_connector
import mysql.connector


commands = []

# Department(deptId, departmentName)
department_table = """CREATE TABLE IF NOT EXISTS department (
                    id varchar(8) NOT NULL,
                    departmentName varchar(255),
                    primary key(id)
                    )"""

commands.append(department_table)

# Course(courseId, deptId, title, number, units)
course_table = """CREATE TABLE IF NOT EXISTS course (
                id varchar(16) NOT NULL,
                deptId int NOT NULL,
                title varchar(255),
                code varchar(8),
                units int,
                primary key(id)
                )"""

commands.append(course_table)

# CourseOffering(offeringId, courseId, termId, roomId, facultyName, onDays, startTime, endTime, capacity)
course_offering_table = """CREATE TABLE IF NOT EXISTS courseOffering (
                        id int NOT NULL AUTO_INCREMENT,
                        courseId varchar(16) NOT NULL,
                        termId varchar(16) NOT NULL,
                        roomId varchar(32) NOT NULL,
                        facultyName varchar(255),
                        onDays varchar(255),
                        startTime time(6),
                        endTime time(6),
                        capacity int,
                        primary key(id)
                        )"""

commands.append(course_offering_table)

# Term(termId, startDate, endDate, termPeriod, year)
term_table = """CREATE TABLE IF NOT EXISTS term (
             id varchar(16) NOT NULL,
             startDate date,
             endDate date,
             termPeriod varchar(16),
             year int,
             primary key(id)
             )"""

commands.append(term_table)

# Building(id, buildingNumber, buildingName)
building_table = """CREATE TABLE IF NOT EXISTS building (
                        id varchar(16) NOT NULL,
                        buildingNumber varchar(32),
                        buildingName varchar(255),
                        primary key(id)
                        )"""

commands.append(building_table)

#R Room(id, buildingId, roomNumber, floor, area, capacity, wheelchairSpaces)
room_table = """CREATE TABLE IF NOT EXISTS room (
                    id varchar(32) NOT NULL,
                    buildingId varchar(16) NOT NULL,
                    roomNumber varchar(16),
                    floor varchar(16),
                    area int,
                    capacity int,
                    wheelchairSpaces int,
                    primary key(id)
                    )"""

commands.append(room_table)

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