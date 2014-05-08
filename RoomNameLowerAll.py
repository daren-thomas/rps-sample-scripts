#RoomNameLowerAll
#dwane@dsdraughting.com
#2014
#
#import libraries and reference the RevitAPI and RevitAPIUI
import clr
import math
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

# to access all the Name-spaces in the RevitAPI & UI, we import them all using *
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

#set the active Revit application and document
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
selection = __revit__.ActiveUIDocument.Selection.Elements

#define a transaction variable and describe the transaction
t = Transaction(doc, 'rename all room names to lower case')

#start a transaction in the Revit database 
t.Start()

#perform some action here...
collector1 = FilteredElementCollector(doc)
collector1.OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()
elementSet1 = collector1.ToElements()

for rooms in elementSet1:
	currentRoomName = rooms.get_Parameter('Name').AsString()
	print 'Old Name = ' + currentRoomName
	newRoomName = currentRoomName.lower()		
	print 'New Name = ' + newRoomName
	rooms.get_Parameter(BuiltInParameter.ROOM_NAME).Set(newRoomName)
	
#commit the transaction to the Revit database
t.Commit()

#close the script window
__window__.Close()
