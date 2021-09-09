# Comparison of Custom Numpy, PyTorch and TensorFlow models

The notebook `mnist_comparison.ipynb` contains the comparison of popular deep learning libraries **PyTorch** and **Tensorflow**, along with the custom deep learning model built using only the **NumPy** library.

## Installation
Python version - 3.9.5

Clone the repository, create a virtual environment and download the dependencies from **requirements.txt** file using the command
```
pip3 install -r requirements.txt
```

## Summary
In this notebook, we download the **MNIST** dataset and prepare it so, that we have the same data fed into all the models rather than using the dataset repositories of the **PyTorch** or **Tensorflow** libraries.

We are implementing a two-layer fully connected network.
| Hidden layer   | Number of neurons | Activation Function |
|----------------|-------------------|---------------------|
| 1              | 128               | ReLu                |
| 2              | 10                | Softmax             |

Other parameters:
 - Loss Function - Cross entropy loss
 - Optimizer - Gradient descent with a learning rate of 0.01
 - Number of epochs of training - 10

After training, we evaluate the model using **accuracy** on the testing set.

## Results
All the models were trained and tested using only the CPU.

| Model            | Accuracy (%) | Training Time (min) |
|------------------|--------------|---------------------|
| Custom model     | 97.08        | 48.32               |
| PyTorch model    | 97.14        | 50.79               |
| TensorFlow model | 97.59        | 93.09               |

Observing the above table, we can conclude that all three models performed almost similarly but, our custom model has the least training time when compared to the model in PyTorch and TensorFlow.

Well, our model is on par with the top deep learning frameworks (at least while performing all operations in CPU).

