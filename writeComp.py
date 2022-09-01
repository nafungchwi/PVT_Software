
#=======================================================================
#
#  Module in PVTfree, Copyright (C) Steve Furnival, HoBoil Limited
#  see PVTfree.py for further details
#
#  Write Data for Compositional Data Output
#
#=======================================================================

#!/usr/bin/python3

import datetime

import numpy     as NP

import calcWater as CW
import utilities as UT
import writeBlk  as WB
import writeOut  as WO

#========================================================================
#  Write GEM Output
#========================================================================

def writeGEM(ZMFvD,clsEOS,dicSAM,clsCMP,clsIO,clsUNI) :

#-- Initialisation --------------------------------------------------    

    sCom = "**"
    nCom = clsEOS.nComp

    dVec = NP.zeros(nCom)

#-- Open the GEM File, if not already open -------------------------

    if not clsIO.qGEM :
        pathGEM = clsIO.patR + ".gem"
        fGEM    = open(pathGEM,'w')
        clsIO.setQGEM(True)
        clsIO.setFGEM(fGEM)
    else :
        fGEM = clsIO.fGEM

#== Headers ===========================================================        

    print("Writing Compositional Description for GEM")

    fSim = clsIO.fGEM
    sInp = clsIO.fInp.name

    OutU = clsCMP.OutU

    if OutU[:3] == "MET" : sUni = "METRIC"
    else                 : sUni = "FIELD "

#-- Write Header Information to Simulator File ----------------------        

    WO.outputHeader(fSim,sCom,clsIO)
    WO.outputEOS(fSim,sCom,clsIO,clsEOS)

#-- Header ----------------------------------------------------------    

#               123456789012345678901234567890123456789012345678901234567890
    sHead = "**==========================================================\n"
    fSim.write(sHead)
    sLabl = "**  CMG-GEM EOS Model generated by PVTfree Program\n"
    fSim.write(sLabl)
    sLabl = "**  From dataset " + sInp + "\n"
    fSim.write(sLabl)
    sLabl = "**  User specified " + sUni + " Units\n"
    fSim.write(sLabl)
    fSim.write(sHead)
    fSim.write("\n")

#-- Equation of State -----------------------------------------------    

    sLabl = "** Equation of State: Peng-Robinson (PR) or Soave-Redlich-Kwong (SRK)\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sEoS = clsEOS.EOS
    sOut = "*MODEL  *" + sEoS + "\n"
    fSim.write(sOut)
    fSim.write("\n")

#-- Number of Components --------------------------------------------

    sLabl = "** Number of Components; All assumed to be USER components\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sOut = "*NC  " + str(nCom) + "  " + str(nCom) + "\n"
    fSim.write(sOut)
    fSim.write("\n")

#-- Component Names -------------------------------------------------    

    sLabl = "** Component Names\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sOut = "*COMPNAME  "
    for iC in range(nCom) :
        sNam = clsEOS.gNM(iC)
        sOut = sOut + "'" + sNam + "'  "
    sOut = sOut + "\n"
    fSim.write(sOut)
    fSim.write("\n")

    fSim.write("*EOSSET  1\n")
    fSim.write("\n")

#-- Mole Weights ----------------------------------------------------    

    sCom = "**  Molecular Weights : [gm/gmol]\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("MW",iC)
    writeVectorD(fSim,sCom,"*MW",7,"{:8.3f}",dVec)

#-- Specific Gravity ------------------------------------------------

    sCom = "**  Specific Gravity\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("SG",iC)
    writeVectorD(fSim,sCom,"*SG",7,"{:8.6f}",dVec)

#-- Boiling Point Temperature ---------------------------------------

    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("TB",iC)
    if OutU[:3] == "MET" :
        sUni = ": [degC]"
        for iC in range(nCom) : dVec[iC] = clsUNI.I2X(dVec[iC],"degc")
    else :
        sUni = ": [degF]"
        for iC in range(nCom) : dVec[iC] = clsUNI.I2X(dVec[iC],"degf")
    sCom = "**  Boiling Point Temperature " + sUni + "\n"
    writeVectorD(fSim,sCom,"*TB",7,"{:8.3f}",dVec)

#-- Critical Temperatures -------------------------------------------
    
    for iC in range(nCom) : dVec[iC] = clsUNI.I2X(clsEOS.gPP("TC",iC),"kelv")
    sCom = "**  Critical Temperatures : [Kelvin]" + "\n"
    writeVectorD(fSim,sCom,"*TCRIT",7,"{:8.3f}",dVec)

#-- Critical Pressures ----------------------------------------------    

    for iC in range(nCom) : dVec[iC] = clsUNI.I2X(clsEOS.gPP("PC",iC),"atm")
    sCom = "**  Critical Pressures : [atm]\n"
    writeVectorD(fSim,sCom,"*PCRIT",7,"{:8.4f}",dVec)

#-- Critical Volumes ------------------------------------------------

    for iC in range(nCom) : dVec[iC] = clsUNI.I2X(clsEOS.gPP("VC",iC),"m3/kgmol")
    sCom = "**  Critical Volumes : [m3/kgmol]\n"
    writeVectorD(fSim,sCom,"*VCRIT",7,"{:8.3f}",dVec)

#-- Critical Z-Factors ----------------------------------------------

    sCom = "**  Critical Z-Factors " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("ZC",iC)
    writeVectorD(fSim,sCom,"*ZCRIT",7,"{:8.6f}",dVec)

#-- Acentric Factors ------------------------------------------------

    sCom = "**  Acentric Factors " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("AF",iC)
    writeVectorD(fSim,sCom,"*AC",7,"{:8.6f}",dVec)

#-- Parachors -------------------------------------------------------    

    sCom = "**  Parachors " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("PA",iC)
    writeVectorD(fSim,sCom,"*PCHOR",7,"{:8.3f}",dVec)
    
#-- Omega-A's -------------------------------------------------------

    sCom = "**  Omega-A Values " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("MA",iC)*clsEOS.OA
    writeVectorD(fSim,sCom,"*OMEGA",6,"{:11.9f}",dVec)

#-- Omega-B's -------------------------------------------------------

    sCom = "**  Omega-B Values " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("MB",iC)*clsEOS.OB
    writeVectorD(fSim,sCom,"*OMEGB",6,"{:11.9f}",dVec)

#-- Volume Shifts ---------------------------------------------------

    sCom = "**  Volume Shifts " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("SS",iC)
    writeVectorD(fSim,sCom,"*VSHIFT",7,"{:9.6f}",dVec)

#-- Binary Interaction Parameters -----------------------------------

    sCom = "** Binary Interaction Parameters\n"
    fSim.write(sCom)
    fSim.write("\n")
    sOut = "*BIN  "
    
    for iC in range(1,nCom) :
        for jC in range(iC) :
            dVal = clsEOS.gIJ(iC,jC) ; sVal = "{:9.6f}  ".format(dVal)
            sOut = sOut + sVal
        sOut = sOut + "\n"
        fSim.write(sOut)
        sOut = "      "

    fSim.write("\n")

#-- Reservoir Temperature -------------------------------------------

    tRes = clsCMP.Tres

    if OutU[:3] == "MET" :
        sUni = ": [degC]"
        tRes = clsUNI.I2X(tRes,"degC")
    else             :
        sUni = ": [degF]"
        tRes = clsUNI.I2X(tRes,"degF")
    sTr = "{:10.3f}\n".format(tRes)
    sLabl = "** Reservoir Temperature " + sUni + "\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sOut = "*TRES  " + sTr
    fSim.write(sOut)
    fSim.write("\n")

#== Brine Density at Standard (Stock Tank) Conditions =================

    if clsCMP.setBr :

        CW.calcPVTW(clsCMP,clsUNI,clsIO)  #-- Brine Properties

        dSTW = clsCMP.dSTW

#-- Aqueous Phase Properties ----------------------------------------    

        sLabl = "** Aqueous Phase Properties\n"
        fSim.write(sLabl)
        fSim.write("\n")

        pRefW = clsCMP.pRefW    #-- Ref Pres
        bRefW = clsCMP.bRefW    #-- Bw = Vres/Vsur = RhoSur/RhoRes
        cRefW = clsCMP.cRefW    #-- Compressibility
        bSalt = clsCMP.bSalt

        dRes  = dSTW/bRefW      #-- Reservoir Density

        if OutU[:3] == "MET" :
            dSTW  = clsUNI.I2X(dSTW ,"kg/m3")
            dRes  = clsUNI.I2X(dRes ,"kg/m3")
            pRefW = clsUNI.I2X(pRefW,"kpa")
            cRefW = clsUNI.I2X(cRefW,"1/kpa")

        sDsur = "{:10.3f}\n".format(dSTW)
        sDres = "{:10.3f}\n".format(dRes)
        sPref = "{:10.3f}\n".format(pRefW)
        sCref = "{:10.3e}\n".format(cRefW)
        sSalt = "{:10.5f}\n".format(bSalt)

        fSim.write("*DENW   " + sDsur)
        fSim.write("*DENWS  " + sDres)
        fSim.write("*CW     " + sCref)
        fSim.write("*REFPW  " + sPref)
        fSim.write("\n")

        fSim.write("*AQUEOUS-VISCOSITY *KESTIN\n")
        fSim.write("*SALINITY          *WTFRAC  " + sSalt)
        fSim.write("\n")

#== Close the file ====================================================

    clsIO.qGEM = UT.closeFile(fSim)

#== No return value ===================================================

    return

#========================================================================
#  Write VIP-COMP or Nexus-COMP Output
#========================================================================

def writeVIP(ZMFvD,clsEOS,dicSAM,clsCMP,clsIO,clsUNI) :

#-- Initialisation --------------------------------------------------    

    sCom = "C "
    nCom = clsEOS.nComp

    dVec = NP.zeros(nCom)

#-- Open the VIP File, if not already open -------------------------

    if not clsIO.qVIP :
        pathVIP = clsIO.patR + ".vip"
        fVIP    = open(pathVIP,'w')
        clsIO.setQVIP(True)
        clsIO.setFVIP(fVIP)
    else :
        fVIP = clsIO.fVIP

#== Headers ===========================================================        

    print("Writing Compositional Description for VIP/Nexus")

    fSim = clsIO.fVIP
    sInp = clsIO.fInp.name

    OutU = clsCMP.OutU

    if OutU[:3] == "MET" : sUni = "METRIC"
    else                 : sUni = "FIELD "

#-- Write Header Information to Simulator File ----------------------        

    WO.outputHeader(fSim,sCom,clsIO)
    WO.outputEOS(fSim,sCom,clsIO,clsEOS)

#-- Header ----------------------------------------------------------    

#               123456789012345678901234567890123456789012345678901234567890
    sHead = "C ==========================================================\n"
    fSim.write(sHead)
    sLabl = "C   VIP/Nexus EOS Model generated by PVTfree Program\n"
    fSim.write(sLabl)
    sLabl = "C   From dataset " + sInp + "\n"
    fSim.write(sLabl)
    sLabl = "C   User specified " + sUni + " Units\n"
    fSim.write(sLabl)
    fSim.write(sHead)
    fSim.write("\n")

#-- Equation of State -----------------------------------------------    

    sLabl = "C  Equation of State: Peng-Robinson (PR) or Soave-Redlich-Kwong (SRK)\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sEoS = clsEOS.EOS
    sOut = "EOS  " + sEoS + "  1  \n"
    fSim.write(sOut)
    fSim.write("\n")

#-- Components ------------------------------------------------------

    sLabl = "C  Component Names\n"
    fSim.write(sLabl)
    fSim.write("\n")
    fSim.write("COMPONENTS\n")
    sOut = "  "
    for iC in range(nCom) :
        sNam = clsEOS.gNM(iC)
        sOut = sOut + sNam + "  "
    sOut = sOut + "\n"
    fSim.write(sOut)
    fSim.write("\n")

#-- Main Properties Table -------------------------------------------

    sLabl = "C  Main Fluid Properties\n"
    fSim.write(sLabl)
    fSim.write("\n")

    if OutU[:3] == "MET" :
        sOut = "PROPERTIES  C  KPA\n"
    else :
        sOut = "PROPERTIES  F  PSIA\n"
    fSim.write(sOut)
#           12345678901
    sOut = "COMP        MW         TC          PC        ZC       ACENTRIC      OMEGAA      OMEGAB      VSHIFT      PCHOR\n"
    fSim.write(sOut)
    
    for iC in range(nCom) :
        sN = clsEOS.gNM(iC)      ; sNm = sN.ljust(9,' ')
        Mw = clsEOS.gPP("MW",iC) ; sMw = "{:10.3f}  ".format(Mw)
        Tc = clsEOS.gPP("TC",iC)
        Pc = clsEOS.gPP("PC",iC)
        if OutU[:3] == "MET" :
            Tc = clsUNI.I2X(Tc,"degc")
            Pc = clsUNI.I2X(Pc,"kpa" )
        else :
            Tc = clsUNI.I2X(Tc,"degf")
        sTc = "{:10.3f}  ".format(Tc)
        sPc = "{:10.3f}  ".format(Pc)
        Zc = clsEOS.gPP("ZC",iC) ; sZc = "{:10.5f}  ".format(Zc)
        AF = clsEOS.gPP("AF",iC) ; sAF = "{:10.5f}  ".format(AF)
        MA = clsEOS.gPP("MA",iC) ; sOA = "{:10.7f}  ".format(MA*clsEOS.OA)
        MB = clsEOS.gPP("MB",iC) ; sOB = "{:10.7f}  ".format(MB*clsEOS.OB)
        SS = clsEOS.gPP("SS",iC) ; sSS = "{:10.7f}  ".format(SS)
        PA = clsEOS.gPP("PA",iC) ; sPA = "{:10.3f}  ".format(PA)
        sOut = sNm + sMw + sTc + sPc + sZc + sAF + sOA + sOB + sSS + sPA + "\n"
        fSim.write(sOut)

    fSim.write("\n")

#-- BInary Interaction Parameters -----------------------------------    

    sLabl = "C  Binary Interaction Parameters\n"
    fSim.write(sLabl)
    fSim.write("\n")

    for iC in range(1,nCom) :

        sCom = clsEOS.gNM(iC)

        sOut = "DJK  " + sCom + "\n"
        fSim.write(sOut)

        for jC in range(iC) :
            sCom = clsEOS.gNM(jC)    ; sNam = sCom.ljust(8,' ')
            dVal = clsEOS.gIJ(iC,jC) ; sVal = "  {:10.5f}\n".format(dVal)
            sOut = sNam + sVal
            fSim.write(sOut)

    fSim.write("\n")

#-- End of EOS Section ----------------------------------------------

    sOut = "C  End of EOS Section\n"
    fSim.write(sOut)
    fSim.write("\n")
    
    fSim.write(sHead)
    fSim.write("ENDEOS\n")
    fSim.write(sHead)
    fSim.write("\n")

#== Water Properties ==================================================

    if clsCMP.setBr :

        fSim.write("C\n")
        fSim.write("C  Water Properties\n")
        fSim.write("C\n")
        fSim.write("\n")

        CW.calcPVTW(clsCMP,clsUNI,clsIO)  #-- Brine Properties

        pRefW = clsCMP.pRefW    #-- Ref Pres
        dSTW  = clsCMP.dSTW     #-- Stock Tank Density
        bRefW = clsCMP.bRefW    #-- Ref Bw
        cRefW = clsCMP.cRefW    #-- Ref Comp
        uRefW = clsCMP.uRefW    #-- Ref Visc
        vRefW = clsCMP.vRefW    #-- Viscosibility

        if OutU[:3] == "MET" :
            pRefW = clsUNI.I2X(pRefW,"kpa")
            dSTW  = clsUNI.I2X(dSTW ,"kg/m3")
            cRefW = clsUNI.I2X(cRefW,"1/kpa")
            vRefW = clsUNI.I2X(vRefW,"1/kpa")

        vRefW = uRefW*vRefW     #-- d[Visc]/dp = Visc*Viscosibility

        sPref = "{:10.3f}  ".format(pRefW)
        sDsur = "{:10.3f}  ".format(dSTW)
        sBref = "{:10.5f}  ".format(bRefW)
        sCref = "{:10.3e}  ".format(cRefW)
        sUref = "{:10.5f}  ".format(uRefW)
        sVref = "{:10.3e}  ".format(vRefW)

#-- Write Water Properties ------------------------------------------

        fSim.write("PVTW  IPVTW  PBASEW       DWB          BWI        CW           VW        VWP\n")
        sOut = "      1      " + sPref + sDsur + sBref + sCref + sUref + sVref + "\n"
        fSim.write(sOut)
        fSim.write("\n")

#== Close the file ====================================================

    clsIO.qVIP = UT.closeFile(fSim)

#== No return values ==================================================

    return

#========================================================================
#  Write Tempest-MORE Output
#========================================================================

def writeMORE(ZMFvD,clsEOS,dicSAM,clsCMP,clsIO,clsUNI) :

#-- Initialisation --------------------------------------------------    

    sCom = "--"
    nCom = clsEOS.nComp

    dVec = NP.zeros(nCom)

#-- Open the MORE File, if not already open ------------------------

    if not clsIO.qMOR :
        pathMOR = clsIO.patR + ".mor"
        fMOR    = open(pathMOR,'w')
        clsIO.setQMOR(True)
        clsIO.setFMOR(fMOR)
    else :
        fMOR = clsIO.fMOR

#== Headers ===========================================================        

    print("Writing Compositional Description for Tempest-MORE")

    fSim = clsIO.fMOR
    sInp = clsIO.fInp.name

    OutU = clsCMP.OutU

    if OutU[:3] == "MET" : sUni = "METRIC"
    else                 : sUni = "FIELD "

#-- Write Header Information to Simulator File ----------------------        

    WO.outputHeader(fSim,sCom,clsIO)
    WO.outputEOS(fSim,sCom,clsIO,clsEOS)

#-- Header ----------------------------------------------------------    

#               123456789012345678901234567890123456789012345678901234567890
    sHead = "--==========================================================\n"
    fSim.write(sHead)
    sLabl = "--  Tempest-MORE EOS Model generated by PVTfree Program\n"
    fSim.write(sLabl)
    sLabl = "--  From dataset " + sInp + "\n"
    fSim.write(sLabl)
    sLabl = "--  User specified " + sUni + " Units\n"
    fSim.write(sLabl)
    fSim.write(sHead)
    fSim.write("\n")

#----------------------------------------------------------------------
#  MORE-Specific Data
#----------------------------------------------------------------------

    sLabl = "-- Component Names (CNAM) are specified in the INPU section\n"
    fSim.write(sLabl)
    fSim.write("\n")

    sOut = "CNAM  "
    for iC in range(nCom) :
        sOut = sOut + clsEOS.gNM(iC) + "  "
    sOut = sOut + "WATR\n"
    fSim.write(sOut)
    fSim.write("\n")

#-- Composition -----------------------------------------------------

    sOut = "-- Compositions\n"
    fSim.write(sOut)
    fSim.write("\n")

    nSam = len(dicSAM)

    for iSam in range(nSam) :
        clsSAM = dicSAM[iSam]
        sNam   = clsSAM.sNam
        sCom = ""
        sKey = "SCMP  " + sNam + "\n"
        for iC in range(nCom) : dVec[iC] = clsSAM.gZI(iC)
        writeVectorD(fSim,sCom,sKey,6,"{:10.7f}",dVec)

#-- Fluid Section Header --------------------------------------------    

    fSim.write(sHead)
    sLabl = "FLUI EOS\n"
    fSim.write(sLabl)
    fSim.write(sHead)
    fSim.write("\n")

    sLabl = "-- Equation of State\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sEoS = clsEOS.EOS
    sOut = "EQUA  " + sEoS + "\n"
    fSim.write(sOut)
    fSim.write("\n")

#-- Reservoir Temperature -------------------------------------------

    tRes = clsCMP.Tres

    if OutU[:3] == "MET" :
        sUni = ": [degC]"
        tRes = clsUNI.I2X(tRes,"degC")
    else             :
        sUni = ": [degF]"
        tRes = clsUNI.I2X(tRes,"degF")
    sTr = "{:10.3f}\n".format(tRes)
    sLabl = "-- Reservoir Temperature " + sUni + "\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sOut = "TEMP  " + sTr
    fSim.write(sOut)
    fSim.write("\n")

#-- Main Properties Table -------------------------------------------

    sLabl = "-- Main Fluid Properties\n"
    fSim.write(sLabl)
    fSim.write("\n")

    sOut = "PROP  CNam       Mw          Tc          Pc       AcF         Zc          SG         Para\n"
    fSim.write(sOut)

    if OutU[:3] == "MET" :
        sOut = "--                          Kelv        bara\n"
    else :
        sOut = "--                          degR        psia\n"
    fSim.write(sOut)
    
    for iC in range(nCom) :
        sN = clsEOS.gNM(iC)      ; sNm = sN.ljust(8,' ')
        Mw = clsEOS.gPP("MW",iC) ; sMw = "{:10.3f}  ".format(Mw)
        Tc = clsEOS.gPP("TC",iC)
        Pc = clsEOS.gPP("PC",iC)
        if OutU[:3] == "MET" :
            Tc = clsUNI.I2X(Tc,"kelv")
            Pc = clsUNI.I2X(Pc,"bara") ; sPc = "{:10.4f}".format(Pc)
        else :
            sPc = "{:10.3f}  ".format(Pc)
        sTc = "{:10.3f}  ".format(Tc)
        AF = clsEOS.gPP("AF",iC) ; sAF = "{:10.5f}  ".format(AF)
        Zc = clsEOS.gPP("ZC",iC) ; sZc = "{:10.5f}  ".format(Zc)
        SG = clsEOS.gPP("SG",iC) ; sSG = "{:10.5f}  ".format(SG)
        PA = clsEOS.gPP("PA",iC) ; sPA = "{:10.3f}  ".format(PA)
        sOut = "      " + sNm + sMw + sTc + sPc + sAF + sZc + sSG + sPA + "\n"
        fSim.write(sOut)

    fSim.write("/\n")
    fSim.write("\n")

#-- Omega-A & Omega-B Multiplers -----------------------------------    

    sCom = "--  Omega-A Multipliers " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("MA",iC)
    writeVectorD(fSim,sCom,"OMGA  MULT\n",6,"{:11.9f}",dVec)

    sCom = "--  Omega-B Multipliers " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("MB",iC)
    writeVectorD(fSim,sCom,"OMGB  MULT\n",6,"{:11.9f}",dVec)

#-- Volume Shift Parameters -----------------------------------------    

    sCom = "--  Volume Shifts " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("SS",iC)
    writeVectorD(fSim,sCom,"VOLU\n",6,"{:11.8f}",dVec)

#-- BIPs ------------------------------------------------------------    

    fSim.write("-- Binary Iteraction Parameters (Lower Triangle)\n")
    fSim.write("\n")
    fSim.write("INTE\n")

    sCom = ""
    for iC in range(1,nCom) :
        bVec = NP.zeros(iC)
        for jC in range(iC) :
            bVec[jC] = clsEOS.gIJ(iC,jC)
        writeVectorD(fSim,sCom,"ROW",7,"{:9.6f}",bVec)

    fSim.write("/\n")
    fSim.write("\n")

#-- Brine Density at Standard (Stock Tank) Conditions ---------------    

    mFrc = clsCMP.bSalt #-- Mass Fraction of Salt in the Brine

    dSTW,comW = CW.calcRoweChouDen(mFrc,UT.tStand,UT.pStand,clsUNI)  #-- Stock Tank Brine Density

    clsCMP.setDenSTW(dSTW)

    clsCMP.setDenSTO(-1.0)  #-- In EoS Mode, E300 calculates STO Density
    clsCMP.setDenSTG(-1.0)  #-- Ditto

#== Brine Properties at Reference Pressure & Tres (for PVTW keyword) ==

    if clsCMP.setBr :

        CW.calcPVTW(clsCMP,clsUNI,clsIO)

#== Write DENSITY and PVTW keywords ===================================

        WB.outputECLDensity(OutU,fSim,clsCMP,clsUNI)
        WB.outputECLPVTW(OutU,fSim,clsCMP,clsUNI)

#== Close the file ====================================================

    clsIO.qMOR = UT.closeFile(fSim)

#== No return value ===================================================

    return

#========================================================================
#  Write E300 Output
#========================================================================

def writeE300(ZMFvD,clsEOS,dicSAM,clsCMP,clsIO,clsUNI) :

#-- Open the E300 File, if not already open ------------------------

    if not clsIO.q300 :
        path300 = clsIO.patR + ".e300"
        f300    = open(path300,'w')
        clsIO.setQ300(True)
        clsIO.setF300(f300)
    else :
        f300 = clsIO.f300

    sCom = "--"

#== Headers ===========================================================        

    print("Writing Compositional Description for E300")

    fSim = clsIO.f300
    sInp = clsIO.fInp.name

    OutU = clsCMP.OutU

    if OutU[:3] == "MET" : sUni = "METRIC"
    else                 : sUni = "FIELD "

#-- Write Header Information to Simulator File ----------------------        

    WO.outputHeader(fSim,sCom,clsIO)
    WO.outputEOS(fSim,sCom,clsIO,clsEOS)

#-- Header ----------------------------------------------------------    

#               123456789012345678901234567890123456789012345678901234567890
    sHead = "--==========================================================\n"
    fSim.write(sHead)
    sLabl = "--  E300 EOS Model generated by PVTfree Program\n"
    fSim.write(sLabl)
    sLabl = "--  From dataset " + sInp + "\n"
    fSim.write(sLabl)
    sLabl = "--  User specified " + sUni + " Units\n"
    fSim.write(sLabl)
    fSim.write(sHead)
    fSim.write("\n")

#-- Number of Components --------------------------------------------
    
    nCom = clsEOS.nComp
    
    sLabl = "--  Number of Components\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sLabl = "NCOMPS\n"
    fSim.write(sLabl)
    sLabl = "  {:2d}  /\n".format(nCom)
    fSim.write(sLabl)
    fSim.write("\n")

#-- Equation of State -----------------------------------------------    

    EOS = clsEOS.EOS
    if EOS == "SRK" : sExt = "Soave-Redlich-Kwong (SRK)"
    else            : sExt = "Peng-Robinson (PR)"
    sLabl = "--  Equation of State: " + sExt + "\n"
    fSim.write(sLabl)
    fSim.write("\n")
    sLabl = "EOS\n"
    fSim.write(sLabl)
    sLabl = "  " + str(EOS) + "  /\n"
    fSim.write(sLabl)
    fSim.write("\n")

    if EOS == "PR" :
        sLabl = "--  Modified Form of the Peng-Robinson EOS\n"
        fSim.write(sLabl)
        fSim.write("\n")
        sLabl = "PRCORR\n"
        fSim.write(sLabl)
        fSim.write("\n")

#== Component Properties ==============================================

    sVec = [ "" for i in range(nCom)]
    dVec = NP.zeros(nCom)

#-- Component Names -------------------------------------------------    

    sCom = "--  Component Names " + "\n"
    for iC in range(nCom) : sVec[iC] = clsEOS.gNM(iC)
    writeVectorS(fSim,sCom,"CNAMES\n",7,8,sVec)

#-- Mole Weights ----------------------------------------------------    

    if OutU[:3] == "MET" : sUni = ": [kg/kgmol]"
    else                 : sUni = ": [lb/lbmol]"
    sCom = "--  Molecular Weights " + sUni + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("MW",iC)
    writeVectorD(fSim,sCom,"MW\n",7,"{:8.3f}",dVec)

#-- Critical Temperatures -------------------------------------------
    
    if OutU[:3] == "MET" :
        sUni = ": [Kelvin]"
        for iC in range(nCom) : dVec[iC] = clsUNI.I2X(clsEOS.gPP("TC",iC),"kelv")
    else             :
        sUni = ": [degrees Rankine]"
        for iC in range(nCom) : dVec[iC] = clsEOS.gPP("TC",iC)
    sCom = "--  Critical Temperatures " + sUni + "\n"
    writeVectorD(fSim,sCom,"TCRIT\n",7,"{:8.3f}",dVec)

#-- Critical Pressures ----------------------------------------------    

    if OutU[:3] == "MET" :
        sUni = ": [barsa]"
        sFor = "{:8.4f}"
        for iC in range(nCom) : dVec[iC] = clsUNI.I2X(clsEOS.gPP("PC",iC),"bara")
    else             :
        sUni = ": [psia]"
        sFor = "{:8.3f}"
        for iC in range(nCom) : dVec[iC] = clsEOS.gPP("PC",iC)
    sCom = "--  Critical Pressures " + sUni + "\n"
    writeVectorD(fSim,sCom,"PCRIT\n",7,sFor,dVec)

#-- Critical Volumes ------------------------------------------------

    if OutU[:3] == "MET" :
        sUni = ": [m3/kgmol]"
        sFor = "{:8.3f}"
        for iC in range(nCom) : dVec[iC] = clsUNI.I2X(clsEOS.gPP("VC",iC),"m3/kgmol")
    else             :
        sUni = ": [ft3/lbmol]"
        sFor = "{:8.4f}"
        for iC in range(nCom) : dVec[iC] = clsEOS.gPP("VC",iC)
    sCom = "--  Critical Volumes " + sUni + "\n"
    writeVectorD(fSim,sCom,"VCRIT\n",7,sFor,dVec)

#-- Critical Z-Factors ----------------------------------------------

    sCom = "--  Critical Z-Factors " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("ZC",iC)
    writeVectorD(fSim,sCom,"ZCRIT\n",7,"{:8.6f}",dVec)

#-- Acentric Factors ------------------------------------------------

    sCom = "--  Acentric Factors " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("AF",iC)
    writeVectorD(fSim,sCom,"ACF\n",7,"{:8.6f}",dVec)

#-- Omega-A's -------------------------------------------------------

    sCom = "--  Omega-A Values " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("MA",iC)*clsEOS.OA
    writeVectorD(fSim,sCom,"OMEGAA\n",6,"{:11.9f}",dVec)

#-- Omega-B's -------------------------------------------------------

    sCom = "--  Omega-B Values " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("MB",iC)*clsEOS.OB
    writeVectorD(fSim,sCom,"OMEGAB\n",6,"{:11.9f}",dVec)

#-- Parachors -------------------------------------------------------    

    sCom = "--  Parachors " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("PA",iC)
    writeVectorD(fSim,sCom,"PARACHOR\n",7,"{:8.3f}",dVec)
    
#-- Volume Shifts ---------------------------------------------------

    sCom = "--  Volume Shifts " + "\n"
    for iC in range(nCom) : dVec[iC] = clsEOS.gPP("SS",iC)
    writeVectorD(fSim,sCom,"SSHIFT\n",7,"{:9.6f}",dVec)

#== Binary Interation Coefficients ====================================

    fSim.write("-- Binary Iteraction Parameters\n")
    fSim.write("\n")
    fSim.write("BIC\n")

    sCom = ""
    for iC in range(1,nCom) :
        bVec = NP.zeros(iC)
        for jC in range(iC) :
            bVec[jC] = clsEOS.gIJ(iC,jC)
        writeVectorD(fSim,sCom,"",7,"{:9.6f}",bVec)

    fSim.write("/\n")
    fSim.write("\n")

#-- Reservoir Temperature -------------------------------------------    

    tRes = clsCMP.Tres

    if OutU[:3] == "MET" :
        sUni = ": [degC]"
        tRes = clsUNI.I2X(tRes,"degC")
    else             :
        sUni = ": [degF]"
        tRes = clsUNI.I2X(tRes,"degF")
    sLabl = "-- Reservoir Temperature " + sUni + "\n"
    fSim.write(sLabl)
    fSim.write("\n")
    fSim.write("RTEMP\n")
    sLabl = "  {:7.3f}".format(tRes) +  "  /\n"
    fSim.write(sLabl)
    fSim.write("\n")

#== Composition (versus Depth? =========================================

    if clsCMP.qDep :
        
        dGOC = clsCMP.dGOC
        
        if OutU[:3] == "MET" :
            dUni = "m"
            zUni = "--  Depth/[m]   Composition\n"
        else                 :
            dUni = "ft"
            zUni = "--  Depth/[ft]  Composition\n"
            
        dGOC = clsUNI.I2X(dGOC,dUni)
        sGOC = "{:10.3f} ".format(dGOC)
        
        fSim.write("--  Composition versus Depth\n")
        fSim.write("--  Note: d(GOC) = " + sGOC + dUni + "\n")
        fSim.write("\n")
        fSim.write("ZMFVD\n")
        fSim.write(zUni)
        
        writeZMFVD(ZMFvD,dUni,fSim,"ECL",nCom,clsUNI)
        
    else :
        sCom = "--  Composition\n"
        for iC in range(nCom) : dVec[iC] = dicSAM[0].gZI(iC)
        writeVectorD(fSim,sCom,"ZI\n",6,"{:10.7f}",dVec)

#== Brine Density at Standard (Stock Tank) Conditions =================

    mFrc = clsCMP.bSalt #-- Mass Fraction of Salt in the Brine

    dSTW,comW = CW.calcRoweChouDen(mFrc,UT.tStand,UT.pStand,clsUNI)  #-- Stock Tank Brine Density

    clsCMP.setDenSTW(dSTW)

    clsCMP.setDenSTO(-1.0)  #-- In EoS Mode, E300 calculates STO Density
    clsCMP.setDenSTG(-1.0)  #-- Ditto

    WB.outputECLDensity(OutU,fSim,clsCMP,clsUNI)

#-- Brine Properties at Reference Pressure & Tres (for PVTW keyword)

    if clsCMP.setBr :

        CW.calcPVTW(clsCMP,clsUNI,clsIO)

#== Write DENSITY and PVTW keywords ===================================

        WB.outputECLPVTW(OutU,fSim,clsCMP,clsUNI)

#== Close the file ====================================================

    clsIO.q300 = UT.closeFile(fSim)

#== No return value ===================================================

    return

#========================================================================
#  Write a Vector of Float (Double) Values
#========================================================================

def writeVectorD(fSim,sComm,sKW,nLen,sForm,dVec) :

    nSETs = 0
    n1SET = nLen
    nSumm = len(dVec)

    nSETa = []

    while (nSumm-n1SET) > 0 :
        nSETs += 1
        nSETa.append(n1SET)
        nSumm = nSumm - n1SET

    nSETs += 1
    nSETa.append(nSumm)

    iCom = 0

    if sKW != "" :
        if sKW == "ROW" :
            fSim.write("  " + sKW)
        else :
            fSim.write(sComm)
            fSim.write("\n")
            fSim.write(sKW)

    for iS in range(nSETs) :

        sLine = "  "
        nThis = nSETa[iS]

        for iC in range(nThis) :
            dThis = dVec[iCom]
            sThis = sForm.format(dThis)
            sLine = sLine + sThis + "  "
            iCom += 1

        if sKW != "" :
            if sKW == "ROW" or sKW[:1] == "*" :
                sLine = sLine + "\n"
            else :
                if   iCom == nSumm : sLine = sLine + "  /\n"
                else               : sLine = sLine + "\n"
        else :
            sLine = sLine + "\n"

        fSim.write(sLine)

    if sKW != "" and sKW != "ROW" : fSim.write("\n")

#========================================================================
#  End of Routine
#========================================================================

    return

#========================================================================
#  Write a Vector of String Values
#========================================================================

def writeVectorS(fSim,sComm,sKW,nLen,nForm,sVec) :

    nSETs = 0
    n1SET = nLen
    nSumm = len(sVec)

    nSETa = []

    while (nSumm-n1SET) > 0 :
        nSETs += 1
        nSETa.append(n1SET)
        nSumm = nSumm - n1SET

    nSETs += 1
    nSETa.append(nSumm)

    iCom = 0

    fSim.write(sComm)
    fSim.write("\n")
    fSim.write(sKW)

    for iS in range(nSETs) :

        sLine = "  "
        nThis = nSETa[iS]

        for iC in range(nThis) :
            sThis = sVec[iCom]
            sThis = sThis.center(nForm)
            sLine = sLine + sThis + "  "
            iCom += 1

        if iCom == nSumm : sLine = sLine + "  /\n"
        else             : sLine = sLine + "\n"

        fSim.write(sLine)

    fSim.write("\n")    

#== No return value ===================================================
    
    return

#========================================================================
#  Write Composition versus Depth Information
#========================================================================

def writeZMFVD(ZMFvD,dUni,fSim,SIM,nCom,clsUNI) :

#          1234567890123456
    s4  = "    "
    s16 = "                "

    nByR = 5
    nRow = int(nCom/nByR) + 1

    for Row in ZMFvD :
        
        TVD  = Row[0]
        Psat = Row[1]
        zDep = Row[2]

        TVD = clsUNI.I2X(TVD,dUni)
        sTVD = "{:10.3f}  ".format(TVD)

        iCom = 0
        zLin = s4
        
        for iRow in range(nRow) :
            if iRow == 0 :
                zLin = s4 + sTVD
            else :
                zLin = s16
            for iInR in range(nByR) :
                if iCom == nCom : break
                zCom = zDep[iCom]
                sCom = "{:10.8f}  ".format(zCom)
                zLin = zLin + sCom
                iCom = iCom + 1
            zLin = zLin + "\n"
            fSim.write(zLin)

    fSim.write("/\n")
    fSim.write("\n")
    
#== No return value ===================================================
    
    return

#========================================================================
#  End of Module
#========================================================================
