"""
vtk demo
"""

import enaml
from enaml.qt.qt_application import QtApplication


def run_demo():
    """
    bootstrap enaml in python
    """
    with enaml.imports():
        from vtk_sample_grid_view import Main

    app = QtApplication()

    view = Main(custom_title='VTK Sample Grid Smaple Demo')
    view.show()

    # Start the application event loop
    app.start()


run_demo()




