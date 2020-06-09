# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:47:45 2019
csv to binary
@author: Duy Anh
"""
import struct

# Instruction to pack data
'''
timestamp   = 32bits   int
accel       = 32*3bits int
gyro        = 32*3bits int
pressure    = 32bits   int
temperature = 32bits   int
'''
packCol = (0,1,2,3,4,5,6,7,8)
data_NA = 0  # The value replace of not available data
typeCol = "iiiiiiiii" # Type of data expect in each column

# File path
dataFrom_csv = "flightComputer_data_filtered.csv"     # FIle to write the formated data to in .csv
dataTo_bin = "flightComputer_data_filtered.bin"     # FIle to write the formated data to in binary

# Enable the ability to input file name or path
changeFile = False
if changeFile:
    dataFrom = str(input("Read from: "))  # Get file to read for format
    dataTo = str(input("Write bits to: "))    # Get the file to write the formatted data to
    
    # Set the read and write file
    dataFrom_csv = dataFrom + ".csv"
    dataTo_bin = dataTo + ".bin"

# Pack the data to binary file
getData = open(dataFrom_csv, 'r') # Get pointer to the file for read
writeData = open(dataTo_bin, 'wb') # Get pointer to the file for write
for line in getData:
    line = line.strip()    # Clear any whitespace
    line = line.split(',') # Get column value separate by comma ','
    
    # Get and filter the data
    data = [] # Empty list
    for index in packCol:
        # Check if the data is valid and save for later write to binary file
        if not line[index].lstrip("+-").isnumeric(): # Does not include decimal point, need to change if want to have decimal point
            data.append(int(data_NA))
        else:
            data.append(int(line[index]))
            
    # Write to binary file
    data_binary = struct.pack('<' + typeCol, *data) # Pack the data in little endien encoding - using *args
    writeData.write(data_binary)
        
# Close file
getData.close()
writeData.close()

# Print status done
print("Finish creating binary file!")
input("END!")