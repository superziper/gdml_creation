from re import L
import pyg4ometry as _pyg
import pyg4ometry.stl as _stl 
import pyg4ometry.gdml as _gdml
import pyg4ometry.geant4 as _g4
import pyg4ometry.visualisation.VtkViewer as _vtk
import pandas as pd

reg = _g4.Registry()

##MATERIAL
tungsten = _g4.nist_material_2geant4Material("G4_W", reg)
udara = _g4.nist_material_2geant4Material("G4_AIR", reg)
# besi = _g4.nist_material_2geant4Material("G4_Fe", reg)
# sulfur = _g4.nist_material_2geant4Material("G4_S", reg)
# mangan = _g4.nist_material_2geant4Material("G4_Mn", reg)
karbon = _g4.MaterialPredefined("G4_C", reg)
tembaga = _g4.nist_material_2geant4Material("G4_Cu", reg)
vakum = _g4.nist_material_2geant4Material("G4_Galactic", reg)
air = _g4.MaterialPredefined("G4_WATER", reg)
timbal = _g4.nist_material_2geant4Material("G4_Pb", reg)
# berilium = _g4.nist_material_2geant4Material("G4_Be", reg)
# kapton = _g4.MaterialPredefined("G4_KAPTON", reg)
# mylar = _g4.MaterialPredefined("G4_MYLAR", reg)
# stainless_steel = _g4.MaterialPredefined("G4_STAINLESS-STEEL", reg)
softTissue = _g4.MaterialPredefined("G4_TISSUE_SOFT_ICRP", reg)
paru = _g4.MaterialPredefined("G4_LUNG_ICRP", reg)
jantung = _g4.MaterialPredefined("G4_MUSCLE_STRIATED_ICRU", reg)

##WORLD
solidWorld = _g4.solid.Box("solidWorld", 1, 1, 4, reg, "m")
logicWorld = _g4.LogicalVolume(solidWorld, udara, "logicWorld", reg)
reg.setWorld(logicWorld.name)

##target1
pos_target1 = _gdml.Position("pos_target1", 0., 0., 0.20055, "cm", reg)
solidTarget1 = _g4.solid.Box("solidTarget1", 1.2, 1.2, 0.0889, reg, "cm")

logicTarget1 = _g4.LogicalVolume(solidTarget1, tungsten, "logicTarget1", reg)
physTarget1 = _g4.PhysicalVolume([0.,0.,0.], pos_target1, logicTarget1, "physTarget1", logicWorld, reg, 0, True)

##target2
pos_target2 = _gdml.Position("pos_target2", 0., 0., 0.07736, "cm", reg)
solidTarget2 = _g4.solid.Box("solidTarget2", 1.2, 1.2, 0.15748, reg, "cm")

logicTarget2 = _g4.LogicalVolume(solidTarget2, tembaga, "logicTarget2", reg)
physTarget2 = _g4.PhysicalVolume([0.,0.,0.], pos_target2, logicTarget2, "physTarget2", logicWorld, reg, 0, True)


#collimator upper
pos_upperCollimator = _gdml.Position("pos_upperCollimator", 0., 0., -1., "cm", reg)
solidUpperCollimator = _g4.solid.Tubs("solidUpperCollimator", 1., 8., 3., 0., 360., reg, "cm", "deg")

logicUpperCollimator = _g4.LogicalVolume(solidUpperCollimator, tungsten, "logicUpperCollimator", reg)
physUpperCollimator = _g4.PhysicalVolume([0.,0.,0.], pos_upperCollimator, logicUpperCollimator, "physUpperCollimator", logicWorld, reg, 0, True)

##collimator lower
solidLowerCollimator = _g4.solid.Cons("solidLowerCollimator", 0., 0.5, 0., 3., 11.18, 0., 360., reg, "cm", "deg")
logicLowerCollimator = _g4.LogicalVolume(solidLowerCollimator, tungsten, "logicLowerCollimator", reg)

##cone collimator
solidTracker = _g4.solid.Tubs("solidTracker", 0., 8., 11.18, 0., 360., reg, "cm", "deg")
solidLower = _g4.solid.Subtraction("solidLower", solidTracker, solidLowerCollimator, [[0.,0.,0.],[0.,0.,0.]], reg)

##lower collimator
pos_lowerCollimator = _gdml.Position("pos_lowerCollimator", 0., 0., 6.5, "cm", reg)
logicLower = _g4.LogicalVolume(solidLower, tungsten, "logicLower", reg)
physLower = _g4.PhysicalVolume([0.,0.,0.], pos_lowerCollimator, logicLower, "physLower", logicWorld, reg, 0, True)

# #vacuum window
# pos_window = _gdml.Position("pos_window", 0., 0., 10., "cm", reg)
# solidWindow = _g4.solid.Tubs("solidWindow", 0., 36., 0.2, 0., 360., reg, "mm", "deg")
# logicWindow = _g4.LogicalVolume(solidWindow, berilium, "logicWindow", reg)
# physWindow = _g4.PhysicalVolume([0., 0., 0.], pos_window, logicWindow, "physWindow", logicWorld, reg)

#flattening filter
pos_flatteningfilter1 = _gdml.Position("pos_flatteningfilter1", 0., 0., 13., "cm", reg)
solidFilter1 = _g4.solid.Cons("solidFilter1", 0., 0.3, 0., 5, 3, 0., 360., reg, "cm", "deg")
logicFilter1 = _g4.LogicalVolume(solidFilter1, tungsten, "logicFilter1", reg)

pos_flatteningfilter2 = _gdml.Position("pos_flatteningfilter2", 0., 0., 15., "cm", reg)
solidFilter2 = _g4.solid.Tubs("solidFilter2", 0., 8., 1, 0., 360., reg, "cm", "deg")
logicFilter2 = _g4.LogicalVolume(solidFilter2, tungsten, "logicFilter2", reg)

physFilter1 = _g4.PhysicalVolume([0.,0.,0.], pos_flatteningfilter1, logicFilter1, "physFilter1", logicWorld, reg)
physFilter2 = _g4.PhysicalVolume([0.,0.,0.], pos_flatteningfilter2, logicFilter2, "physFilter2", logicWorld, reg)


# pos_flatteningfilter2 = _gdml.Position("pos_flatteningfilter2", 0., 0., 15.5405, "cm", reg)
# solidFilter2 = _g4.solid.Tubs("solidFilter2", 0., 2.5, 0.0405, 0., 360., reg, "cm", "deg")
# logicFilter2 = _g4.LogicalVolume(solidFilter2, stainless_steel, "logicFilter2", reg)
# physFIlter2 = _g4.PhysicalVolume([0.,0.,0.], pos_flatteningfilter2, logicFilter2, "physFilter2", logicWorld, reg)

# #ionizationchamber
# solidIonizationW = _g4.solid.Tubs("solidIonizationW", 0., 2.*2.54*10., 0.016*25.4, 0., 360., reg, "mm", "deg")
# solidIonizationP = _g4.solid.Tubs("solidIonizationP", 0., 2.*2.54*10., 0.010*25.4, 0., 360., reg, "mm", "deg")
# #W1
# pos_W1 = _gdml.Position("pos_W1", 0., 0., 157., "mm", reg)
# logicW1 = _g4.LogicalVolume(solidIonizationW, kapton, "logicW1", reg)
# physW1 = _g4.PhysicalVolume([0., 0., 0.], pos_W1, logicW1, "physW1", logicWorld, reg)

# #P1
# pos_P1 = _gdml.Position("pos_P1", 0., 0., 158., "mm", reg)
# logicP1 = _g4.LogicalVolume(solidIonizationP, kapton, "logicP1", reg)
# physP1 = _g4.PhysicalVolume([0., 0., 0.], pos_P1, logicP1, "physP1", logicWorld, reg)

# #W2
# pos_W2 = _gdml.Position("pos_W2", 0., 0., 159., "mm", reg)
# logicW2 = _g4.LogicalVolume(solidIonizationW, kapton, "logicW2", reg)
# physW2 = _g4.PhysicalVolume([0., 0., 0.], pos_W2, logicW2, "physW2", logicWorld, reg)

# #P2
# pos_P2 = _gdml.Position("pos_P2", 0., 0., 160., "mm", reg)
# logicP2 = _g4.LogicalVolume(solidIonizationP, kapton, "logicP2", reg)
# physP2 = _g4.PhysicalVolume([0., 0., 0.], pos_P2, logicP2, "physP2", logicWorld, reg)

# #W3
# pos_W3 = _gdml.Position("pos_W3", 0., 0., 161., "mm", reg)
# logicW3 = _g4.LogicalVolume(solidIonizationW, kapton, "logicW3", reg)
# physW3 = _g4.PhysicalVolume([0., 0., 0.], pos_W3, logicW3, "physW3", logicWorld, reg)

# #P3
# pos_P3 = _gdml.Position("pos_P3", 0., 0., 162., "mm", reg)
# logicP3 = _g4.LogicalVolume(solidIonizationP, kapton, "logicP3", reg)
# physP3 = _g4.PhysicalVolume([0., 0., 0.], pos_P3, logicP3, "physP3", logicWorld, reg)

# ##mirror
# pos_mirror = _gdml.Position("pos_mirror", 0., 0., 175., "mm", reg)
# rot_mirror = _gdml.Rotation("rot_mirror", 0., 12., 0., "deg", reg)
# solidMirror = _g4.solid.Tubs("soldiMirror", 0., 63., 0.5, 0., 360., reg, "mm", "deg")
# logicMirror = _g4.LogicalVolume(solidMirror, mylar, "logicMirror", reg)
# physMirror = _g4.PhysicalVolume(rot_mirror, pos_mirror, logicMirror, "physMirror", logicWorld, reg)

# JAW
# JAWX
pos_Jaw1X = _gdml.Position("pos_Jaw1X", 127., 0., 360., "mm", reg)
solidJaw1X = _g4.solid.Box("solidJaw1X", 12., 18.6, 8, reg, "cm")
logicJaw1X = _g4.LogicalVolume(solidJaw1X, tungsten, "logicJaw1X", reg)
physJaw1X = _g4.PhysicalVolume([0.,0.,0.], pos_Jaw1X, logicJaw1X, "physJaw1X", logicWorld, reg)

pos_Jaw2X = _gdml.Position("pos_Jaw2X", -135., 0., 360., "mm", reg)
solidJaw2X = _g4.solid.Box("solidJaw2X", 12., 18.6, 8, reg, "cm")
logicJaw2X = _g4.LogicalVolume(solidJaw2X, tungsten, "logicJaw2X", reg)
physJaw2X = _g4.PhysicalVolume([0.,0.,0.], pos_Jaw2X, logicJaw2X, "physJaw2X", logicWorld, reg)

##JAWY
pos_Jaw1Y = _gdml.Position("pos_Jaw1Y", 0., -190., 270., "mm", reg)
solidJaw1Y = _g4.solid.Box("solidJaw1Y", 18.6, 12, 8, reg, "cm")
logicJaw1Y = _g4.LogicalVolume(solidJaw1Y, tungsten, "logicJaw1Y", reg)
physJaw1Y = _g4.PhysicalVolume([0.,0.,0.], pos_Jaw1Y, logicJaw1Y, "physJaw1Y", logicWorld, reg)

pos_Jaw2Y = _gdml.Position("pos_Jaw2Y", 0., 110., 270., "mm", reg)
solidJaw2Y = _g4.solid.Box("solidJaw2Y", 18.6, 12, 8, reg, "cm")
logicJaw2Y = _g4.LogicalVolume(solidJaw2Y, tungsten, "logicJaw2Y", reg)
physJaw2Y = _g4.PhysicalVolume([0.,0.,0.], pos_Jaw2Y, logicJaw2Y, "physJaw2Y", logicWorld, reg)

# pos_Jaw3Y = _gdml.Position("pos_Jaw3Y", 0., 0., 60., "cm", reg)
# solidJaw4Y = _g4.solid.Box("solidJaw4Y", 14., 18., 10., reg, "cm")
# solidJaw3Y = _g4.solid.Box("solidJaw3Y", 40., 40., 10., reg, "cm")
# solidJaw = _g4.solid.Subtraction("solidJaw", solidJaw3Y, solidJaw4Y, [[0.,0.,0.],[-3.,-50.,0.]], reg)
# logicJaw3Y = _g4.LogicalVolume(solidJaw, tungsten, "logicJaw3Y", reg)
# physJaw3Y = _g4.PhysicalVolume([0.,0.,0.], pos_Jaw3Y, logicJaw3Y, "physJaw3Y", logicWorld, reg)

df = pd.read_csv("/home/labmedis/TA_aviv/code_python/MLC/PA.csv")
pos_MLC_A = df['leaf A converted'][:-1].tolist()
pos_MLC_B = df['leaf B converted'][:-1].tolist()

solidMLCCentral = _g4.solid.Box("solidMLCCentral", 150.,  5., 50., reg)
solidMLCSides = _g4.solid.Box("solidMLCSides", 150.,  10., 50., reg)
logicMLCCentral = _g4.LogicalVolume(solidMLCCentral, tungsten, "logicMLCCentral", reg)
logicMLCSides = _g4.LogicalVolume(solidMLCSides, tungsten, "logicMLCSides", reg)

for i in range(60):
    if i >= 0 and i < 20:
        _g4.PhysicalVolume([0., 0., 0.], [pos_MLC_A[i], -245+i*10, 480.], logicMLCSides, "leafA"+str(i), logicWorld, reg)    
    elif i >= 20 and i < 40:
        _g4.PhysicalVolume([0., 0., 0.], [pos_MLC_A[i], -47.5+(i-20)*5, 480.], logicMLCCentral, "leafA"+str(i), logicWorld, reg)  
    elif i >= 40:
        _g4.PhysicalVolume([0., 0., 0.], [pos_MLC_A[i], 55+(i-40)*10, 480.], logicMLCSides, "leafA"+str(i), logicWorld, reg) 

for i in range(60):
    if i >= 0 and i < 20:
        _g4.PhysicalVolume([0., 0., 0.], [pos_MLC_B[i], -245+i*10, 480.], logicMLCSides, "leafB"+str(i), logicWorld, reg)    
    elif i >= 20 and i < 40:
        _g4.PhysicalVolume([0., 0., 0.], [pos_MLC_B[i], -47.5+(i-20)*5, 480.], logicMLCCentral, "leafB"+str(i), logicWorld, reg)  
    elif i >= 40:
        _g4.PhysicalVolume([0., 0., 0.], [pos_MLC_B[i], 55+(i-40)*10, 480.], logicMLCSides, "leafB"+str(i), logicWorld, reg)

#phantom
pos_phantom = _gdml.Position("pos_phantom", 85., -70., 1000., "mm", reg)
rotation_phantom = _gdml.Rotation("rot_phantom", 90., 0., 0. -164.5, "deg", reg)

body_stl = _stl.Reader('body_phantom.stl', solidname="body",registry=reg)
solidBody = body_stl.getSolid()
logicBody = _g4.LogicalVolume(solidBody, softTissue, "logicBody", reg)
physBody = _g4.PhysicalVolume(rotation_phantom, pos_phantom, logicBody, "physBody", logicWorld, reg)

lungRT_stl = _stl.Reader('lungRT_phantom.stl', solidname="lungRT",registry=reg)
solidLungRT = lungRT_stl.getSolid()
logicLungRT = _g4.LogicalVolume(solidLungRT, paru, "logicLungRT", reg)
physLungRT = _g4.PhysicalVolume([0.,0.,0.], [0.,0.,0.], logicLungRT, "physLungRT", logicBody, reg)

lungLT_stl = _stl.Reader('lungLT_phantom.stl', solidname="lungLT", registry=reg)
solidLungLT = lungLT_stl.getSolid()
logicLungLT = _g4.LogicalVolume(solidLungLT, paru, "logicLungLT", reg)
physLungLT = _g4.PhysicalVolume([0.,0.,0.], [0.,0.,0.], logicLungLT, "physLungLT", logicBody, reg)

heart_stl = _stl.Reader('heart_phantom.stl', solidname="heart",registry=reg)
solidHeart = heart_stl.getSolid()
solidHeart = _g4.solid.Subtraction("solidHeart", solidHeart, solidLungRT, [[0.,0.,0.],[0.,0.,0.]], reg)
logicHeart = _g4.LogicalVolume(solidHeart, jantung, "logicHeart", reg)
physHeart = _g4.PhysicalVolume([0.,0.,0.], [0.,0.,0.], logicHeart, "physHeart", logicBody, reg)

PTV_stl = _stl.Reader('PTV_phantom.stl', solidname="PTV",registry=reg)
solidPTV = PTV_stl.getSolid()
logicPTV = _g4.LogicalVolume(solidPTV, softTissue, "logicPTV", reg)
physPTV = _g4.PhysicalVolume([0.,0.,0.], [0.,0.,0.], logicPTV, "physPTV", logicBody, reg)

spinalCord_stl = _stl.Reader('spinalCord_phantom.stl', solidname="spinal_cord",registry=reg)
solidSpinalCord = spinalCord_stl.getSolid()
logicSpinalCord = _g4.LogicalVolume(solidSpinalCord, softTissue, "logicSpinalCord", reg)
physSpinalCord = _g4.PhysicalVolume([0.,0.,0.], [0.,0.,0.], logicSpinalCord, "physSpinalCord", logicBody, reg)

trakea_stl = _stl.Reader('trakea_phantom.stl', solidname="trakea",registry=reg)
solidTrakea = trakea_stl.getSolid()
solidTrakea = _g4.solid.Subtraction("solidTrakea", solidTrakea, solidLungRT, [[0.,0.,0.],[0.,0.,0.]], reg)
logicTrakea = _g4.LogicalVolume(solidTrakea, softTissue, "logicTrakea", reg)
physTrakea = _g4.PhysicalVolume([0.,0.,0.], [0.,0.,0.], logicTrakea, "physTrakea", logicBody, reg)

vi = _pyg.visualisation.VtkViewer()
vi.addLogicalVolume(logicWorld)
# vi.setRandomColours()
vi.view()

# write = _gdml.Writer()
# write.addDetector(reg)
# write.write("phantom_PA.gdml")