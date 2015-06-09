rps-sample-scripts
==================

A collection of sample scripts for the RevitPythonShell (https://code.google.com/p/revitpythonshell)

This is a repository for short RPS scripts that have no other place to stay.

  * exportImage.py - export the currently visible view as a PNG image
  * revitsnoop.py - interface to the RevitLookup tool by Jeremy Tammik

Dwane Stairmand posted some scripts to the RevitPythonShell user group (http://groups.google.com/group/RevitPythonShell)

  * RoomNameLower.py - room names to lower-case (selected)
  * RoomNameLowerAll.py - room names to lower-case (all)
  * RoomNameUpper.py - room names to upper-case (selected)
  * RoomNameUpperAll.py - room names to uper-case (all>)
  * SelectAllText.py - select all the text within a project (ready for the spell check)
  * SheetNameLowerAll.py - sheet name to lower-case (all)
  * SheetNameUpperAll.py - sheet name to upper-case (all)
  * TextLower.py - text to lower-case (selected)
  * TextLowerAll.py - text to lower-case (all)
  * TextUpper.py - text to upper-case (selected)
  * TextUpperAll.py - text to upper-case (all)

# StartupScripts

The folder `StartupScripts` contains some examples of using the startup script
functionality in RPS. The blog post [More control over the RibbonPanel in RevitPythonShell](http://darenatwork.blogspot.ch/2016/03/more-control-over-ribbonpanel-in.html)
contains a description of how these work:

  * simple_ribbon.py - create a new `RibbonPanel` programatically and add a `PushButton`
  * simple_ribbon_with_icon.py - same as above, but assign an icon to the `PushButton` 
  * new_ribbon_panel.py - an elaborate demo of messing with the `RibbonPanel`

# RpsAddIns

The folder `RpsAddIns` contains some examples of using the "Deploy RpsAddIn" functionality

  * NewRibbonPanel - wrap up the startup script example `new_ribbon_panel.py` as a plugin

# License & Credit

This project is licensed under the terms of the MIT license. See the file "LICENSE" in the project root for more information.

Unless otherwise specified, the files in this repository were developed by Daren Thomas at the assistant chair for [Sustainable Architecture and Building Technologies (SuAT)](http://suat.arch.ethz.ch)
at the [Institute of Technology in Architecture](http://ita.arch.ethz.ch), ETH Zürich.
