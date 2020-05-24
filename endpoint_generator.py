#!/usr/bin/python3
from sys import argv
import csv

if len(argv) < 3:
	exit("Parameter missing. Parameter 1 should be input file (csv), parameter 2 should be output file")
	

content = """
from flask import Flask

app = Flask(__name__)
"""

endpoints_file = open(argv[1])
output_file = open(argv[2], "w")

print("Writing file...")
for row in csv.DictReader(endpoints_file):
	content += "\n\n"
	content += "@app.route('{}')\r".format(row['endpoint'])
	content += "\ndef {}():\r".format(row['method'])
	content += "return \"Showing {} route\"\n".format(row['method'])


content += """

if __name__ == '__main__':
	app.run(host='{}', port={}, debug=True)

""".format(argv[3] if 3 < len(argv) else '0.0.0.0', argv[4] if 4 < len(argv) else '5000')


output_file.write(content)

print("Done")

output_file.close()
endpoints_file.close()
