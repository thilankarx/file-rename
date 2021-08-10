import os
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys

path = '/home/orise/Desktop/Q1/'

files = os.listdir(path)

files.sort()

mergedObject = PdfFileMerger()

for f in files:
    mergedObject.append(PdfFileReader(path+f, 'rb')) 
    
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")	
    print(f)

# mergedObject.write("/home/orise/Desktop/mergedfilesoutput.pdf")



