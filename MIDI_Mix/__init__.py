# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live
from MIDI_Mix import MIDI_Mix

def create_instance(c_instance):
    ' Creates and returns the APC20 script '
    return MIDI_Mix(c_instance)


# local variables:
# tab-width: 4
