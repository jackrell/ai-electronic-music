#!/bin/bash

polyphony_rnn_generate \
--run_dir=/tmp/polyphony_rnn/logdir/run1 \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--output_dir=/tmp/polyphony_rnn/generated \
--num_outputs=10 \
--num_steps=128 \
--primer_pitches="[67,64,60]" \
--condition_on_primer=true \
--inject_primer_during_generation=false