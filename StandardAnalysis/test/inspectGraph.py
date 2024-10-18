import tensorflow as tf

'''def summarize_graph(graph_def_file):
    with tf.io.gfile.GFile(graph_def_file, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
        print("Model inputs:")
        print([n.name for n in tf.compat.v1.get_default_graph().as_graph_def().node if n.op == 'Placeholder'])
        print("\nModel outputs:")
        print([n.name for n in tf.compat.v1.get_default_graph().as_graph_def().node if 'Softmax' in n.name or 'Sigmoid' in n.name])'''

# Replace 'graph.pb' with the path to your .pb file

def summarize_graph(graph_def_file):
    with tf.io.gfile.GFile(graph_def_file, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        
        # Extract input nodes and their shapes
        input_nodes = [(n.name, n.attr['shape'].shape) for n in graph_def.node if n.op == 'Placeholder']
        print("Model inputs:")
        for input_node, shape in input_nodes:
            input_shape = [dim.size for dim in shape.dim]
            print(f"Node: {input_node}, Shape: {input_shape}")

        print("\nModel outputs:")
        print([n.name for n in graph_def.node if 'Softmax' in n.name or 'Sigmoid' in n.name])

# Replace 'graph.pb' with the path to your .pb file
summarize_graph('graph_electron.pb')
