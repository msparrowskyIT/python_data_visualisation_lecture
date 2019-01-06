import vtk

cube = vtk.vtkCubeSource()
cube.SetXLength(2.5)
cube.SetYLength(3.5)
cube.SetZLength(4.5)

cube_mapper = vtk.vtkPolyDataMapper()
cube_mapper.SetInputConnection(cube.GetOutputPort())

cube_actor = vtk.vtkActor()
cube_actor.SetMapper(cube_mapper)
cube_actor.SetPosition(0.0, 0.0, 0.0)

renderer = vtk.vtkRenderer()
renderer.AddActor(cube_actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

window.Render()
interactor.Initialize()
interactor.Start()