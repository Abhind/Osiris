#!/usr/bin/env python
import re
import mimetypes
import os
# all declarations
path = 'Path where logs are stored'
out_val = "('text/plain', None)"
in_val = "test"
in_val1 = "test"
temp_list1 = []
traversal = []
# funcrion defination
def match(temp_list1):
    with open("output.txt", "w") as f1:
     for line in temp_list1:
         print(line)
         f1.write("******************************************************************")
         f1.write("\n")
         f1.write("File Path:")
         f1.write("\t")
         f1.write(line)
         f1.write("\n")
         f1.write("******************************************************************")
         f1.write("\n")
         f2 = open(line, "r")
         for line1 in f2:
                 if re.match("(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6789]\d{9}",line1):
                         f1.write("Phone:")
                         f1.write("\t")
                         f1.write(line1)
                         f1.write("\n")
                 elif re.match("\S+@\S+",line1):
                         f1.write("Email:")
                         f1.write("\t")
                         f1.write(line1)
                         f1.write("\n")
                 elif re.findall("VPA",line1):
                         f1.write("VPA:")
                         f1.write("\t")
                         f1.write(line1)
                         f1.write("\n")
                 elif re.match("[A-Z]{5}[0-9]{4}[A-Z]{1}",line1):
                         f1.write("PAN:")
                         f1.write("\t")
                         f1.write(line1)
                         f1.write("\n")
                 else:
                         f1.write(" ")
    return

#File Traversal in a directory
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        #print(f)
        if '.log' in file:
            files.append(os.path.join(r, file))

print(files)
for f1 in files:
        #Phone = open(f, "r")
        in_val = mimetypes.guess_type(f1, strict=True)
        #print(in_val)
        # As .txt file returns 'text/, None' and log file returns None, None; i am excluding the text file from processing and only considering the log files
        if not'text' in in_val:
            print(in_val)
            traversal.append(f1)
print(traversal)
match(traversal)
