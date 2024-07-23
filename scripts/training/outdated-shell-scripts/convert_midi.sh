INPUT_DIRECTORY = "../../data/midi_files/Progressive House"
SEQUENCES_TFRECORD = /tmp/notesequences.tfrecord

convert_dir_to_note_sequences \
  --input_dir=INPUT_DIRECTORY \
  --output_file=SEQUENCES_TRFRECORD \
  --recursive