# Custom Object Detection by using Darkflow

## Real-time object detection and classification
Paper: [version 1](https://arxiv.org/pdf/1506.02640.pdf), [version 2](https://arxiv.org/pdf/1612.08242.pdf).

There is various way to implement YOLO. I have tried to Pytorch implementation, Darknet Implementation
until so far. But we are building a system that interatcts with Flutter Application. So,
darkflow is a tensorflow translation of Darknet. I have used Anaconda and jupyer notebook.

## Getting Started

In Flutter application, we need to detect a pothole by training a custom object detection.
At the end of the trainning, there is some checkpoints files are created in the `/ckpt` directory.
Also, It is convertable file to `*.pb`. Also it is convertable to `*.lite` which can be used in mobile 
side of application.

### Requirements

Python3 or Python2, tensorflow 1.0, numpy, opencv 3.
After training part:
We need to do:

```
pip uninstall tensorflow
```

```
pip install "tensorflow==1.9.*"
```

Purpose of doing this is that there is some confilicting dependicies to new tensorflow version.
To obtain an easiest and efficient way is upgrading tensorflow version for using tf_convert API 
which is developed by Google.

### Set up Darkflow Repository
You can choose one of the following three ways to get started with darkflow. If you are using Python 3 on windows you will need to install Microsoft Visual C++ 14.0. Here you can find installation process, why it is required, references etc or you can try stackoverflow.

1. Just build the Cython extensions in place. NOTE: If installing this way you will have to use `./flow` in the cloned darkflow directory instead of `flow` as darkflow is not installed globally.
    ```
    python3 setup.py build_ext --inplace
    ```

2. Let pip install darkflow globally in dev mode (still globally accessible, but changes to the code immediately take effect)
    ```
    pip install -e .
    ```

3. Install with pip globally
    ```
    pip install .
    ```

### Installing some requirements

A step by step series of examples that tell you how to get a development env running.

Download the DARKFLOW repository. You can find it under this link. (https://github.com/thtrieu/darkflow)

For the purpose of training custom model. You need the start with initail weights which is obtained by under this link.(https://pjreddie.com/darknet/yolo/) or you can download by bash command.

```
wget https://pjreddie.com/media/files/yolov3.weights
```
You can download yolov3 weights in this way.

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With


## Contributing

The model has trained and converting the tflite module for RoadPulse application. For details on our code of conduct, and the process, you can conctact me via e-mail.

## Authors

* **Enes Karanfil** - *Student at TOBB University of Economics and Technology* - enkaranfiles@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Milestones

* Paper based research and training process
* YOLOV3 -tiny based-
* Realtime Streaming
* One-pass CNN structure
* RoadPulse
