# AI Electronic Music Generator
(work in progress) Using Magenta AI music libraries to make an electronic music generator app

Directions:
Ensure you have Magenta installed
If you use the Magenta repository instructions, it will automatically create a Magenta conda venv
In your terminal, run
```sh
eval "$(/Users/YOUR_USERNAME/miniconda3/bin/conda shell.YOUR_SHELL hook)"
```
to access conda base environment.

Then run 
```sh 
conda activate magenta
```

To train on your own midi files, access and alter the training scripts to replace the file locations with your own files.
First, you need to convert the MIDI to NoteSequences, then create sequence examples, then continue to training.

For more details, read the polyphony_rnn README (outdated): https://github.com/magenta/magenta/blob/main/magenta/models/polyphony_rnn/README.md
