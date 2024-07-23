#!/usr/bin/env python

import os
from note_seq import midi_io

def convert_midi_to_note_sequences(input_dir, output_file, recursive=False):
    note_sequences = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.mid'):
                try:
                    midi_path = os.path.join(root, file)
                    midi_data = open(midi_path, 'rb').read()
                    note_sequence = midi_io.midi_to_note_sequence(midi_data)
                    note_sequences.append(note_sequence)
                except Exception as e:
                    print(f"Error processing {file}: {e}")
        if not recursive:
            break

    with tf.io.TFRecordWriter(output_file) as writer:
        for note_sequence in note_sequences:
            writer.write(note_sequence.SerializeToString())

if __name__ == "__main__":
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()
    INPUT_DIRECTORY = "../../data/midi_files/Progressive House"
    SEQUENCES_TFRECORD = "/tmp/notesequences.tfrecord"
    convert_midi_to_note_sequences(INPUT_DIRECTORY, SEQUENCES_TFRECORD, recursive=True)
