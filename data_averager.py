#! /usr/bin/python

from sys import argv
import csv
from os import path
import re

error_message = ('Please provide full filepath to USGS Geomagnetism file as an '
                 'argument to be parsed.\n Example: "python data_averager.py '
              '/path/to/file"')
              
# The objective is to average all the Dst, the HON and the SJG columns only.
# The below variables are positional coordinates of this data we're interested
# in from the dataset provided.

dst_pos = 7
hon_pos = 10
sjg_pos = 11

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
    if len(geo_dataset) < 1:
        print(error_message)
    else:
        if geo_dataset[0] == ['Year Mon Day Hr DOY from start Fractional DOY '
                              'Fractional year Dst HER KAK HON SJG sigma']:
            print('Valid dataset detected. Continuing...')
            return geo_dataset
        else:
            print(error_message)
            

def dataParser(usgs_geo_data):
    """ Takes a list of lists and finds the average of a subset of those lists.
    
    This function removes the header row which isn't data, and splits the sets
    of data we're interested in into each set into its own list. It then
    calculates the average of each set of data and prints these averages to
    the terminal window.
    
    Arguments: 
        usgs_geo_data - A list of lists.
    """
    
    dst_list = []
    hon_list = []
    sjg_list = []
    
    just_data = usgs_geo_data[1:]
    for row in just_data:
        data_row = row[0].split(' ')
        dst_list.append(float(data_row[dst_pos]))
        hon_list.append(float(data_row[hon_pos]))
        sjg_list.append(float(data_row[sjg_pos]))
        
    dst_average = sum(dst_list) / len(dst_list)
    hon_average = sum(hon_list) / len(hon_list)
    sjg_average = sum(sjg_list) / len(sjg_list)
    
    print('Here are some sample averages - DST, HON, then SJG')
    
    print dst_list[:5]
    print hon_list[:5]
    print sjg_list[:5]
    
    print('DST average: %s' % dst_average)
    print('HON average: %s' % hon_average)
    print('SJG average: %s' % sjg_average)    


def main():
    usgs_data_list = dataGrabber()
    if usgs_data_list:
        dataParser(usgs_data_list)
    
    
if __name__ == '__main__':
    main()