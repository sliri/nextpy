# 5.3.2
################

import itertools


class MusicNotes:
    def __init__(self):
        self.base_notes_list = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.counter = -1
        self.octave = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.octave == 4 and self.counter % 7 == 0:
            raise StopIteration()
        elif self.counter % 7 == 0:
            self.octave += 1
            self.counter = self.counter % 7
            self.current_octave = [(2 ** self.octave) * note for note in self.base_notes_list]
        return self.current_octave[self.counter]


if __name__ == "__main__":
    Music = MusicNotes()
    for notes in Music:
        print(notes)
