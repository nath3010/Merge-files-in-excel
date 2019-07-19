import os
import pandas
import pandas as pd
import glob





input_directory = "C://Users//nlsouza//Desktop//KPMG//Projetos//Bayer//todos//indiretos  mod//"
output_directory = "C://Users//nlsouza//Desktop//KPMG//Projetos//Bayer//todos//indiretos  mod final//"


files = os.listdir(input_directory)   

#Create a column with the files names 
for file in files: 
    
    excel = pandas.read_excel( input_directory + file)
    excel['file name'] = file
    print(diretorio + arquivo) 
    
    excel.to_excel(output_directory + file)
   


#Mearge the files
all_data = pd.DataFrame()
for f in glob.glob("where is the path//*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


#Create one file with all files
all_data.to_excel("the path//name.xlsx")
