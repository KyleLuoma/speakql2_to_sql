import pandas
import db_connector as db
import mysql.connector
import xml.etree.ElementTree as ET
import random

db_connector = db.DbConnector()

def insert_course_values():
    courses = pandas.read_csv("./app/src/db_util/data/data/courses.csv", sep = "|")
    print(courses.iloc[0].id, courses.iloc[0].course_names)

    courses["units"] = courses.apply(
        lambda row: row.course_names[row.course_names.find(")") - 2 : row.course_names.find(")")].strip().replace("(", ""), 
        axis = 1)
    print(courses.units.head())

    courses["department"] = courses.apply(
        lambda row: row.course_names.split()[0],
        axis = 1
    )
    print(courses.department.head())

    courses["code"] = courses.apply(
        lambda row: row.course_names.split()[1].replace(".", ""),
        axis = 1
    )
    print(courses.code.head())

    courses["title"] = courses.apply(
        lambda row: row.course_names[
            row.course_names.find(". ") + 2 :
            row.course_names.find(" (")
        ].strip(),
        axis = 1
    )
    print(courses.title.head())

    insert_course_query = """INSERT INTO speakql_university.course (id, deptId, title, code, units) 
                                                            VALUES('{}', '{}', '{}', '{}', '{}')"""
    cnx = db_connector.get_speakql_university_connector()
    cursor = cnx.cursor()

    for row in courses.itertuples():
        command = insert_course_query.format(
            row.id,
            row.department,
            row.title,
            row.code,
            row.units
        )
        try:
            result = cursor.execute(command)
            cnx.commit()
            print("Query", command, "Executed")

        except mysql.connector.Error as error:
            print("Failed to DO SOMETHING in MySQL: {}".format(error))

    if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")



def insert_location_values():
    insert_location_query = """INSERT INTO speakql_university.building (id, buildingNumber, buildingName)
                                                                  VALUES ('{}', '{}', '{}')"""
    classrooms = pandas.read_excel("./app/src/db_util/data/data/classroom data.xlsx")
    
    building_number_list = []
    for row in classrooms.drop_duplicates(subset = ["Building Name"]).itertuples():
        print("Inserting location", row[1])
        code = row[3].split()[0].strip()
        building_number = random.randint(100, 8000)
        while building_number in building_number_list:
            building_number = random.randint(100, 8000)
        building_number_list.append(building_number)

        command = insert_location_query.format(
            code,
            building_number, 
            row[1]
        )

        try:
            cnx = db_connector.get_speakql_university_connector()
            cursor = cnx.cursor()
            print("Running query", command)
            result = cursor.execute(command)
            cnx.commit()
            print("Query", command, "Executed")

        except mysql.connector.Error as error:
            print("Failed to DO SOMETHING in MySQL: {}".format(error))
        
    if cnx.is_connected():
        cursor.close()
        cnx.close()
        print("MySQL connection is closed")


#R Room(id, buildingId, roomNumber, floor, area, capacity, wheelchairSpaces)

def insert_room_values():
    insert_room_query = """INSERT INTO speakql_university.room (id, buildingId, roomNumber, floor, area, 
                            capacity, wheelchairSpaces)
                        VALUES ('{}', '{}', '{}', '{}', {}, {}, {})"""
    
    classrooms = pandas.read_excel("./app/src/db_util/data/data/classroom data.xlsx")

    for row in classrooms.itertuples():
        id = row[3]
        building_id = row[3].split()[0].strip()
        room_number = row[2]
        floor = row[4]
        area = int(row[5])
        capacity = int(row[6])
        wheelchair_spaces = int(row[26])

        command = insert_room_query.format(
            id, building_id, room_number, floor, area, capacity, wheelchair_spaces
        )

        try:
            cnx = db_connector.get_speakql_university_connector()
            cursor = cnx.cursor()
            #print("Running query", command)
            result = cursor.execute(command)
            cnx.commit()
            #print("Query", command, "Executed")

        except mysql.connector.Error as error:
            print("Failed to run query {} in MySQL: {}".format(command, error))
        
    if cnx.is_connected():
        cursor.close()
        cnx.close()
        print("MySQL connection is closed")



# Term(termId, startDate, endDate, termPeriod, year)
def insert_term_values():
    insert_term_query = """INSERT INTO speakql_university.term (id, startDate, endDate, termPeriod, year)
                                                                  VALUES ('{}', '{}', '{}', '{}', {})"""
    terms = pandas.read_csv("./app/src/db_util/data/data/university_data - terms.csv")
    print(terms.head())
    for row in terms.itertuples():
        command = insert_term_query.format(
            row[1],
            row[2],
            row[3],
            row[4],
            int(row[5])
        )
        try:
            cnx = db_connector.get_speakql_university_connector()
            cursor = cnx.cursor()
            result = cursor.execute(command)
            cnx.commit()

        except mysql.connector.Error as error:
            print("Failed to execute query {} in MySQL: {}".format(command, error))
        
    if cnx.is_connected():
        cursor.close()
        cnx.close()
        print("MySQL connection is closed")



def insert_department_values():
    tree = ET.parse('./app/src/db_util/data/data/ucsd_departments.xml')
    root = tree.getroot()
    insert_department_query = "INSERT INTO speakql_university.department (id, departmentName) VALUES('{}', '{}')"

    for child in root:
        print(child.text, child.attrib["value"])
        command = insert_department_query.format(child.attrib["value"].strip(), child.text.strip())
        try:
            cnx = db_connector.get_speakql_university_connector()
            cursor = cnx.cursor()
            result = cursor.execute(command)
            cnx.commit()
            print("Query", command, "Executed")

        except mysql.connector.Error as error:
            print("Failed to DO SOMETHING in MySQL: {}".format(error))
        
    if cnx.is_connected():
        cursor.close()
        cnx.close()
        print("MySQL connection is closed")


# CourseOffering(offeringId, courseId, termId, roomId, facultyName, onDays, startTime, endTime, capacity)
def insert_course_offering_values():
    try:
        cnx = db_connector.get_speakql_university_connector()
        cursor = cnx.cursor(buffered=True, dictionary=True)
        
        cursor.execute("SELECT * FROM speakql_university.term;")
        term_ids = []
        for (tuple) in cursor:
            term_ids.append(tuple["id"])

        cursor.execute("SELECT * FROM speakql_university.course;")
        course_ids = []
        for (tuple) in cursor:
            course_ids.append(tuple["id"])

        cursor.execute("SELECT * from speakql_university.room;")
        room_ids = []
        room_capacities = {}
        for (tuple) in cursor:
            room_ids.append(tuple["id"])
            room_capacities[tuple["id"]] = tuple["capacity"]

        print(len(term_ids))
        print(len(course_ids))
        print(len(room_ids))

        on_day_list = ["MonWed", "TueThu"]
        start_time_end_time_list = [
            ["08:00:00", "09:50:00"],
            ["10:00:00", "11:50:00"],
            ["12:00:00", "13:50:00"],
            ["14:00:00", "15:50:00"],
            ["16:00:00", "17:50:00"],
            ["18:00:00", "19:50:00"]
        ]
    except mysql.connector.Error as error:
        print("Failed to DO SOMETHING in MySQL: {}".format(error))

    mock_names = pandas.read_csv("./app/src/db_util/data/data/MOCK_NAMES.csv")

    try:
        course_offerings = []

        for term in term_ids:
            for room in room_ids:
                course_offering = {}
                for i in range(0, len(start_time_end_time_list)):
                    for j in range(0, len(on_day_list)):
                        course_offering["courseId"] = course_ids[random.randint(0, len(course_ids) - 1)]
                        course_offering["termId"] = term
                        course_offering["roomId"] = room
                        course_offering["startTime"] = start_time_end_time_list[i][0]
                        course_offering["endTime"] = start_time_end_time_list[i][1]
                        course_offering["onDays"] = on_day_list[j]
                        course_offering["capacity"] = random.randint(int(room_capacities[room] / 2), int(room_capacities[room]))
                        rand_name_ix = random.randint(0, 99)
                        course_offering["facultyName"] = mock_names.iloc[rand_name_ix].first_name + " " + mock_names.iloc[rand_name_ix].last_name

                        command = """INSERT INTO speakql_university.courseOffering (courseId, termId, roomId, facultyName, onDays, 
                                     startTime, endTime, capacity) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', {})"""

                        command = command.format(
                            course_offering["courseId"],
                            course_offering["termId"],
                            course_offering["roomId"],
                            course_offering["facultyName"],
                            course_offering["onDays"],
                            course_offering["startTime"],
                            course_offering["endTime"],
                            course_offering["capacity"]
                        )
                        cursor.execute(command)
                        cnx.commit()


    except mysql.connector.Error as error:
        print("Failed {} in MySQL: {}".format(command, error))

    cursor.close()
    cnx.close()    

#insert_term_values()
#insert_location_values()
#insert_department_values()
#insert_course_values()
#insert_room_values()
insert_course_offering_values()