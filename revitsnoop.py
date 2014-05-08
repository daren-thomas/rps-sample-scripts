'''
Launch a RevitLookup "Snoop Objects" dialog for elements from the RPS shell

= Introduction =

You _do_ have `RevitLookup` installed, don't you? This is _the_ tool for
introspecting model elements. You can find it in the Revit SDK folder, along
with the source code. The plugin does many things, among which I most often use
the "Snoop Current Selection..." feature. This pops up a nice dialog that lets
you snoop around in the selected elements properties. See here for more:
https://github.com/jeremytammik/RevitLookup

I find that RevitLookup and RevitPythonShell complement each other rather well.
Except, while inside the shell, you can't start any other plugins, so  you
can't access the snoop functionality. Unless...

= Details =

The module `revitsnoop` provides a mechanism to hook into the RevitLookup
plugin and start it with an object of your choice.

Example:

{{{
>>>import revitsnoop

>>>snooper = revitsnoop.RevitSnoop(__revit__)

>>>snooper.snoop(doc.ProjectInformation)
}}}

This will pop up a dialog for snooping the documents project information. You
can of course snoop any `Element` object.
'''
import clr
from Autodesk.Revit.DB import ElementSet


class RevitSnoop(object):
    def __init__(self, uiApplication):
        '''
        for RevitSnoop to function properly, it needs to be instantiated
        with a reverence to the Revit Application object.
        '''
        # find the RevitLookup plugin
        rlapp = [app for app in uiApplication.LoadedApplications
                 if app.GetType().Namespace == 'RevitLookup'
                 and app.GetType().Name == 'App'][0]
        # tell IronPython about the assembly of the RevitLookup plugin
        clr.AddReference(rlapp.GetType().Assembly)
        import RevitLookup
        self.RevitLookup = RevitLookup
        # See note in CelloctorExt.cs in the RevitLookup source:
        self.RevitLookup.Snoop.CollectorExts.CollectorExt.m_app = uiApplication

    def snoop(self, element):
        elementSet = ElementSet()
        elementSet.Insert(element)
        form = self.RevitLookup.Snoop.Forms.Objects(elementSet)
        form.ShowDialog()
