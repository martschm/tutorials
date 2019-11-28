from mlxtend.data import loadlocal_mnist

def import_data():
    X_full, y_full = loadlocal_mnist(
                                 images_path='../data/t10k-images-idx3-ubyte',
                                 labels_path='../data/t10k-labels-idx1-ubyte')
    return X_full, y_full
