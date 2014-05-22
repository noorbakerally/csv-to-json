csv-to-json
===========

A simply python script that converts a csv file and output a json

This is a script which needs to be modified for custom use. I'm using this script with the following assumptions:
1. All the columns are on the first line seperated by ;
2. The first column is a primary key
3. The rows comes after and are again seperated by ;

A sample csv file as follows:

studentId,name,surname
1,noorani,bakerally
2,john,smith

will be output in json as follows:

{1:{"name":"noorani","surname":"bakerally"},2:{"name":"john","surname":"smith"}}

I'm using the above design structure to ensure that all object within the json can be directly referenced with a primary key

USAGE
=====
Suppose you have a file input.csv, to convert it to JSON,

python json_conv.py input.csv

If you want to direct the output, simply use redirection, python json_conv.py input.csv >> output.csv
