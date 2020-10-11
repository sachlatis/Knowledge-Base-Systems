#!/usr/bin/env python3

import csv

trip_idURI = "http://www.example.com/trips"
trip_headsignURI = "http://www.example.com/trip_headsign"
direction_idURI = "http://www.example.com/direction_id"
block_idURI = "http://www.example.com/block_id"


string_ = "^^xsd:string."
integer_ = "^^xsd:int."
boolean_ = "^^xsd:boolean."



outputFileName = "tripsOUTNEW.txt"
outputFile = open(outputFileName, "w")

inputFileName = "trips.txt"

cnt = 0
with open(inputFileName) as infile:
  for line in infile:
    cnt = cnt + 1
    row = line.split(",")

    trip_id = row[2]
    trip_headsign = row[3]
    direction_id = row[4]
    block_id = row[5]

    if cnt>1:
      outputFile.write('<'+trip_idURI +'/'+trip_id+'> ' + 'a' + ' <' +trip_idURI+'>'+'.''\n')
      outputFile.write('<'+trip_idURI +'/'+trip_id+'> '+'<'+ trip_headsignURI +'>' +' "' + str(trip_headsign)+ '"' + string_ +'\n')
      outputFile.write('<'+trip_idURI +'/'+trip_id+'> '+'<'+ direction_idURI +'>' +' "' + str(direction_id)+ '"' + boolean_+'\n')
      outputFile.write('<'+trip_idURI +'/'+trip_id+'> '+'<'+ block_idURI +'>' +' "' + str(block_id)+ '"' + integer_ +'\n')


print(cnt)


