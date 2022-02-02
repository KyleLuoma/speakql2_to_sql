import requests
import pandas

URL = "https://catalog.ucsd.edu/front/courses.html"
page = requests.get(URL)

course_links = []
dept_ref_frag = '<a href="../courses/'
courses_text = page.text
cursor = 0
text_to_check = courses_text[cursor : len(courses_text)]

while dept_ref_frag in text_to_check:
    next_link_start = text_to_check.find(dept_ref_frag) + len('<a href="..')
    next_link_end = text_to_check.find('"', next_link_start)
    course_links.append(text_to_check[next_link_start : next_link_end])
    text_to_check = text_to_check[next_link_end : ]
    
courses = pandas.DataFrame()
course_ref_frag = '<p class="anchor-parent"><a class="anchor" id="'
course_ids = []
course_names = []
course_descriptions = []
for link in course_links:
    print(link)
    course_page_url = "https://catalog.ucsd.edu" + link 
    course_page = requests.get(course_page_url)
    #print(course_page.text)
    text_to_check = course_page.text
    while course_ref_frag in text_to_check:
        id_start = text_to_check.find(course_ref_frag) + len(course_ref_frag)
        id_end = text_to_check.find('"', id_start)
        id = text_to_check[id_start : id_end]
        course_ids.append(id)

        course_name_start = text_to_check.find('<p class="course-name">', id_end) + len('<p class="course-name">')
        course_name_end = text_to_check.find('</p>', course_name_start)
        course_name = text_to_check[course_name_start : course_name_end]
        course_names.append(course_name)

        course_description_start = text_to_check.find('<p class="course-descriptions">', course_name_end) + len('<p class="course-descriptions">')
        course_description_end = text_to_check.find('</p>', course_description_start)
        course_description = text_to_check[course_description_start : course_description_end]
        course_descriptions.append(course_description)

        text_to_check = text_to_check[course_description_end : ]
        #print(id, course_name, course_description)

courses["id"] = pandas.Series(course_ids)
courses["course_names"] = pandas.Series(course_names)
courses["course_descriptions"] = pandas.Series(course_descriptions)

courses.to_csv("./courses.csv", sep = "|")
#courses.to_excel("./courses.xlsx")