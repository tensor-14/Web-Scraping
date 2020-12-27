from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find('h5')  #Searches for the first h5 tag only
    courses_html_tags = soup.find_all('h5')  #Searches for all the h5 tags
    for course in courses_html_tags:
        print(course.text)

    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]    #accessing the last element
        print(f'{course_name} costs {course_price}')
