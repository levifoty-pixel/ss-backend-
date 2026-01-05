from mido import MidiFile

# Standard guitar tuning (EADGBE), MIDI note numbers
GUITAR_STRINGS = {
    "E_low": 40,   # E2
    "A": 45,       # A2
    "D": 50,       # D3
    "G": 55,       # G3
    "B": 59,       # B3
    "E_high": 64   # E4
}

def find_string_and_fret(note):
    """
    Given a MIDI note number, find the best guitar string and fret.
    """
    best_string = None
    best_fret = None
    smallest_fret = 999

    for string_name, open_note in GUITAR_STRINGS.items():
        fret = note - open_note
        if 0 <= fret <= 20 and fret < smallest_fret:
            smallest_fret = fret
            best_string = string_name
            best_fret = fret

    return best_string, best_fret

def midi_to_tab(midi_path):
    """
    Convert a MIDI file into a simple guitar tab representation.
    """
    midi = MidiFile(midi_path)
    tab_output = []

    current_time = 0

    for track in midi.tracks:
        for msg in track:
            current_time += msg.time

            if msg.type == "note_on" and msg.velocity > 0:
                string_name, fret = find_string_and_fret(msg.note)

                if string_name is not None:
                    tab_output.append({
                        "time": current_time,
                        "string": string_name,
                        "fret": fret,
                        "note": msg.note
                    })

    return tab_output
