# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:05:23 2016

@author: jessica
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QLineEdit
import FreeCAD, FreeCADGui, Draft
import importAirfoilDAT
 
# Select .dat airfoil data file to be imported
 
filename = QtGui.QFileDialog.getOpenFileName(QtGui.qApp.activeWindow(),'Open An Airfoil File','*.dat')
 
class p():
 
    def proceed(self):
            try:
 
                # This produces a scaled Airfoil with a DWire
 
                scalefactor=float(self.s1.text())
                f1=str(filename)
                importAirfoilDAT.insert(f1,"Unnamed")
                Draft.scale(App.ActiveDocument.ActiveObject,delta=App.Vector(scalefactor,scalefactor,scalefactor),center=App.Vector(0,0,0),legacy=True)
 
            except:
                FreeCAD.Console.PrintError("Error, not a valid .dat file\n")
 
            self.close()
 
    def close(self):
        self.dialog.hide()
 
    def __init__(self):
        self.dialog = None
        self.s1 = None
 
        # Make dialog box and get the scale size
 
        self.dialog = QtGui.QDialog()
        self.dialog.resize(350,100)
        self.dialog.setWindowTitle("Airfoil Import & Scale")
        la = QtGui.QVBoxLayout(self.dialog)
        t1 = QtGui.QLabel("Chord Length")
        la.addWidget(t1)
        self.s1 = QtGui.QLineEdit()
        la.addWidget(self.s1)
 
        # Add OK / Cancel buttons
 
        okbox = QtGui.QDialogButtonBox(self.dialog)
        okbox.setOrientation(QtCore.Qt.Horizontal)
        okbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        la.addWidget(okbox)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("accepted()"), self.proceed)
        QtCore.QObject.connect(okbox, QtCore.SIGNAL("rejected()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self.dialog)
        self.dialog.show()
        self.dialog.exec_()
 
p()