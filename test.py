


load_new_file = open("NewPVTfile.txt","a")
load_new_file.write("\n")
load_new_file.write("--========================================================\n")
load_new_file.write("--EOS PVT Program\n")
load_new_file.write("--Code by Steve Furnival, GUI by Ngwashi Ronald Afungchwi and Prof. David O. Ogbe\n\n")

load_new_file.write("--========================================================\n")
load_new_file.write("--Fluid Initialisation\n")
load_new_file.write("--========================================================\n \n")

load_new_file.write("INIT \n \n")
    #load_new_file.write("ENV     1 \n")
    #load_new_file.write("TSAT    1 \n")
    #load_new_file.write("ENDDEB \n \n")

EOS_insert = input("Enter equation of State (PR or SRK): ")

load_new_file.write("EOS   " + EOS_insert)
    #if EOS == PR or SRK write them here in file 
load_new_file.write("\n\n")

split_number = input("Enter number of split: ")

load_new_file.write("--Number of pseudocomponents to be split from C7+\n\n")
load_new_file.write("SPLIT   " + split_number)
    #collect the value from split input and write it here

load_new_file.write("\n \n")
load_new_file.write("--Sample Definitions \n\n")
    #load samples data here 
Load_samples = open("Sample_data.txt", "r")
for lines0 in Load_samples:
    load_new_file.write(lines0)

load_new_file.write(" \n\n")
load_new_file.write("ENDINIT \n\n")
    
    #load experiment data 
load_new_file.write("--==============================================================\n")
load_new_file.write("--Experiments \n")
load_new_file.write("--==============================================================\n\n")
load_new_file.write("EXP \n\n")

Load_CCE = open("CCE_data.txt","r")
Load_CVD = open("CVD_data.txt","r")
Load_DLE = open("DLE_data.txt","r")
Load_SEP = open("SEP_data.txt","r")


for lines in Load_CCE:
    load_new_file.write(lines)
load_new_file.write(" \n")
for lines2 in Load_CVD: 
    load_new_file.write(lines2)
load_new_file.write(" \n")    
for lines3 in Load_DLE:
    load_new_file.write(lines3)
load_new_file.write(" \n")
for lines4 in Load_SEP:
    load_new_file.write(lines4)

load_new_file.write("\n\n \n")
load_new_file.write("ENDEXP \n\n")

load_new_file.write("--==============================================================\n")
load_new_file.write("--STOP \n")
load_new_file.write("--==============================================================\n\n")
load_new_file.write("STOP \n\n")  


