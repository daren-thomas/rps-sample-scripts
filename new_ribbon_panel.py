"""
new_ribbon_panel.py - a startup script to create a selection of
controls on the ribbon.

This script is based on the New Ribbon Panel and Controls example in the
Revit API Devolopers Guide.

NOTE:
    - this MUST be set as a startup script for it to work
    - the RPS variable "EXAMPLES_PATH" must be set and contain "helloworld.py"
"""

import os
from RevitPythonShell.RpsRuntime import ExternalCommandAssemblyBuilder
from Autodesk.Revit.UI import *

SCRIPT_PATH = os.path.join(__vars__['EXAMPLES_PATH'], "helloworld.py")
DLL_PATH = os.path.expandvars(r"%APPDATA%\RevitPythonShell2015\simple_ribbon.dll")
print 'storing external command assembly here:', DLL_PATH

def create_ribbon_panel():
    panel = __uiControlledApplication__.CreateRibbonPanel("New Ribbon Panel")
    add_radio_group(panel)
    panel.AddSeparator()
    add_push_button(panel)
    panel.AddSeparator()
    add_split_button(panel)
    panel.AddSeparator()
    add_stacked_buttons(panel)
    panel.AddSeparator()
    add_slide_out(panel)

if __name__ == '__main__':
    try:
        create_ribbon_panel()
    except:
        import traceback
        traceback.print_exc()
