#manage codewith 1 python script to create folder structure 
#import os and initialiaze log for imformation
import os
from pathlib import Path
import logging 

#logging for mesages and time they are logged
logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s:')

#create project folder and inside crteate src for all other folders
project_name = "mlProject"

 #take a list of files namaes you will want inside src under parent folder project_name
 
list_of_files = [
     ".git/workflows/.gitkeep",
     f"src/{project_name}/__init__.py",
     f"src/{project_name}/components/__init__.py",
     f"src/{project_name}/utils/__init__.py",
     f"src/{project_name}/config/__init__.py",
     f"src/{project_name}/config/configuration/__init__.py",
     f"src/{project_name}/pipeline/__init__.py",
     f"src/{project_name}/entity/__init__.py",
     f"src/{project_name}/entity/config/__init__.py",
     f"src/{project_name}/constatnts/__init__.py",
     "cofig/config.yaml",
     "params.yaml",
     "schema.yaml",
     "main.py",
     "app.py",
     "Dockerfile",
     "requirements.txt",
     "setup.py",
     "research/trials.ipynb",
     "templates/index.html"
     
 ]
 
 
for filepath in list_of_files:
     filepath = Path(filepath)
     filedir, filename = os.path.split(filepath)
     
     #create folder directories & log information
     if filedir != "":
         os.makedirs(filedir, exist_ok=True)
         logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    #create the files to file directories ad log information
    #also checking if file exists in dir     
     if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creatig empty file: {filepath}")
    #if everything is okay!! log info file already exists
     else:
        logging.info(f"{filenmae} is already exist")
        
        
     
   

