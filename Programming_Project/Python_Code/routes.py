#!/usr/bin/env python3

import csv

routesURI = "http://www.example.com/routes"
route_short_nameURI = "http://www.example.com/route_short_name"
route_long_nameURI = "http://www.example.com/route_long_name"
route_descURI = "http://www.example.com/route_desc"
route_typeURI = "http://www.example.com/route_type"
route_colorURI = "http://www.example.com/route_color"
route_text_colorURI = "http://www.example.com/route_text_color"

string_ = "^^xsd:string."
integer_ = "^^xsd:int."

outputFileName = "routesOUT.txt"
outputFile = open(outputFileName, "w")

inputFileName = "routes.txt"

cnt = 0
with open(inputFileName) as infile:
  for line in infile:
    cnt = cnt + 1
    row = line.split(",")
    route_id = row[0]
    route_short_name = row[1]
    route_long_name = row[2]
    #route_desc = "EMPTY"
    route_type = row[4]
    route_color = row[5]
    route_text_color = row[6]
    if cnt>1:
      outputFile.write('<'+routesURI+'/'+route_id+'> ' + 'a' + ' <' +routesURI+'>'+'.''\n')
      outputFile.write('<'+routesURI+'/'+route_id+'> '+'<'+ route_short_nameURI +'>' +' "' + str(route_short_name)+ '"' + string_ +'\n')
      outputFile.write('<'+routesURI+'/'+route_id+'> '+'<'+ route_long_nameURI +'> '  + str(route_long_name)+  string_ +'\n')
      #outputFile.write('<'+routesURI+'/'+route_id+'> '+'<'+ route_descURI +'>' + ' "' + str(route_desc)+ '"' + string_ +'\n')
      outputFile.write('<'+routesURI+'/'+route_id+'> '+'<'+ route_typeURI +'>' + ' "' + str(route_type)+ '"' + integer_ +'\n')
      outputFile.write('<'+routesURI+'/'+route_id+'> '+'<'+ route_colorURI +'>' + ' "' + str(route_color)+ '"' + string_ +'\n')
      outputFile.write('<'+routesURI+'/'+route_id+'> '+'<'+ route_text_colorURI +'>' + ' "' + str(route_text_color).rstrip()+ '"' + string_ +'\n')

print(cnt)


