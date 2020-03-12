import pandas as pd
import csv
import json



# without file extension

def write_json(fname):
    jsonfile = open(
        '%s.json' % fname, 'a')
    reader = csv.DictReader(
        open("%s.csv" % fname))
    for row in reader:
        jsonfile.write(json.dumps(row)+'\n')

# with file extension

def csv2xl(csvFilename):
    # function reads csv file as data frame and then writes to a xlsx file
    df = pd.read_csv('%s' % (csvFilename))
    xlFilename = csvFilename.replace('.csv', '.xlsx')
    df.to_excel('%s' % (xlFilename), index=False)
