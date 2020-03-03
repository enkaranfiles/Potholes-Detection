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

### Working Environment

I have trained the model on:
1. NVDIA 2080 SLI GPU
2. 24 Core Processor, its able to run the program with 40 threads.

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

## Training Custom Object Detection Model

To obtain a state-of-art result in Pothole Detection, we need to collect massive dataset. I have collected the dataset from open-source platforms and connections from other companies. I have resized them, I have spent 2 hours to annotate them. Hence, to best of our knowledge, we need to see first preliminary results, so I have annotated the small amount of data and ou can see in the jupyter notebook file, we can find the pothole at given a image with .36 confidence score (labeled and trained on 50 images.).
#### Annotation
- To annotate images download [labelImg](https://tzutalin.github.io/labelImg/). 
- Check this [video](https://www.youtube.com/watch?v=p0nR2YsCY_U&feature=youtu.be) to learn how to use lebelImg.<br>
- Github repo for labelImg can be found [here](https://github.com/tzutalin/labelImg#installation)

## Training on your own dataset

*The steps below assume we want to use tiny YOLO and our dataset has 1 classes*

1. Create a copy of the configuration file `tiny-yolo-voc.cfg` and rename it according to your preference `tiny-yolo-voc-custom.cfg` (It is crucial that you leave the original `tiny-yolo-voc.cfg` file unchanged). Here `tiny-yolo-voc-custom.cfg` is for 1 classes, you can change the name as you wish.<br>

2. In `tiny-yolo-voc-custom.cfg`, change classes in the [region] layer (the last layer) to the number of classes you are going to train for. In our case, classes are set to 1.
    
    ```python
    ...

    [region]
    anchors = 1.08,1.19,  3.42,4.41,  6.63,11.38,  9.42,5.11,  16.62,10.52
    bias_match=1
    classes=1  ## 1 classes
    coords=4
    num=5
    softmax=1
    
    ...
    ```
3. In `tiny-yolo-voc-custom.cfg`, change filters in the [convolutional] layer (the second to last layer) to num * (classes + 5). In our case, num is 5 and classes are 1 so 5 * (1 + 5) = 30 therefore filters are set to 30.
    
    ```python
    ...

    [convolutional]
    size=1
    stride=1
    pad=1
    filters=30  ## 5 * (1 + 5) = 30
    activation=linear

    [region]
    anchors = 1.08,1.19,  3.42,4.41,  6.63,11.38,  9.42,5.11,  16.62,10.52
    
    ...
    ```
4. Change `labels.txt` to include the label(s) you want to train on (number of labels should be the same as the number of classes you set in `tiny-yolo-voc-custom.cfg` file). In my case, `labels.txt` will contain 1 labels.

    ```
    pothole
    ```
5. Reference the `tiny-yolo-voc-custom.cfg` model when you train.

`flow --model cfg/tiny-yolo-voc-custom.cfg --load weights/tiny-yolo-voc.weights --train --annotation train/annot --dataset train/images --gpu 1.0 --epochs 1000`
<br><br>Spesifying the model `--model cfg/tiny-yolo-voc-custom.cfg` and the weights `--load weights/tiny-yolo-voc.weights`. After that specify the path for the annatations `--annotation train/anoot` and images `--dataset train/images`. Use `--gpu 1.0` to use gpu for speed, if you do not  have GPU just don't use this part. You can specify the number of epochs. By default it is 1000. However it can be stopped anytime. I recommend to keep the lose below 1. Darkflow saving training step every 250 iteration under the `/ckpt` folder. From my experiments, I have seen the loss at least approximately 1.50, but loading more data it will be less than 1.
<br><br>

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
