#! /usr/bin/python

from sys import argv
import csv
from os import path

error_message = ('Please provide full filepath to USGS Geomagnetism file as an '
                 'argument to be parsed.\n Example: "python data_averager.py '
              '/path/to/file"')


def dataGrabber():
    geo_dataset = []
    
    if len(argv) != 2:
        print(error_message)
        print 
        
    else:
        file_path = argv[1]
        if path.isfile(file_path):
            with open(file_path, 'r') as geo_data:
                geo_reader = csv.reader(geo_data, delimiter=' ')
                for row in geo_reader:
                    geo_dataset.append(row)
                return geo_dataset
        else:
            print(error_message)
            

def dataParser(usgs_geo_data):
    print usgs_geo_data
    

def main():
    usgs_data_list = dataGrabber()
    if usgs_data_list:
        dataParser(usgs_data_list)
    
    
if __name__ == '__main__':
    main()