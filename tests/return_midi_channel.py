from mido import MidiFile

mid = MidiFile('S:\\Midi-Library\\raw_midi\\freemidi\\1576.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    # for msg in track:
    #     print(msg)