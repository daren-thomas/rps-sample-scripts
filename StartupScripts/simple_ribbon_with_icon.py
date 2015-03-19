'''
simple_ribbon_with_icon.py - creates a ribbon panel with a single push button.

NOTE:
    - this MUST be set as a startup script for it to work
    - the RPS variable "EXAMPLES_PATH" must be set and contain "helloworld.py"
'''
import clr
clr.AddReference('PresentationCore')
from System.Windows.Media.Imaging import BitmapImage
from System import Uri

# script that is run when Revit starts in the IExternalApplication.Startup event.
try:
    import os
    from RevitPythonShell.RpsRuntime import ExternalCommandAssemblyBuilder
    from Autodesk.Revit.UI import *

    SCRIPT_PATH = os.path.join(__vars__['EXAMPLES_PATH'], "helloworld.py")
    LARGE_IMG_PATH = os.path.join(__vars__['EXAMPLES_PATH'], "PythonScript32x32.png")
    SMALL_IMG_PATH = os.path.join(__vars__['EXAMPLES_PATH'], "PythonScript16x16.png")
    DLL_PATH = os.path.expandvars(r"%APPDATA%\RevitPythonShell2015\simple_ribbon_with_icon.dll")
    print 'storing external command assembly here:', DLL_PATH

    builder = ExternalCommandAssemblyBuilder()
    builder.BuildExternalCommandAssembly(
        DLL_PATH,
        {'HelloWorld': SCRIPT_PATH})

    panel = __uiControlledApplication__.CreateRibbonPanel('simple_ribbon (with icon)')

    pbd = PushButtonData('pb_HelloWorld', 'hello, world!', DLL_PATH, 'HelloWorld')
    pbd.LargeImage = BitmapImage(Uri(LARGE_IMG_PATH))
    pbd.Image = BitmapImage(Uri(SMALL_IMG_PATH))
    panel.AddItem(pbd)

    #__window__.Close()  # closes the window
except:
    import traceback       # note: add a python27 library to your search path first!
    traceback.print_exc()  # helps you debug when things go wrong
