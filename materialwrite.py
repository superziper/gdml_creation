import pyg4ometry as _pyg
import pyg4ometry.stl as _stl 
import pyg4ometry.gdml as _gdml
import pyg4ometry.geant4 as _g4
import pyg4ometry.visualisation.VtkViewer as _vtk

reg = _g4.Registry()

air = _g4.nist_material_2geant4Material("G4_LUNG_ICRP", reg)

solidWorld = _g4.solid.Box("solidWorld", 1, 1, 3, reg, "m")
logicWorld = _g4.LogicalVolume(solidWorld, air, "logicWorld", reg)

reg.setWorld(logicWorld.name)

write = _gdml.Writer()
write.addDetector(reg)
write.write("material.gdml")