#!/usr/bin/env python

from magenta.models.polyphony_rnn import polyphony_model
from magenta.models.polyphony_rnn import polyphony_rnn_pipeline
from magenta.pipelines import pipeline
import tensorflow.compat.v1 as tf

def create_dataset(input_file, output_dir, eval_ratio=0.10):
    tf.logging.set_verbosity(tf.logging.INFO)

    pipeline_instance = polyphony_rnn_pipeline.get_pipeline(
        min_steps=80,  # 5 measures
        max_steps=512,
        eval_ratio=eval_ratio,
        config=polyphony_model.default_configs['polyphony']
    )

    def tf_record_iterator(file_name, example_type):
        dataset = tf.data.TFRecordDataset(file_name)
        for raw_record in dataset:
            yield example_type.FromString(raw_record.numpy())

    pipeline.run_pipeline_serial(
        pipeline_instance,
        tf_record_iterator(input_file, pipeline_instance.input_type),
        output_dir
    )

if __name__ == "__main__":
    input_file = "/tmp/notesequences.tfrecord"
    output_dir = "/tmp/polyphony_rnn/sequence_examples"
    create_dataset(input_file, output_dir)