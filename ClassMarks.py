from os.path import exists as results_exist
import statistics

forename = 0
surname = 1
subject = 2
mark = 3
grade = 4

# Promt User to enter a class name.
classname = input("Please enter the Class name: ")
filename = classname + '.txt'
if results_exist(filename):
    # If it exists, read all entered records into program
    print("Retrieving existing file data")
    with open(filename) as f:
        all_records = f.readlines()
f = open(filename, 'a+') 

# Prompt user to select operation mode
user_mode = input("Please select mode. ENTRY or REPORT? ")
if user_mode.upper() == 'ENTRY':   
    entry_mode = True
    report_mode = False 
    print("\nYou have entered ENTRY mode")
    print("Enter students <FORENAME> <SURNAME> <SUBJECT> <MARK> - seperated by <SPACES>")
if user_mode.upper() == 'REPORT':
    report_mode = True
    entry_mode = False

while entry_mode:
    user_input = input("Enter Result: ")
    if user_input[0:4].upper() == 'EXIT':
        f.close()
        entry_mode = False
    else:
        new_record = user_input.replace(",","")
        new_record = new_record.split()
        write_record = new_record[forename] + ', ' + new_record[surname] + ', ' + new_record[subject] + ', ' + new_record[mark]
        f.write(write_record + '\n')        

while report_mode: 
    with open(classname + '.txt') as f:
        all_records = f.readlines()
        records = []
        for record in all_records:
            record = record.replace("\n","")   
            record = record.split(', ')
            if (int(record[mark]) >= 70): record.append('(A)')
            elif (int(record[mark]) >= 60) and (int(record[mark]) < 70): record.append('(B)')
            elif (int(record[mark]) >= 45) and (int(record[mark]) < 60): record.append('(C)')    
            elif (int(record[mark]) < 45): record.append('(F)') 
            records.append(record)
            
    report_type = input("Please select report. STUDENT or SUBJECT? ")
    if report_type.upper() == 'STUDENT':
        user_input = input("Enter Students name: ")
        student_name = user_input.split()        
        print("Results for:")
        print("\t", student_name[forename], student_name[surname], "\t", end="")
        r = 0
        while r < len(records):
            if (records[r][forename] == student_name[forename]) and (records[r][surname]) == student_name[surname]:
                print('[', records[r][subject],':',records[r][mark], records[r][grade], '] ', end="")
            r+=1
    if report_type.upper() == 'SUBJECT':
        user_input = input("Please select a subject. ALL MATHS ENGLISH SCIENCE ART? ")
        subject_report = user_input.upper()
        print("\n") 
        print(subject_report, "Exam Results Statistics:")
        marks_list = []
        pass_count = 0
        i = 0             
        if subject_report == 'ALL':
            while i < len(records):
                marks_list.append(int(records[i][mark]))
                if not(records[i][grade] == '(F)'):
                    pass_count+=1
                i+=1                   
        else:
            while i < len(records):
                if (records[i][subject].upper() == subject_report):
                    marks_list.append(int(records[i][mark]))
                    if not(records[i][grade] == '(F)'):
                        pass_count+=1
                i+=1                        
        print("min:", min(marks_list))
        print("max:", max(marks_list))
        print("mean:", statistics.mean(marks_list))
        print("median:", statistics.median(marks_list)) 
        print("Pass rate:", pass_count, '/', len(records))
    report_mode = False
