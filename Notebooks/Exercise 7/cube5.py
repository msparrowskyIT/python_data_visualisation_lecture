import vtk

points = vtk.vtkPoints()
points.InsertNextPoint(0.0, 0.0, 0.0)
points.InsertNextPoint(0.0, 10.0, 0.0)
points.InsertNextPoint(10.0, 0.0, 0.0)
points.InsertNextPoint(10.0, 10.0, 0.0)

colors = vtk.vtkUnsignedCharArray()
colors.SetName("colors")
colors.SetNumberOfComponents(3)
colors.InsertNextTuple((255, 0, 0))
colors.InsertNextTuple((0, 255, 0))
colors.InsertNextTuple((0, 0, 255))
colors.InsertNextTuple((255, 255, 0))

poly_data = vtk.vtkPolyData()
poly_data.SetPoints(points)
poly_data.GetPointData().SetScalars(colors)

cube = vtk.vtkCubeSource()
cube.SetXLength(2.5)
cube.SetYLength(3.5)
cube.SetZLength(4.5)

glyph3D = vtk.vtkGlyph3D()
glyph3D.SetSourceConnection(cube.GetOutputPort())
glyph3D.SetColorModeToColorByScalar()
glyph3D.SetInputData(poly_data)
glyph3D.ScalingOff()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(glyph3D.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)
interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

window.Render()
interactor.Initialize()
interactor.Start()