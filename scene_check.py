# -*- coding: utf-8 -*-

# from maya import cmds
# from maya import mel

from maya import OpenMayaUI as OMUI
import os
from  inspect import getsourcefile

# 到入check_fun时，需要先将文件路径添加进来。
import sys
file_path =  os.path.abspath(getsourcefile(lambda : 0))
sys.path.append(file_path.replace(file_path.split('\\')[-1], ""))
import check_fun

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2.QtUiTools import *
    from shiboken2 import wrapInstance
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide.QtUiTools import *
    from shiboken import wrapInstance


mayaMainWindowPtr = OMUI.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)

class SceneCheck(QWidget):


    def __init__(self, *args, **kwargs):
        super(SceneCheck, self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Scene Clean up场景清理")
        self.initUI()

    def initUI(self):
        loader = QUiLoader()
        file_path =  os.path.abspath(getsourcefile(lambda : 0)) #获取脚本的绝对路径
        currentUI = file_path.replace(file_path.split('\\')[-1], "scene_check.ui")
        #currentUI = file_path.replace(".py", ".ui")             #获取UI的的绝对路径
        print ("current file path:"+file_path)
        file = QFile( currentUI)
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, parentWidget=self)
        self.ui.dp_name_check_btn.clicked.connect(self.check_dp_names)
        self.ui.bs_check_btn.clicked.connect(self.check_bs_values)
        self.ui.bindpose_check_btn.clicked.connect(self.check_bindpose)
    def check_dp_names(self):
        check_fun.duplicated_transform_nodes_check()
    def check_bs_values(self):
        check_fun.init_blendshape_check()
    def check_bindpose(self):
        check_fun.bindpose_check()

def main():
    ui = SceneCheck()
    ui.show()
    return ui

if __name__ == '__main__':
    main()
