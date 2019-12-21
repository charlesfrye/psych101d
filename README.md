This is the GitHub repository for the course PSYCH101-D,
**Data Science for Research Psychology**,
taught at UC Berkeley in Fall 2019.

## Course Description

Experimental and data science abound with models.
Models of data can be used
to _simulate_, as in models of the climate,
to _explain simply_, as in paper airplanes,
and to _predict_, as in prototype models;
all of these are forms of inferential thinking.
In this course, we will learn to use Python
to describe, create, manipulate, and interrogate models of data.
With these new skills,
we will simulate, explain, and predict phenomena and data,
drawing examples from research psychology.
As one application of these tools,
we will develop classical statistical approaches,
like null hypothesis significance testing and linear regression.

## Course Materials

All of the materials are available in the `content` directory
of this repository, for local download,
or as interactive notebooks in the cloud via links at the
[website](https://charlesfrye.github.io/psych101d).

## How to Use the Materials

A table on the
[course website](https://charlesfrye.github.io/psych101d)
contains links that can be used to access and interact with the materials.
They will drop you into a cloud-computing environment in your browser,
where you can review lectures, complete homeworks and labs, and get scores on autograded sections.
Check the website for details.

## Locally Installing the Materials

If you would like to execute the code locally,
you will need to install Python and all of the relevant packages on your machine.

You'll first need to create a virtual environment
to install the packages into.
This will ensure you can use this material bug-free
without messing up any other Python code on your computer.
You might use
[Anaconda](https://docs.anaconda.com/anaconda/install/)
or, better,
[virtualenv](https://docs.python-guide.org/dev/virtualenvs/).
The material has only been tested with Python 3.6.8 on OS X and Linux,
and may have bugs outside of that setup,
so make sure you're working with an environment in Python 3.6.8.

[Clone the repository as normal](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository),
then navigate to the root directory of the project and install the dependencies using
```
pip install -r requirements.txt
```

Again, it is strongly recommended that you perform the above installation in a virtual environment,
e.g. as provided by Anaconda or virtualenv.

The materials are Jupyter notebooks,
so you will need to start up Jupyter with the following command
```
jupyter notebook
```
which will open up the Jupyter interface in a browser window.
