Ableton Live Control Script for Akai MIDIMIX.

Adds colored focus box to the default MIDI MIX script.

Tested on live 9 & 10.

Based on Star Child's tutorial: https://www.youtube.com/watch?v=IgKwcCJsoz4


To install on Windows:

  1. Place 'MIDI_MIX' folder in "//../ProgramData/Ableton/Live X.X.X Suite/     Resources/MIDI Remote Scripts"

  2. Connect your MIDI MIX controller

  3. Run Ableton





To change the size of the track selection box (coloured box in Session view),
Open “YourControllerName.py”

Change the values in the brackets () of lines 94, 99, 100, 106 and 107 to suit your needs

On line 94 the first number is the amount horizontally and second is vertical.
Lines 99 and 106 are vertical,
100 and 112 are horizontal.
Make sure the value you input corresponds with the two values on line 94.


This is what the code will look like:
94        self._session = SpecialSessionComponent(X, Y)
99        self._scene_launch_buttons = [self._note_map[SCENELAUNCH[index]] for index in range(X) ]
100       self._track_stop_buttons = [self._note_map[TRACKSTOP[index]] for index in range(Y) ]
106       for scene_index in range(X):
112       for track_index in range(Y):

Lastly, don’t forget to add or remove rows/columns for SCENELAUNCH and CLIPNOTEMAP from MIDI_Map.py


Downloads:
BCRManager - 	    http://mountainutilities.eu/bcmanager

Based off FCB1020 scripts by http://remotescripts.blogspot.com

**st4rchild**
Special thanks to Youtuber "Lux" for figuring out the scene selection box.
And Aleksander Olav for working out Push 2 User Mode.

  ----------
  DISCLAIMER
  ----------

THESE FILES ARE PROVIDED AS-IS, WITHOUT ANY WARRANTY, EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO FITNESS FOR ANY PARTICULAR PURPOSE.
