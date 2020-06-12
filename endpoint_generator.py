#!/usr/bin/python3
from sys import argv
import csv
from jinja2 import Template


# jinja2 setup, open template
template = Template(open("template.py").read())

# check for parameters
if len(argv) < 3:
	exit("Parameter missing. Parameter 1 should be input file (csv), parameter 2 should be output file")


try:
	# open csv file for input 
	endpoints_file = open(argv[1])
	# open file for output
	output_file = open(argv[2], "w")


	# read csv file
	print("Reading input file...")
	rows = csv.DictReader(endpoints_file)

	# render template and write output file
	print("Loading template...")
	result = template.render(rows=rows, host=argv[3] if 3 < len(argv) else '0.0.0.0', port=argv[4] if 4 < len(argv) else '5000')
	print("Writing output...")
	output_file.write(result)

	print("Done")

	output_file.close()
	endpoints_file.close()
except Exception as e: 
	print("Error")
	raise