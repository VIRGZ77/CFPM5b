import os.path
from os import path
import statistics

forename = 0
surname = 1
subject = 2
mark = 3
grade = 4

def format_record_write(record):
    record = record.replace(",","") 
    record = record.split()
    return record[forename] + ', ' + record[surname] + ', ' + record[subject] + ', ' + record[mark] + '\n'

def format_record_read(record):
    record = record.replace("\n","")   
    record = record.split(', ')
    record.append(get_grade(record[mark]))   
    return record

def retrieve_records(filename):
    with open(filename) as f:
        all_records = f.readlines()
        records = []
        record = 0
        for record in all_records:
            records.append(format_record_read(record))
    return records

def get_grade(mark):
    if (int(mark) >= 70): return 'A'
    elif (int(mark) >= 60) and (int(mark) < 70): return 'B'
    elif (int(mark) >= 45) and (int(mark) < 60): return 'C'    
    elif (int(mark) < 45): return 'F'

def student_report(student_name):
    student_name = student_name.split()        
    print("Results for:")
    print("\t", student_name[forename], student_name[surname], "\t", end="")
    r = 0
    while r < len(records):
        if (records[r][forename] == student_name[forename]) and (records[r][surname]) == student_name[surname]:
            print('[', records[r][subject],':',records[r][mark], records[r][grade], '] ', end="")
        r+=1

def subject_report(subject_name):
    subject_name = subject_name.upper()
    print("\n") 
    marks_list = []
    pass_count = 0
    i = 0             
    if (subject_name == 'MATHS') or (subject_name == 'ENGLISH') or (subject_name == 'SCIENCE') or (subject_name == 'ART'):
        print(subject_name, "Exam Results Statistics:")
        while i < len(records):
            if (records[i][subject].upper() == subject_name):
                marks_list.append(int(records[i][mark]))
                if not(records[i][grade] == '(F)'):
                    pass_count+=1
            i+=1     
    else: 
        print("ALL Exam Results Statistics:")
        while i < len(records):
            marks_list.append(int(records[i][mark]))
            if not(records[i][grade] == '(F)'):
                pass_count+=1
            i+=1                       
    print("min:", min(marks_list))
    print("max:", max(marks_list))
    print("mean:", statistics.mean(marks_list))
    print("median:", statistics.median(marks_list)) 
    print("Pass rate:", pass_count, '/', len(records))

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
    if user_mode.upper() == 'ENTRY':   
        entry_mode = True
        report_mode = False 
    if user_mode.upper() == 'REPORT':
        report_mode = True
        entry_mode = False
else:
    entry_mode = True
    report_mode = False

while entry_mode:
    print("Enter students <FORENAME> <SURNAME> <SUBJECT> <MARK> - seperated by <SPACES>")
    user_input = input("Enter Result: ")
    
    if user_input[0:4].upper() == 'EXIT':
        f.close()
        entry_mode = False
    else:
        f.write(format_record_write(user_input))

while report_mode: 
    records = retrieve_records(filename)
    
    report_type = input("Please select report. STUDENT or SUBJECT? ")
    
    if report_type.upper() == 'STUDENT':
        user_input = input("Enter Students name: ")
        student_report(user_input)
        
    if report_type.upper() == 'SUBJECT':
        user_input = input("Please select a subject. ALL MATHS ENGLISH SCIENCE ART? ")
        subject_report(user_input)
        
    report_mode = False
