## Introduction to PySpark

## Goals of the Laboratory

In this introductory laboratory, we expect students to:
- Acquire basic knowledge about Python and Matplotlib
- Gain familiarity with Juypter Notebooks
- Gain familiarity with the PySpark API and SparkSQL

To achieve such goals, we will go through the following steps:
In section 1, IPython and Jupyter Notebooks are introduced to help students understand the environment used to work on Data Science projects.
In section 2, we briefly overview Python and its syntax. In addition, we cover Matplotlib, a very powerful library to plot figures in Python, which you can use for your Data Science projects. Finally, we introduce Pandas, a python library that is very helpful when working on Data Science projects.
In section 3 we cover the PySpark and SparkSQL APIs
In section 4, we conclude the introductory laboratory with a simple use case.


### Python, IPython and Jupyter Notebooks¶
Python is a high-level, dynamic, object-oriented programming language. It is a general purpose language, which is designed to be easy to use and easy to read.
IPython (Interactive Python) is orignally developed for Python. Now, it is a command shell for interactive computing supporting multiple programming languages. It offers rich media, shell syntax, tab completion, and history. IPython is based on an architecture that provides parallel and distributed computing. IPython enables parallel applications to be developed, executed, debugged and monitored interactively.
Jupyter Notebooks are a web-based interactive computational environment for creating IPython notebooks. An IPython notebook is a JSON document containing an ordered list of input/output cells which can contain code, text, mathematics, plots and rich media. Notebooks make data analysis easier to perform, understand and reproduce. All laboratories in this course are prepared as Notebooks. As you can see, in this Notebook, we can put text, images, hyperlinks, source code... The Notebooks can be converted to a number of open standard output formats (HTML, HTML presentation slides, LaTeX, PDF, ReStructuredText, Markdown, Python) through File -> Download As in the web interface. In addition, Jupyter manages the notebooks' versions through a checkpoint mechanism. You can create checkpoint anytime via File -> Save and Checkpoint.
NOTE on Checkpointing: in this course, we use a peculiar environment to work. We don't have a Notebook server: instead, we creat on demand clusters with a Notebook front-end. Since your clusters are emphemeral (they are terminated after a pre-defined amount of time), checkpointing is of little use, for anything else than saving your notebook in your emphemeral environment. It is far better to download regularly your notebooks, and to push them to your git repository.
