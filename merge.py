import os
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys

path = 'files path'

files = os.listdir(path)

files.sort()

mergedObject = PdfFileMerger()

for f in files:
    mergedObject.append(PdfFileReader(path+f, 'rb')) 
    
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")	
    print(f)

# mergedObject.write("new files path/mergedfilesoutput.pdf")



