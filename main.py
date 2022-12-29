# page request: https://jonathansoma.com/lede/foundations-2018/classes/apis/multiple-pages-of-data-from-apis/

# api pagination canvas https://canvas.instructure.com/doc/api/file.pagination.html

import requests
import time
import configparser
import datetime
from datetime import date
from requests.auth import HTTPBasicAuth
import json  # might be unnecessary
import pprint

# Notes:
# Courses link:
# "https://canvas.instructure.com/api/v1/courses?access_token="
# Assignments link for college success strategies
# "https://canvas.instructure.com/api/v1/courses/56470000000015120/assignments?access_token="


courseId = str(56470000000015120)

# Access token
access_token = "5647~6sxmke1PdjSLbsrwcgMIVk8XeBnKXdOtlvrgpix1SyDYqO0BxosvaMzV8iuCOuWN"

# Class link
url = "https://canvas.instructure.com/api/v1/courses?per_page=1000;access_token="
# Class request
classRequest = requests.get(url + access_token)


def assignmentsRequestFunc(courseId):
    url2 = "https://canvas.instructure.com/api/v1/courses/" + courseId + "/assignments?per_page=1000;access_token="
    # assignments request
    assignmentsRequest = requests.get(url2 + access_token)
    return assignmentsRequest


# course request
coursesRequest = requests.get(url + access_token)


# seperator
def seperator():
    print("#######################")

def assignmentUploader():
    today = str(date.today())  # gets today's date
    today_list = [int(today[0:4]), int(today[5:7]), int(today[8:10]),
                  today[8:10]]  # makes today into a list of year, month, day
    for x in classRequest.json():
        ticker = 0 # delete me
        if ticker == 0: # delete me
            print(x["end_at"])  # delete me
            ticker += 1 # delete me
        if type(x["end_at"]) != type(None):
            end_atList = [int(x["end_at"][0:4]), int(x["end_at"][5:7]), int(x["end_at"][8:10])]
            if today_list[0] >= end_atList[0] and today_list[1] >= end_atList[1] and today_list[2] >= end_atList[2]:
                print("HORAY")
                # So, I left off here, trying to get the horay to trigger when the end of the class was later
                # than the current date, but I couldnt get it to proc. I did reverse the sign and it always proc'ed
                # ensure that the comparison is accurate and that your current class does in fact show up on the api call
assignmentUploader()




class courses:
    def __init__(self, name, id, start_at, end_at, current_status):
        self.name = str(name)
        self.id = int(id)
        self.start_at = str(start_at)
        self.end_at = str(end_at)
        self.current_status = current_status
        start_at_list = [start_at[0:4], start_at[5:7], start_at[8:10]]

    def currentCourse(end_at):
        today = str(date.today())  # gets today's date
        today_list = [today[0:4], today[5:7], today[5:7],
                      today[8:10]]  # makes today into a list of year?, month?, day?
        if end_at != None:  # if the end at value is none then...
            end_at_list = [end_at[0:4], end_at[5:7],
                           end_at[8:10]]  # turn the end at list into the same comparable list as the day
            if today_list[0] < end_at_list[0]:
                if today_list[1] < end_at_list[1]:
                    if today_list[2] < end_at_list[2]:
                        current_status = "True"
                        return current_status  # return current status as true if method is called to say that this is good to go to pull the assignments from, if not then it returns false, just like with the line 4 lines up and the proceeding.
                    else:
                        current_status = "False"
                        return current_status
                else:
                    current_status = "False"
                    return current_status
            else:
                current_status = "False"
                return current_status
        else:
            current_status = "False"
            return current_status  #


def coursePopulator():
    for x in classRequest.json():
        r = courses.currentCourse(x["end_at"])
        test = courses(x["name"], x["id"], x["start_at"], x["end_at"], r)
        print(test.name)
        print(test.current_status)



# coursePopulator()


# print(date.today())
# print("#######################")
# for t in coursesRequest.json():
#   print(t["name"])
#   print(t["id"])
# print("#######################")
# The proceeding for loop is to do 2 things, loop through the list that the json file comes in and so as to isolate one singular class
# n = 0
# list = []
# for x in coursesRequest.json():
#   list.append(n)
#   if n < 1:
#     list2 = x
#   else:
#     pass
#   n += 1
#   print (x)
# print(list)
# print("#######################")
# print(list2)
# print("#######################")
# print(list2["id"])
# print("#######################")

# print(assignmentsRequest.text)
# b = 0
# assignmentList = []
# for r in assignmentsRequest.json():
#   assignmentList.append(b)
#   if b < 1:
#     assignmentlist2 = r
#   else:
#     pass
#   b += 1
#   print (r)
# print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print (assignmentlist2["has_submitted_submissions"])
# print("#######################")
# print (assignmentlist2["lock_at"])
# print("#######################")
# print(assignmentList)
# print("#######################")
# print(assignmentlist2)
# print("#######################")
# print(list2["id"])
# print("#######################")


def get_new_assignments():
    courses = requests.get(url + access_token)  # courses
    abridged_courses = courses.text[1:-1]
    # json_text_file = open("jsontext.json", "w")
    # json_text_file.write(courses.text)
    # json_text_file.close()
    # abridged_courses = "{" + abridged_courses + "}"
    print(type(courses.text))
    data = json.loads(courses.text)
    print(type(data))
    print(courses.text[0])
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    pprint.pprint(data)  # pprint prints it in an easier to read format


# get_new_assignments()


# TODO: For loop throught the courses
# Get the id of the course
# Make a request to get assiments for that particular course
# Figure out the newest data

# dead honest, I stole this little bit of code. it was helpful though
def run_schedule():
    while True:
        now = datetime.datetime.now()
        target = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=2, minute=0))

        if target < now:
            target += datetime.timedelta(days=1)
        time.sleep((target - now).total_seconds())
        # do something
        print("test")


def main():
    run_schedule()


if __name__ == '__main__':
    main()