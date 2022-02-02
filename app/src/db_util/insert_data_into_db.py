import pandas
import db_connector
import mysql.connector
import xml.etree.ElementTree as ET
import random

def insert_course_values():
    courses = pandas.read_csv("./app/src/db_util/courses.csv", sep = "|")
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
    classrooms = pandas.read_excel("./app/src/db_util/classroom data.xlsx")
    
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

#insert_location_values()

#R Room(id, buildingId, roomNumber, floor, area, capacity, roomType, overflowCapable, floorType, 
#       seatingType, boards, acoustics, ventilation, windows, windowDarkenability, windowCoverings, 
#       lighting, lectern, instructorTables, clock, wheelchairSpaces)

def insert_room_values():
    insert_room_query = """INSERT INTO speakql_university.room (id, buildingId, roomNumber, floor, area, 
                            capacity, roomType, overflowCapable, floorType, seatingType, boards, acoustics, 
                            ventilation, windows, windowDarkenability, windowCoverings,
                            lighting, lectern, instructorTables, clock, wheelchairSpaces)
                        VALUES ('{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{}', '{}', '{}', '{}', 
                            '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})"""
    
    classrooms = pandas.read_excel("./app/src/db_util/classroom data.xlsx")

    for row in classrooms.itertuples():
        id = row[3]
        building_id = row[3].split()[0].strip()
        room_number = row[2]
        floor = row[4]
        area = int(row[5])
        capacity = int(row[6])
        room_type = row[7]
        overflow_capable = row[10]
        floor_type = row[11]
        seating_type = row[12]
        boards = str(row[15]).replace("'", "")
        acoustics = row[17]
        ventilation = row[18]
        windows = row[19]
        window_darkenability = row[20]
        window_coverings = row[21]
        lighting = row[22]
        lectern = row[23]
        instructor_tables = row[24]
        clock = row[25]
        wheelchair_spaces = int(row[26])

        command = insert_room_query.format(
            id, building_id, room_number, floor, area, capacity, room_type, overflow_capable, floor_type,
            seating_type, boards, acoustics, ventilation, windows, window_darkenability, window_coverings, lighting,
            lectern, instructor_tables, clock, wheelchair_spaces
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

insert_room_values()

def insert_department_values():
    tree = ET.parse('./app/src/db_util/ucsd_departments.xml')
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