import os  

path = '/home/orise/Desktop/paper/Q5 - 05'  
new_path = '/home/orise/Desktop/Q5'  

files = os.listdir(path)  
print(files)
files.sort()
print(files)
# size_files = sizeof()

for f in files: 	
    print(f) 
    pdf = os.listdir(path+"/"+str(f))
    for n in pdf: 
        file_path = path+"/"+str(f)
        filename, file_extension = os.path.splitext(file_path+"/"+str(n))
        # print(file_extension)
        print(file_path)
        if(file_extension == ".pdf"):
            True
            # print("ok")
            os.rename(str(filename)+".pdf",new_path+"/"+str(f)+".pdf") 
            # count += 1
