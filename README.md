# Custom Object Detection by using Darkflow

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
To obtain an easiest and efficient way is upgrading tensorflow version for using tf_conver API 
which is developed by Google.

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

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

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
