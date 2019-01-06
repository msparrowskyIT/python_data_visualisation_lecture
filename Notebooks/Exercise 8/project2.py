from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import sys

app = QApplication(sys.argv)

# VTK
stl_frame = QFrame()
stl_widget = QVTKRenderWindowInteractor(stl_frame)

# LIST FILE / DELETE
list_delete_grid = QGridLayout()

list_widget = QListWidget()

def show():
    list(map(lambda i: list_widget.item(i).setCheckState(Qt.Unchecked), range(list_widget.count())))
    list_widget.currentItem().setCheckState(Qt.Checked)

    stl_reader = vtk.vtkSTLReader()
    stl_reader.SetFileName(directory_path.text() + "/" + list_widget.currentItem().text())
    stl_reader.Update()
    # Create mapper
    stl_mapper = vtk.vtkPolyDataMapper()
    stl_mapper.SetInputConnection(stl_reader.GetOutputPort())
    # Create actor
    stl_actor = vtk.vtkActor()
    stl_actor.SetMapper(stl_mapper)
    # Create renderer
    stl_renderer = vtk.vtkRenderer()
    stl_renderer.AddActor(stl_actor)
    stl_widget.GetRenderWindow().AddRenderer(stl_renderer)
    # Create interactor
    stl_interactor = stl_widget.GetRenderWindow().GetInteractor()
    stl_interactor.Initialize()
    stl_interactor.Start()
    
list_widget.itemDoubleClicked.connect(show)
list_delete_grid.addWidget(list_widget, 0,0,0,4)

def delete_file():
    global list_widget
    row = list_widget.row(list_widget.currentItem())
    list_widget.takeItem(row)
#     list_widget.removeItemWidget(list_widget.currentItem()) -> z jakiegoś powodu nie działa? hmm

delete_file_btn = QPushButton("Delete")
delete_file_btn.clicked.connect(delete_file)
list_delete_grid.addWidget(delete_file_btn, 0,5,0,6, Qt.AlignTop)


# BROWSE / LOAD FILE
browse_load_grid = QGridLayout()
browse_load_grid.addWidget(QLabel("Select folder to load:"), 0,0)

directory_path = QLineEdit()
directory_path.setReadOnly(True)
browse_load_grid.addWidget(directory_path, 0,1,0,4)

browsed_files = []

def browse_files():
    global browsed_files
    global directory_path

    browse_dlg = QFileDialog()
    browse_dlg.setFileMode(QFileDialog.ExistingFiles)
    browse_dlg.setNameFilter("*.stl")
    if browse_dlg.exec_():
        b =  browse_dlg.selectedFiles()
        browsed_files = [(file.split("/")[-1], file) for file in browse_dlg.selectedFiles()]
        directory_path.setText(browse_dlg.directory().absolutePath())

browse_files_btn = QPushButton("Browse")
browse_files_btn.clicked.connect(browse_files)
browse_load_grid.addWidget(browse_files_btn, 0,5)

loaded_files = []

def create_list_item(name):
    global list_widget

    list_item = QListWidgetItem(name, list_widget)
    list_item.setCheckState(Qt.Unchecked)
    return list_item

def load_files():
    global list_widget
    global browse_files

    list_widget.clear()
    loaded_files = browsed_files
    list(map(lambda f: list_widget.addItem(create_list_item(f[0])), loaded_files))

load_files_btn = QPushButton("Load")
load_files_btn.clicked.connect(load_files)
browse_load_grid.addWidget(load_files_btn, 0,6)

# CLOSE
def app_close(checked):
    app.quit()

close_btn = QPushButton("Close")
close_btn.clicked.connect(app_close)

# VERTICAL POSITIONS
vert_box = QVBoxLayout()
vert_box.addLayout(browse_load_grid)
vert_box.addLayout(list_delete_grid)
vert_box.addWidget(QLabel("VTK Preview of selected items:"))
vert_box.addWidget(stl_widget)
vert_box.addWidget(close_btn)

app_win = QWidget()
app_win.setLayout(vert_box)
app_win.show()
app.exec_()