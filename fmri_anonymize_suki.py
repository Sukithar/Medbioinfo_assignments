#!/usr/bin/env python3
# created: October 06, 2017
# Sukithar Rajan
# last update: October 20, 2017
#*******************************
# Script to read DICOM (image) files from multiple sub-directories;
# and substitute patient_name, date_of_birth, and personnummer with a secret_code
#################################

import sys
import os
import dicom
import numpy
import shutil

###############################################
# navigate through directories/sub-directories;
# find dicom files, and report,  make a copy
# and save in another directory for parsing
###############################################

usage = """
Usage:
./fmri_anonymize_suki.py original_directory anonymized_directory secret_code
Please provide absolute path of directories
Anonymized directory should be empty. If there exists no such directory;
then the script will make one for you
"""

if len(sys.argv) != 4:
    print(usage)
    sys.exit()

PathDicom = sys.argv[1] # give source directory as argument
#PathDicom="/Users/srrn/Desktop/Practise/fMRI/" # set a working directory path

# make a new directory to save copy of Dicom files
NewPath = sys.argv[2] # give destination path as argument # this folder should be empty
#NewPath = "/Users/srrn/Desktop/Practise/fMRI/DicomCopy/"
if not os.path.exists(NewPath):
    """if no destination directory; then make a new one"""
    os.mkdir(NewPath)

counter_1=0
listFilesDCM = [] # create an empty list for DICOM files
print('**********************************')
print('Copying DICOM files to destination dir')

for dirName, subdirList, fileList in os.walk((PathDicom), topdown=False):
    for files in fileList:
        if "EE" in files:
            if files not in listFilesDCM:
                listFilesDCM.append(os.path.join(dirName, files)) # adds files from different directories
#                print(files)

for i in listFilesDCM:
#    print(i)
#    shutil.move(i, NewPath)
    shutil.copy(i, NewPath)
    counter_1 += 1

print('**********************************')
print('Destination directory:', NewPath)
print('Number of Dicom files copied to destination:',counter_1)

########################################################################
# navigate to folder having copied files; read Dicom files and anonymize
########################################################################

code = sys.argv[3]
counter_2 = 0
listFilesDCM_2 = [] # empty list for saving file names in the dir
new_file_name = '_anonymised.dcm' #extension for copied file

for dirName, subdirList, fileList in os.walk(NewPath):
    for filename in fileList:
        listFilesDCM_2.append(os.path.join(dirName, filename))
#print(listFilesDCM_2)
#for i in listFilesDCM_2:

""" loop through the files and change relevant fields"""
for filenameDCM in listFilesDCM_2:
    file_1 = dicom.read_file(filenameDCM)
    counter_2 += 1
    if ("PatientName" in file_1):
        file_1.PatientName = code
    if ("PatientBirthDate" in file_1):
        file_1.PatientBirthDate = code
    if ("PatientID" in file_1):
        file_1.PatientID = code
    file_1.save_as(filenameDCM + new_file_name)

"""removing copied files after editing"""
for f in listFilesDCM_2:
    os.remove(os.path.join(NewPath, f))
#    print(f)

print('Number of anonymized files:', counter_2)
print('**********************************')

#####################################
