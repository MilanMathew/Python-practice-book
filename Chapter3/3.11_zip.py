# Program takes name of zip file as first argument and 
# files to add as rest of the arguments.
import sys
import zipfile

new_zip_file = zipfile.ZipFile(sys.argv[1],'w')
for i in range(2, len(sys.argv)):
    new_zip_file.write(sys.argv[i])
