#!/usr/bin/env python3

import csv

stop_timesURI = "http://www.example.com/stop_times"
tripURI = "http://www.example.com/trip_id"
arrival_timeURI = "http://www.example.com/arrival_time"
departure_timeURI = "http://www.example.com/departure_time"
stop_idURI = "http://www.example.com/stop_id"
stop_sequenceURI = "http://www.example.com/stop_sequence"
pickup_typeURI = "http://www.example.com/pickup_type"
drop_off_typeURI = "http://www.example.com/drop_off_type"

string_ = "^^xsd:string."
integer_ = "^^xsd:int."
time_ = "^^xsd:dateTime."

outputFileName = "stop_timesOUT.txt"
outputFile = open(outputFileName, "w")

inputFileName = "stop_times.txt"

cnt = 0
with open(inputFileName) as infile:
  for line in infile:
    cnt = cnt + 1
    row = line.split(",")
    trip_id = row[0]
    arrival_time = row[1]
    departure_time = row[2]
    stop_id = row[3]
    stop_sequence = row[4]
    pickup_type = row[5]
    drop_off_type = row[6]
    if cnt>1:
      outputFile.write('<http://www.example.com/trips/'+trip_id+'/stops/'+ stop_id +'> '  + 'a' + ' <'+stop_timesURI +'>'+'.''\n')
      outputFile.write('<http://www.example.com/trips/'+trip_id+'/stops/'+ stop_id +'> ' + '<'+ arrival_timeURI +'>' +' "' + str(arrival_time)+ '"' + time_ +'\n')
      outputFile.write('<http://www.example.com/trips/'+trip_id+'/stops/'+ stop_id +'> ' + '<'+ departure_timeURI +'>'+' "' + str(departure_time)+ '"' + time_ +'\n')
      outputFile.write('<http://www.example.com/trips/'+trip_id+'/stops/'+ stop_id + '> ' + '<'+ stop_sequenceURI +'>' + ' "' + str(stop_sequence)+ '"' + integer_ +'\n')
      outputFile.write('<http://www.example.com/trips/'+trip_id+'/stops/'+ stop_id +'> ' + '<'+ pickup_typeURI +'>' + ' "' + str(pickup_type)+ '"' + integer_ +'\n')
      outputFile.write('<http://www.example.com/trips/'+trip_id+'/stops/'+ stop_id +'> ' + '<'+ drop_off_typeURI +'>' + ' "' + str(drop_off_type).rstrip()+ '"' + integer_ +'\n')

print(cnt)



