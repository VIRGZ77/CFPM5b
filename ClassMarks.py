import os.path
from os import path
import statistics
import json
import pickle

forename = 0
surname = 1
subject = 2
mark = 3
grade = 4

def entry_check(user_input):
    """ Ensures that record entry string has 4 distinct parts seperated by SPACES
        and that the 4th part is only number characters"""
    space = 0
    posn = 0
    for c in user_input:
        posn+=1
        if c.isspace():
            space+=1
            position = posn
    if space == 3:
        for n in user_input[position:]:
            if not(n.isdigit()):
                print("ERROR: MARK portion contains non numeric characters") 
                return False
        return True
    else:
        print("ERROR: Entry does not contain 4 parts e.g., Joe Bloggs Maths 99") 
        return False  

def format_record_write(record):
    """ Formats the entererd record string to remove any COMMAS and then splits it into a word list"""
    record = record.replace(",","") 
    record = record.split()
    return record[forename] + ', ' + record[surname] + ', ' + record[subject] + ', ' + record[mark] + '\n'

def format_record_read(record):
    """ Formats the read record string to remove trailing NEW LINE (\n) and the splits using COMMA SPACE (, )
        as a separator.  Then a Alphanumeric GRADE is appended depending upon the MARK"""
    record = record.replace("\n","")   
    record = record.split(', ')
    record.append(get_grade(record[mark]))   
    return record

def get_grade(mark):
    """ Determine GRADE upon specificied MARK"""
    if (int(mark) >= 70): return 'A'
    elif (int(mark) >= 60) and (int(mark) < 70): return 'B'
    elif (int(mark) >= 45) and (int(mark) < 60): return 'C'    
    elif (int(mark) < 45): return 'F'

def retrieve_records(filename):
    """ Read all records from an existing file"""
    with open(filename) as f:
        all_records = f.readlines()
        records = []
        record = 0
        for record in all_records:
            records.append(format_record_read(record))
    return records

def student_list(records):
    """ Creates a SET of student fullnames """
    n = 0
    fullname_list = []
    while n < len(records):
        fullname = records[n][forename]+" "+records[n][surname]
        fullname_list.append(fullname)  
        n+=1
    students =set(fullname_list)
    return students

def student_report(student_name):
    """ Return either a report for the user specified FORENAME SURNAME string provided, or a report for 
    ALL students"""
    if student_name:
        student_name = student_name.split()        
        print("\n", student_name[forename], student_name[surname], "\t", end="")
        r = 0
        report = {}
        report["Forename"] = student_name[forename]
        report["Surname"] = student_name[surname]
        while r < len(records):
            if (records[r][forename] == student_name[forename]) and (records[r][surname]) == student_name[surname]:
                print('[', records[r][subject],':',records[r][mark], records[r][grade], '] ', end="")
                report[records[r][subject]] = records[r][mark] + ' (' + records[r][grade] + ')'
            r+=1
        return report
    
def students_report(records):
    report = ""
    students = student_list(records)
    for individual in students:
        report = report + str(student_report(individual))
        #student_report("Alan Virgo")
        #student_report("Isaac Clarke")
    
    return report    


def subject_report(subject_name):
    """ Returns either a report for the user specified SUBJECT should it exist in the records, or a report for 
        ALL records"""
    subject_name = subject_name.upper()
    print("\n") 
    marks_list = []
    pass_count = 0
    fail_count = 0
    i = 0             
    if (subject_name == 'MATHS') or (subject_name == 'ENGLISH') or (subject_name == 'SCIENCE') or (subject_name == 'ART'):
        report_title = subject_name
        while i < len(records):
            if (records[i][subject].upper() == subject_name):
                marks_list.append(int(records[i][mark]))
                if not(records[i][grade] == 'F'):
                    pass_count+=1
                else:
                    fail_count+=1       
            i+=1     
    else: 
        report_title = 'ALL'
        while i < len(records):
            marks_list.append(int(records[i][mark]))
            if not(records[i][grade] == 'F'):
                pass_count+=1
            else:
                fail_count+=1
            i+=1   
    print(report_title, "Exam Results Statistics:")
    print("min:", min(marks_list))
    print("max:", max(marks_list))
    print("mean:", statistics.mean(marks_list))
    print("median:", statistics.median(marks_list)) 
    print("Passed:", pass_count)
    print("Failed:", fail_count)
    
    report = {}
    report["Subject"] = report_title
    report["Min"] = min(marks_list)
    report["Max"] = max(marks_list)
    report["Mean"] = statistics.mean(marks_list)
    report["Median"] = statistics.median(marks_list)
    report["Passed"] = pass_count
    report["Failed"] = fail_count
    return report    

def json_export(report):
    """ Export JSON formatted data for passed variable. Reads back to provide user confirmation"""
    # Write json file
    with open("report.json", "w") as f:
        json.dump(report, f)  
    # Read json file
    f = open("report.json")
    print("\n")
    print(json.load(f))
    print("'report.json' file created.")

def pickle_export(report):
    """ Export Pickle formatted data for passed variable.  Reads back to provided user confirmation"""
    # Write pickle file
    with open("report.pickle", "wb") as f:
        pickle.dump(report, f) 
    # Read pickle file
    f = open("report.pickle", "rb")
    print("\n")
    print(pickle.load(f))
    print("'report.pickle' file created.")
    
# Prompt User to enter a class name.
classname = input("Please enter the Class name: ")
filename = classname + '.txt'
file_exists = False
if path.exists(filename):
    file_exists = True
    # If it exists, read all entered records into program
    with open(filename) as f:
        print("Retrieving records...")
        all_records = f.readlines()
f = open(filename, 'a+') 

# Prompt user to select operation mode if file exists else start entry mode
if file_exists:
    user_mode = input("Please select mode. ENTRY or REPORT? ")
    while not((user_mode.upper() == 'ENTRY') or (user_mode.upper() == 'REPORT')):
        user_mode = input("Please select mode. ENTRY or REPORT? ")
    if user_mode.upper() == 'ENTRY':   
        entry_mode = True
        report_mode = False 
        print("Enter students <FORENAME> <SURNAME> <SUBJECT> <MARK> - seperated by <SPACES>")
    if user_mode.upper() == 'REPORT':
        report_mode = True
        entry_mode = False
else:
    entry_mode = True
    report_mode = False
    print("Enter students <FORENAME> <SURNAME> <SUBJECT> <MARK> - seperated by <SPACES>")

while entry_mode:
    user_input = input("Enter Result: ")  
    if user_input[0:4].upper() == 'EXIT':
        f.close()
        entry_mode = False
    elif entry_check(user_input):
        f.write(format_record_write(user_input))
    else:
        print("Invalid Entry!")
    
    
while report_mode: 
    records = retrieve_records(filename)
    
    report_type = input("Please select report. STUDENT or SUBJECT? ")
    while not((report_type.upper() == 'STUDENT') or (report_type.upper() == 'SUBJECT')):
        report_type = input("Please select report. STUDENT or SUBJECT? ")
        user_mode = user_mode.upper()
    
    if report_type.upper() == 'STUDENT':
        user_input = input("Enter Students name: ")
        if user_input:
            report = student_report(user_input)
        else:
            report = students_report(records)
        
    if report_type.upper() == 'SUBJECT':
        user_input = input("Please select a subject. ALL MATHS ENGLISH SCIENCE ART? ")
        report = subject_report(user_input)
    
    user_input = input("\nPress 'J' to export data to data.json or 'P' to export to data.pickle or 'Q' to quit: ")
    while not((user_input.upper() == 'J') or (user_input.upper() == 'P') or (user_input.upper() == 'Q')):
        user_input = input("\nPress 'J' to export data to data.json or 'P' to export to data.pickle or 'Q' to quit: ")
        
    if user_input.upper() == 'J':
        json_export(report)

    elif user_input.upper() == 'P':
        pickle_export(report)
    else:
        print("Good Bye!")
    report_mode = False
