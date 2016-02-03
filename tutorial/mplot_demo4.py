"""
Mplot demo - run multiplot example
"""

import enaml
from enaml.qt.qt_application import QtApplication


def run_demo():
    with enaml.imports():
        from mplot_demo_docks import Main

    app = QtApplication()

    view = Main(custom_title='Matplotlib demo', mplot_style='darkish')
    view.show()

    # Start the application event loop
    app.start()


run_demo()
