# Comparison of Custom Numpy, PyTorch and TensorFlow models

The notebook `mnist_comparison.ipynb` contains comparison of popular deep learning libraries **PyTorch** and **Tensorflow**, along withe the custom deep learning model built using only **NumPy** library.

In this notebook we download the **MNIST** dataset and prepare it, so that we have the same data fed into all the models rather than using the dataset repositories of the **PyTorch** or **Tensorflow** libraries.

We are implementing a two layer fully connected network.
| Hidden layer   | Number of neurons | Activation Function |
|----------------|-------------------|---------------------|
| 1              | 128               | ReLu                |
| 2              | 10                | Softmax             |

Other parameters:
 - Loss Funtion - Cross entropy loss
 - Optimizer - Gradient descent with learning rate 0.01
 - Number of epochs of training - 20

After training we evaluate the model using **accuracy** on the testing set.

## Results
All the models were trained and tested using only CPU.

| Model            | Accuracy (%) | Training Time (s) |
|------------------|--------------|-------------------|
| Custom model     |              |                   |
| PyTorch model    |              |                   |
| TensorFlow model |              |                   |
