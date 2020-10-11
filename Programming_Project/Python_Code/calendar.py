#!/usr/bin/env python3
import csv
calendarURI = "http://www.example.com/calendar"
mondayURI = "http://www.example.com/monday"
tuesdayURI = "http://www.example.com/tuesday"
wednesdayURI = "http://www.example.com/wednesday"
thursdayURI = "http://www.example.com/thursday"
fridayURI = "http://www.example.com/friday"
saturdayURI = "http://www.example.com/saturday"
sundayURI = "http://www.example.com/sunday"
start_dateURI = "http://www.example.com/start_date"
end_dateURI = "http://www.example.com/end_date"
string_ = "^^xsd:string."
integer_ = "^^xsd:int."
boolean_ = "^^xsd:boolean."
date_ = "^^xsd:date."
outputFileName = "calendarOUTNEW.txt"
outputFile = open(outputFileName, "w")
inputFileName = "calendar.txt"
cnt = 0
with open(inputFileName) as infile:
  for line in infile:
    cnt = cnt + 1
    row = line.split(",")
    service_id = row[0]
    monday = row[1]
    tuesday = row[2]
    wednesday = row[3]
    thursday = row[4]
    friday = row[5]
    saturday = row[6]
    sunday = row[7]
    s = row[8]
    f = row[9]
    start_day_final = str(s[0:4]+'-'+ s[4:6]+'-'+s[6:8])
    end_date_final = str(f[0:4]+'-'+ f[4:6]+'-'+f[6:8])
    if cnt>1:
      outputFile.write('<'+calendarURI+'/'+service_id+'> ' + 'a' + ' <' + calendarURI+'>'+'.''\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ mondayURI +'>' +' "' + str(monday)+ '"' + boolean_ +'\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ tuesdayURI +'>' + ' "' + str(tuesday)+ '"' + boolean_ +'\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ wednesdayURI +'>' + ' "' + str(wednesday)+ '"' + boolean_ +'\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ thursdayURI +'>' + ' "' + str(thursday)+ '"' + boolean_ +'\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ fridayURI +'>' + ' "' + str(friday)+ '"' + boolean_ +'\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ saturdayURI +'>' + ' "' + str(saturday)+ '"' + boolean_ +'\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ sundayURI +'>' + ' "' + str(sunday)+ '"' + boolean_ +'\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ start_dateURI +'>' + ' "' + str(start_day_final)+ '"' + date_ +'\n')
      outputFile.write('<'+calendarURI+'/'+service_id+'> '+'<'+ end_dateURI +'>' + ' "' + str(end_date_final)+ '"' + date_+'\n')

print(cnt)


