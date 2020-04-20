import argparse
import os
import shutil
import tensorflow as tf
from mlagents.trainers import tensorflow_to_barracuda as tf2bc
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile

##########################################
# parse argments
##########################################
parser = argparse.ArgumentParser(prog='cptk2barracuda',usage='Tensorflow saved model to unity barracuda .nn file.')
parser.add_argument('-i', '--input', help='Prefix input dir path.(*.ckpt)')
parser.add_argument('-o', '--output', help='Unity barracuda file path.(*.nn)')
args = parser.parse_args()

##########################################
# to flozen graph
##########################################
workdir= "/tmp/output"

#config = tf.ConfigProto()
graph = tf.Graph()
with tf.compat.v1.Session(graph=graph) as sess:

    # Restore from checkpoint
    loader = tf.compat.v1.train.import_meta_graph(args.input + '.meta')
    loader.restore(sess, args.input)

    # Create working directory
    shutil.rmtree(workdir)
    os.mkdir(workdir)

    # Export checkpoint to SavedModel
    builder = tf.compat.v1.saved_model.builder.SavedModelBuilder(workdir)
    builder.add_meta_graph_and_variables(sess,
                                        [tf.saved_model.TRAINING, tf.saved_model.SERVING],
                                        strip_default_attrs=True)
    builder.save()

    # Convert frozen graph
    graph_def = graph.as_graph_def()
    output_graph_def = graph_util.convert_variables_to_constants(
                sess, graph_def, ['is_continuous_control', 'version_number', 'memory_size', 'action_output_shape', 'action_probs', 'action']
    )

    with gfile.GFile(workdir + "/frozen_graph_def.pb", "wb") as f:
        f.write(output_graph_def.SerializeToString())


##########################################
# to barracuda
##########################################
tf2bc.convert(workdir + '/frozen_graph_def.pb', args.output)


