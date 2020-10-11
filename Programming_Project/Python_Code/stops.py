#!/usr/bin/env python3

import csv

stop_idURI = "http://www.example.com/stops"
stop_codeURI = "http://www.example.com/stop_code"
stop_nameURI = "http://www.example.com/stop_name"
stop_descURI = "http://www.example.com/stop_desc"
stop_latURI = "http://www.example.com/stop_lat"
stop_lonURI = "http://www.example.com/stop_lon"
location_typeURI = "http://www.example.com/location_type"

lat = "http://www.w3.org/2003/01/geo/wgs84_pos#lat"
lon ="http://www.w3.org/2003/01/geo/wgs84_pos#long"

string_ = "^^xsd:string."
integer_ = "^^xsd:int."
float_ = "^^xsd:float."

outputFileName = "stopsOUT.txt"
outputFile = open(outputFileName, "w")

inputFileName = "stops.txt"

cnt = 0
with open(inputFileName) as infile:
  for line in infile:
    cnt = cnt + 1
    row = line.split(",")

    stop_id = row[0]
    stop_code = row[1]
    stop_name = row[2]
    stop_desc = row[3]
    stop_lat = row[4]
    stop_lon = row[5]
    location_type = row[6]

    if cnt>1:
      outputFile.write('<'+stop_idURI+'/'+stop_id+'> ' + 'a' + ' <' +stop_idURI+'>'+'.''\n')
      outputFile.write('<'+stop_idURI+'/'+stop_id+'> '+'<'+ stop_codeURI +'>' +' "' + str(stop_code)+ '"' + integer_ +'\n')
      outputFile.write('<'+stop_idURI+'/'+stop_id+'> '+'<'+ stop_nameURI +'> '  + str(stop_name)+  string_ +'\n')
      outputFile.write('<'+stop_idURI+'/'+stop_id+'> '+'<'+ stop_descURI  +'>' + ' "' + str(stop_desc)+ '"' + string_ +'\n')


      outputFile.write('<'+stop_idURI+'/'+stop_id+'> '+'<'+ lat +'>' + ' "' + str(stop_lat)+ '"' +'\n')
      outputFile.write('<'+stop_idURI+'/'+stop_id+'> '+'<'+ lon +'>' + ' "' + str(stop_lon)+ '"' +'\n')



      outputFile.write('<'+stop_idURI+'/'+stop_id+'> '+'<'+ location_typeURI +'>' + ' "' + str(location_type).rstrip()+ '"' + integer_ +'\n')

print(cnt)

