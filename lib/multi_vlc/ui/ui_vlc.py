# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/vlc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VlcMainWindow(object):
    def setupUi(self, VlcMainWindow):
        VlcMainWindow.setObjectName("VlcMainWindow")
        VlcMainWindow.resize(1177, 474)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VlcMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(VlcMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setDefaultSectionSize(120)
        self.tableView.horizontalHeader().setMinimumSectionSize(100)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        VlcMainWindow.setCentralWidget(self.centralwidget)
        self.statusBarObj = QtWidgets.QStatusBar(VlcMainWindow)
        self.statusBarObj.setObjectName("statusBarObj")
        VlcMainWindow.setStatusBar(self.statusBarObj)
        self.menuBarObj = QtWidgets.QMenuBar(VlcMainWindow)
        self.menuBarObj.setGeometry(QtCore.QRect(0, 0, 1177, 20))
        self.menuBarObj.setObjectName("menuBarObj")
        self.menuFile = QtWidgets.QMenu(self.menuBarObj)
        self.menuFile.setObjectName("menuFile")
        self.menuVideo = QtWidgets.QMenu(self.menuBarObj)
        self.menuVideo.setObjectName("menuVideo")
        self.menu_Position = QtWidgets.QMenu(self.menuBarObj)
        self.menu_Position.setObjectName("menu_Position")
        VlcMainWindow.setMenuBar(self.menuBarObj)
        self.toolBar = QtWidgets.QToolBar(VlcMainWindow)
        self.toolBar.setObjectName("toolBar")
        VlcMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdd = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.actionAdd.setIcon(icon)
        self.actionAdd.setObjectName("actionAdd")
        self.actionDelete = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.actionDelete.setIcon(icon)
        self.actionDelete.setObjectName("actionDelete")
        self.actionReset = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("document-revert")
        self.actionReset.setIcon(icon)
        self.actionReset.setObjectName("actionReset")
        self.actionLoad = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.actionLoad.setIcon(icon)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("document-save")
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionFind_Opened = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("edit-find")
        self.actionFind_Opened.setIcon(icon)
        self.actionFind_Opened.setObjectName("actionFind_Opened")
        self.actionSet_Position = QtWidgets.QAction(VlcMainWindow)
        self.actionSet_Position.setCheckable(True)
        icon = QtGui.QIcon.fromTheme("document-page-setup")
        self.actionSet_Position.setIcon(icon)
        self.actionSet_Position.setObjectName("actionSet_Position")
        self.actionStart = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.actionStart.setIcon(icon)
        self.actionStart.setObjectName("actionStart")
        self.actionClose = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("process-stop")
        self.actionClose.setIcon(icon)
        self.actionClose.setObjectName("actionClose")
        self.actionPause = QtWidgets.QAction(VlcMainWindow)
        self.actionPause.setCheckable(True)
        icon = QtGui.QIcon.fromTheme("media-playback-pause")
        self.actionPause.setIcon(icon)
        self.actionPause.setObjectName("actionPause")
        self.actionSave_As = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.actionSave_As.setIcon(icon)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionAssign = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("zoom-fit-best")
        self.actionAssign.setIcon(icon)
        self.actionAssign.setObjectName("actionAssign")
        self.actionMove_Down = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("go-down")
        self.actionMove_Down.setIcon(icon)
        self.actionMove_Down.setObjectName("actionMove_Down")
        self.actionMove_Up = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("go-up")
        self.actionMove_Up.setIcon(icon)
        self.actionMove_Up.setObjectName("actionMove_Up")
        self.actionNew = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionShuffle = QtWidgets.QAction(VlcMainWindow)
        icon = QtGui.QIcon.fromTheme("media-playlist-shuffle")
        self.actionShuffle.setIcon(icon)
        self.actionShuffle.setObjectName("actionShuffle")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionReset)
        self.menuVideo.addAction(self.actionAdd)
        self.menuVideo.addAction(self.actionDelete)
        self.menuVideo.addAction(self.actionMove_Down)
        self.menuVideo.addAction(self.actionMove_Up)
        self.menuVideo.addAction(self.actionShuffle)
        self.menuVideo.addSeparator()
        self.menuVideo.addAction(self.actionStart)
        self.menuVideo.addAction(self.actionPause)
        self.menuVideo.addAction(self.actionClose)
        self.menu_Position.addAction(self.actionFind_Opened)
        self.menu_Position.addAction(self.actionSet_Position)
        self.menu_Position.addAction(self.actionAssign)
        self.menuBarObj.addAction(self.menuFile.menuAction())
        self.menuBarObj.addAction(self.menuVideo.menuAction())
        self.menuBarObj.addAction(self.menu_Position.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionReset)
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addAction(self.actionMove_Down)
        self.toolBar.addAction(self.actionMove_Up)
        self.toolBar.addAction(self.actionShuffle)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFind_Opened)
        self.toolBar.addAction(self.actionSet_Position)
        self.toolBar.addAction(self.actionAssign)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionClose)

        self.retranslateUi(VlcMainWindow)
        QtCore.QMetaObject.connectSlotsByName(VlcMainWindow)

    def retranslateUi(self, VlcMainWindow):
        _translate = QtCore.QCoreApplication.translate
        VlcMainWindow.setWindowTitle(_translate("VlcMainWindow", "[*]VLC Manager[*]"))
        self.menuFile.setTitle(_translate("VlcMainWindow", "&File"))
        self.menuVideo.setTitle(_translate("VlcMainWindow", "&Video"))
        self.menu_Position.setTitle(_translate("VlcMainWindow", "&Position"))
        self.toolBar.setWindowTitle(_translate("VlcMainWindow", "toolBar"))
        self.actionAdd.setText(_translate("VlcMainWindow", "&Add"))
        self.actionDelete.setText(_translate("VlcMainWindow", "&Delete"))
        self.actionDelete.setShortcut(_translate("VlcMainWindow", "Del"))
        self.actionReset.setText(_translate("VlcMainWindow", "&Reset"))
        self.actionLoad.setText(_translate("VlcMainWindow", "&Open"))
        self.actionLoad.setToolTip(_translate("VlcMainWindow", "Open"))
        self.actionLoad.setShortcut(_translate("VlcMainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("VlcMainWindow", "&Save"))
        self.actionSave.setShortcut(_translate("VlcMainWindow", "Ctrl+S"))
        self.actionFind_Opened.setText(_translate("VlcMainWindow", "&Find Opened"))
        self.actionFind_Opened.setToolTip(_translate("VlcMainWindow", "Find Opened"))
        self.actionSet_Position.setText(_translate("VlcMainWindow", "&Set Position"))
        self.actionStart.setText(_translate("VlcMainWindow", "&Start"))
        self.actionClose.setText(_translate("VlcMainWindow", "&Close"))
        self.actionClose.setShortcut(_translate("VlcMainWindow", "Ctrl+Esc"))
        self.actionPause.setText(_translate("VlcMainWindow", "&Pause"))
        self.actionPause.setShortcut(_translate("VlcMainWindow", "Space"))
        self.actionSave_As.setText(_translate("VlcMainWindow", "Save &As"))
        self.actionSave_As.setShortcut(_translate("VlcMainWindow", "Ctrl+Shift+S"))
        self.actionAssign.setText(_translate("VlcMainWindow", "&Assign"))
        self.actionAssign.setToolTip(_translate("VlcMainWindow", "Assign"))
        self.actionMove_Down.setText(_translate("VlcMainWindow", "&Move Down"))
        self.actionMove_Up.setText(_translate("VlcMainWindow", "Move &Up"))
        self.actionMove_Up.setToolTip(_translate("VlcMainWindow", "Move Up"))
        self.actionNew.setText(_translate("VlcMainWindow", "&New"))
        self.actionNew.setShortcut(_translate("VlcMainWindow", "Ctrl+N"))
        self.actionShuffle.setText(_translate("VlcMainWindow", "S&huffle"))
