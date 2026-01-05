from basic_pitch import ICASSP2022Model
from basic_pitch.utils import save_output
import os
import uuid

def transcribe_audio(audio_path):
    # Load the model
    model = ICASSP2022Model()

    # Run transcription
    output_dict = model.transcribe([audio_path])

    # Create a unique filename for the MIDI output
    output_id = str(uuid.uuid4())
    midi_path = f"outputs/{output_id}.mid"

    # Make sure the outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    # Save the MIDI file
    save_output(output_dict, output_path=midi_path, save_midi=True, save_model_outputs=False)

    return midi_path
