import pyg4ometry

read = pyg4ometry.gdml.Reader("phantom_water.gdml")
reg = read.getRegistry()
logicWorld = reg.getWorldVolume()

vi = pyg4ometry.visualisation.VtkViewer()
vi.addLogicalVolume(logicWorld)
# vi.setRandomColours()
vi.view()
