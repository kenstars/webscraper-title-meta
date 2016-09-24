import urllib2
import re
import csv
URL_list = []

input_filename = 'filename.csv'
output_filename = 'outputfile.csv'

with open(input_filename, 'rb') as csvfile:
	filepoint = csv.reader(csvfile, delimiter=',')
	for row in filepoint:
		URL_list.append(row[0])

target = open(output_filename, 'w')

target.write('URL, Title, Meta Description')
for URL in URL_list[1:]:
	try:
		data = urllib2.urlopen(URL)
		title = '-'
		meta_desc = '-'
		for line in data:
			if '</head' not in line:
				if '<title' in line:
					title = line.split('>')[1].split('<')[0]
				if '<meta' in line:
					if 'name="Description"' in line :
						meta_desc = line.split('content')[1].strip()
						meta_desc = re.findall(r'"([^"]*)"', meta_desc)[0].strip()
			else:
				break
		if title == None:
			title = '-'
		if meta_desc == None or meta_desc == '':
			meta_desc = '-'
		target.write(URL+', '+title+', '+meta_desc)
		target.write("\n")
	except:
		print "Found a row without a valid URL"


target.close()





