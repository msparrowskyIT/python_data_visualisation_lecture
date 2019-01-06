import vtk

def create_cube_actor(shape=(0.0, 0.0, 0.0), position=(0.0, 0.0, 0.0), color=(0.0, 0.0, 0.0)):

    cube = vtk.vtkCubeSource()
    cube.SetXLength(shape[0])
    cube.SetYLength(shape[1])
    cube.SetZLength(shape[2])

    cube_mapper = vtk.vtkPolyDataMapper()
    cube_mapper.SetInputConnection(cube.GetOutputPort())

    cube_actor = vtk.vtkActor()
    cube_actor.SetMapper(cube_mapper)
    cube_actor.GetProperty().SetColor(*color)
    cube_actor.SetPosition(*position)

    return cube_actor

red_cube_actor = create_cube_actor(shape=(2.5, 3.5, 4.5), color=(1.0, 0.0, 0.0))
green_cube_actor = create_cube_actor(shape=(2.5, 3.5, 4.5), position=(0.0, 10.0, 0.0), color=(0.0, 1.0, 0.0))
blue_cube_actor = create_cube_actor(shape=(2.5, 3.5, 4.5), position=(10.0, 0.0, 0.0), color=(0.0, 0.0, 1.0))
yellow_cube_actor = create_cube_actor(shape=(2.5, 3.5, 4.5), position=(10.0, 10.0, 0.0), color=(0.0, 1.0, 1.0))

renderer = vtk.vtkRenderer()
renderer.AddActor(red_cube_actor)
renderer.AddActor(green_cube_actor)
renderer.AddActor(blue_cube_actor)
renderer.AddActor(yellow_cube_actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)

window.Render()
interactor.Initialize()
interactor.Start()