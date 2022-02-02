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

# Building(id, buildingNumber, buildingName)
building_table = """CREATE TABLE IF NOT EXISTS building (
                        id varchar(16) NOT NULL,
                        buildingNumber varchar(32),
                        buildingName varchar(255),
                        primary key(id)
                        )"""

commands.append(building_table)

#R Room(id, buildingId, roomNumber, floor, area, capacity, roomType, overflowCapable, floorType, 
#       seatingType, boards, acoustics, ventilation, windows, windowDarkenability, windowCoverings, 
#       lighting, lectern, instructorTables, clock, wheelchairSpaces)
room_table = """CREATE TABLE IF NOT EXISTS room (
                    id varchar(32) NOT NULL,
                    buildingId varchar(16) NOT NULL,
                    roomNumber varchar(16),
                    floor varchar(16),
                    area int,
                    capacity int,
                    roomType varchar(32),
                    overFlowCapable varchar(8),
                    floorType varchar(255),
                    seatingType varchar(255),
                    boards varchar(255),
                    acoustics varchar(255),
                    ventilation varchar(64),
                    windows varchar(32),
                    windowDarkenability varchar(64),
                    windowCoverings varchar(64),
                    lighting varchar(32),
                    lectern varchar(128),
                    instructorTables varchar(32),
                    clock varchar(32),
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