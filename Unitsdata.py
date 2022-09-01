"""conversion factor 
scf/scf to 
1. stb/scf = 0.178107607
2. stb/Mscf = 0.00017815
3. sm3/sm3 = 1
4. sm3/ksm3 = 0.001

1/psi to 
1. bar = 0.06894757

lb/ft3 to 
1. kg/m3 = 16.0184671
2. gm/cm3 = 0.01601846
3. degAPI = 0.16016366

rcf/rcf to 
1. stb/scf = 0.178107607
2. stb/Mscf = 0.00017815
3. sm3/sm3 = 1
4. sm3/ksm3 = 0.001

scf/scf to 
1. scf/stb = 5.61458354
2. Mscf/stb = 5613.24726
3. sm3/sm3 = 1
4. ksm3/sm3 = 1000

ft to 
1. m = 3.280839895

frac to 
1. perc = 100



"""

optionmenu = tkinter.Menu(menubar, tearoff = 0)
optionmenu.add_command(label = "Options...", command = open)
optionmenu.add_command(label = "Units", command = UnitConv)
menubar.add_cascade(label="Options", menu=optionmenu)