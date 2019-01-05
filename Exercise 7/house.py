import vtk

def load_actor(file_path):
    reader = vtk.vtkOBJReader()
    reader.SetFileName(file_path)
    reader.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    return actor

# house
house_actor = load_actor("house_obj/house.obj")
house_actor.GetProperty().SetColor(0.396, 0.263, 0.129)

house_transform = vtk.vtkTransform() 
house_transform.Scale(0.1, 0.1, 0.1)
house_actor.SetUserTransform(house_transform)

#lego
lego_actor = load_actor("house_obj/lego_man.obj")
lego_actor.GetProperty().SetColor(1.0, 1.0, 0)
lego_actor.SetPosition(0, 0, 20)
lego_actor.RotateY(180)

renderer = vtk.vtkRenderer()
renderer.AddActor(house_actor)
renderer.AddActor(lego_actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(window)
interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

window.Render()
interactor.Initialize()
interactor.Start()