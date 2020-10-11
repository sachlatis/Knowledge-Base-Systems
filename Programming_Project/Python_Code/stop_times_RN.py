#!/usr/bin/env python3

import csv

stop_timesURI = "http://www.example.com/stop_times"

stop_times_has_trips = "http://www.example.com/stop_times_has_trips"
stop_times_has_stops = "http://www.example.com/stop_times_has_stops"

trip_idURI = "http://www.example.com/trips"
stop_idURI = "http://www.example.com/stops"


outputFileName = "stop_times_RN_OUT.txt"
outputFile = open(outputFileName, "w")

inputFileName = "stop_times.txt"

cnt = 0
with open(inputFileName) as infile:
  for line in infile:
    cnt = cnt + 1
    row = line.split(",")
    trip_id = row[0]
    stop_id = row[3]
    if cnt>1:
      outputFile.write('<http://www.example.com/trips/'+trip_id+'/stops/'+ stop_id +'> ' + '<'+ stop_times_has_trips +'>' +' <'+trip_idURI +'/'+trip_id+'>.'+'\n')
      outputFile.write('<http://www.example.com/trips/'+trip_id+'/stops/'+ stop_id +'> ' + '<'+ stop_times_has_stops +'>' +' <'+stop_idURI+'/'+stop_id+'>.'+'\n')


print(cnt)


