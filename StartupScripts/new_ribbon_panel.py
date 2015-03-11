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
import clr
clr.AddReference('PresentationCore')
from System.Windows.Media.Imaging import BitmapImage
from System import Uri
from RevitPythonShell.RpsRuntime import ExternalCommandAssemblyBuilder
from Autodesk.Revit.UI import *

SCRIPT_PATH = os.path.join(__vars__['EXAMPLES_PATH'], "helloworld.py")
LARGE_IMG_PATH = os.path.join(__vars__['EXAMPLES_PATH'], "PythonScript32x32.png")
SMALL_IMG_PATH = os.path.join(__vars__['EXAMPLES_PATH'], "PythonScript16x16.png")
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


def add_radio_group(panel):
    """add radio button group"""
    radio_data = RadioButtonGroupData("radioGroup")
    radio_button_group = panel.AddItem(radio_data)

    tb1 = ToggleButtonData("toggleButton1", "Red")
    tb1.ToolTip = "Red Option"
    tb1.LargeImage = BitmapImage(Uri(LARGE_IMG_PATH))
    tb1.Image = BitmapImage(Uri(SMALL_IMG_PATH))

    tb2 = ToggleButtonData("toggleButton2", "Green")
    tb2.ToolTip = "Green Option"
    tb2.LargeImage = BitmapImage(Uri(LARGE_IMG_PATH))
    tb2.Image = BitmapImage(Uri(SMALL_IMG_PATH))

    tb3 = ToggleButtonData("toggleButton3", "Blue")
    tb3.ToolTip = "Blue Option"
    tb3.LargeImage = BitmapImage(Uri(LARGE_IMG_PATH))
    tb3.Image = BitmapImage(Uri(SMALL_IMG_PATH))

    radio_button_group.AddItem(tb1)
    radio_button_group.AddItem(tb2)
    radio_button_group.AddItem(tb3)


def add_push_button(panel):
    pass


def add_split_button(panel):
    pass


def add_stacked_buttons(panel):
    pass


def add_slide_out(panel):
    pass


if __name__ == '__main__':
    try:
        builder = ExternalCommandAssemblyBuilder()
        builder.BuildExternalCommandAssembly(
            DLL_PATH,
            {'HelloWorld': SCRIPT_PATH})
        create_ribbon_panel()
    except:
        import traceback
        traceback.print_exc()
