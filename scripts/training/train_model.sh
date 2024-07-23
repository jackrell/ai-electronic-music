#!/bin/bash

# ensure this script is executable

# set paths to data and log directories
SEQUENCE_EXAMPLE_FILE=/tmp/polyphony_rnn/sequence_examples/training_poly_tracks.tfrecord
RUN_DIR=/tmp/polyphony_rnn/logdir/run1

# run the training script with desired parameters
polyphony_rnn_train \
  --run_dir=${RUN_DIR} \
  --sequence_example_file=${SEQUENCE_EXAMPLE_FILE} \
  --hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
  --num_training_steps=10000

# change hyparams depending on memory usage, using 64-unit batch size (default 128), 2-layer RNN with 64-unit (default of 3 layers of 256 units) to train faster
# add \ -- eval and change sequence example file to make it an eval job
# to view training and evaluationd data, run this script then run tensorboard --logdir=/tmp/polyphony_rnn/logdir
# Then go to http://localhost:6006 to view the TensorBoard dashboard
