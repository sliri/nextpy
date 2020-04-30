# 5.1.2
################

import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

yonatan_hakatan_notes = notes.split('_')

for note in yonatan_hakatan_notes:
    frequency = int(freqs[note.split(',')[0]])
    duration = int(note.split(',')[1])
    winsouosnd.Beep(frequency, duration)
