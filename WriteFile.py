new_file = open("NewPVTFile.txt", mode="w", encoding="utf-8")


new_file.write("\n")
new_file.write("--========================================================\n")
new_file.write("--EOS PVT Program\n")
new_file.write("--Code by Steve Furnival, GUI by Ngwashi Ronald Afungchwi and Prof. David O. Ogbe\n\n")

new_file.write("--========================================================\n")
new_file.write("--Initialisation\n")
new_file.write("--========================================================\n \n")

new_file.write("INIT \n \n")
new_file.write("ENV     1 \n")
new_file.write("TSAT    1 \n")
new_file.write("ENDDEB \n \n")
new_file.write("EOS \n\n")
new_file.write("--Split Plus Fraction [C7+] into 3 Pseudo-Components\n\n")
new_file.write("SPLIT \n \n")
new_file.write("--Have 2 Samples, one Gas Condensate (from Gas Cap) and one Volatile Oil (from Oil Rim) \n \n")





new_file.close()