#! /usr/bin/python

from sys import argv
import csv
from os import path
import re

error_message = ('Please provide full filepath to USGS Geomagnetism file as an '
                 'argument to be parsed.\n Example: "python data_averager.py '
              '/path/to/file"')


def dataGrabber():
    """ This function ensures the file exists, and it is valid.
    
    A valid file is a USGS Gemoganetism .txt file downloaded from the USGS
    Geomagnetism website. It verifies it is a valid file by looking at the
    header row. If a valid file isn't provided, this script will not continue.
    
        Returns: geo_dataset - A list of lists with each inner list containing
            data from each row of the file.
    """
    
    geo_dataset = []
    
    # If an argument is not provided with the script, then print help text.
    
    if len(argv) != 2:
        print(error_message)
        
    # If an argument is provided, check that it is a valid, existing file.
    # If it is valid, clean up the extra white spaces.
    
    else:
        file_path = argv[1]
        if path.isfile(file_path):
            with open(file_path, 'r') as geo_data:
                geo_reader = csv.reader(geo_data, delimiter=' ')
                for row in geo_reader:
                    text_row = ' '.join(row)
                    clean_row = re.sub(' +', ' ',text_row)
                    geo_dataset.append([clean_row])
        else:
            print(error_message)
                
    if geo_dataset[0] == ['Year Mon Day Hr DOY from start Fractional DOY '
                          'Fractional year Dst HER KAK HON SJG sigma']:
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