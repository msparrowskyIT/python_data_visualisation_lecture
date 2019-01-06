from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

app = QApplication(sys.argv)

# SELECT IMAGE
img_path_input = QLineEdit()

def load_img():
    global img_lbl
    global img_path_input
    
    if not img_path_input.text(): 
        browse_dlg = QFileDialog()
        browse_dlg.setFileMode(QFileDialog.ExistingFile)
        browse_dlg.setNameFilters(["*.png", "*.jpg"])    
        if(browse_dlg.exec_()):
            img_path = browse_dlg.selectedFiles()
            img_path_input.setText(img_path[0])
    
    img_lbl.setPixmap(QPixmap(img_path_input.text()))

img_select_btn = QPushButton("Select")
img_select_btn.clicked.connect(load_img)

select_grid = QGridLayout()
select_grid.addWidget(QLabel("Image to open:"), 0,0)
select_grid.addWidget(img_path_input, 0,1,0,5)
select_grid.addWidget(img_select_btn, 0,6)

# CONVERT IMAGE
r_weight_input = QLineEdit()
g_weight_input = QLineEdit()
b_weight_input = QLineEdit()

def convert_img():
    global img_lbl
    global r_weight_input
    global g_weight_input
    global b_weight_input
    
    img_pixmap = img_lbl.pixmap()
    if img_pixmap and r_weight_input and g_weight_input and b_weight_input:
        img = img_pixmap.toImage()
        r_weight, g_weight, b_weight = float(r_weight_input.text()), float(g_weight_input.text()), float(b_weight_input.text())
        weights = sum([r_weight, g_weight, b_weight])
        for w in range(img.width()):
            for h in range(img.height()):
                color = img.pixelColor(w, h)
                new_color = QColor(r_weight/weights*color.red(), g_weight/weights*color.green(), b_weight/weights*color.blue())
                img.setPixelColor(w, h, new_color) 

        img_lbl.setPixmap(QPixmap(img))      

img_convert_btn = QPushButton("Convert")
img_convert_btn.clicked.connect(convert_img)

convert_grid = QGridLayout()
convert_grid.addWidget(QLabel("Red weight:"), 1,0)
convert_grid.addWidget(r_weight_input, 1,1)
convert_grid.addWidget(QLabel("Green weight:"), 1,2)
convert_grid.addWidget(g_weight_input, 1,3)
convert_grid.addWidget(QLabel("Blue weight:"), 1,4)
convert_grid.addWidget(b_weight_input, 1,5)
convert_grid.addWidget(img_convert_btn, 1,6)

# convert_grid.addWidget(QLabel("Convert to grayscale:"), 0,0)
# convert_grid.addWidget(QLabel("Assume the colors are in range 0-255."), 2,0)

# IMAGE
img_lbl = QLabel()
img_lbl.setAlignment(Qt.AlignCenter)
img_lbl.setFixedHeight(500)
img_lbl.setFixedWidth(1000)

#OPERATIONS
def save_as_img():
    img_pixmap = img_lbl.pixmap()
    if img_pixmap:
        img_save_path = QFileDialog().getSaveFileName()
        img_pixmap.save(img_save_path[0])

img_save_as_btn = QPushButton("Save As")
img_save_as_btn.clicked.connect(save_as_img)

def app_close(checked):
    app.quit()

close_btn = QPushButton("Close")
close_btn.clicked.connect(app_close)

operation_grid = QGridLayout()
operation_grid.addWidget(img_save_as_btn, 0,0)
operation_grid.addWidget(close_btn, 0,1)

# VERTICAL BOX
vert_box = QVBoxLayout()
vert_box.addLayout(select_grid)
vert_box.addWidget(QLabel("Convert to grayscale:"))
vert_box.addLayout(convert_grid)
vert_box.addWidget(QLabel("Assume the colors are in range 0-255."))
vert_box.addWidget(img_lbl)
vert_box.addLayout(operation_grid)
vert_box.addStretch()

app_win = QWidget()
app_win.setLayout(vert_box)
app_win.show()
app.exec()