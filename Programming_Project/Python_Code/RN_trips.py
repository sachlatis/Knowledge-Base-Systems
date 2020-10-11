#!/usr/bin/env python3

import csv

trip_idURI = "http://www.example.com/trips"

trips_has_routes = "http://www.example.com/trips_has_routes"
trips_has_calendar = "http://www.example.com/trips_has_calendar"

routesURI = "http://www.example.com/routes"
calendarURI = "http://www.example.com/calendar"

outputFileName = "trips_RN_OUT.txt"
outputFile = open(outputFileName, "w")

inputFileName = "trips.txt"

cnt = 0
with open(inputFileName) as infile:
  for line in infile:
    cnt = cnt + 1
    row = line.split(",")

    rout_id = row[0]
    service_id = row[1]
    trip_id = row[2]

    if cnt>1:
      outputFile.write('<'+trip_idURI +'/'+trip_id+'> '+'<'+ trips_has_routes +'>' +' <'+routesURI +'/'+rout_id+'>.'+'\n')
      outputFile.write('<'+trip_idURI +'/'+trip_id+'> '+'<'+ trips_has_calendar +'>' +' <'+calendarURI +'/'+service_id+'>.'+'\n')


print(cnt)



