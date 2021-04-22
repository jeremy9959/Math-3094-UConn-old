# Installing Anaconda/Python/Jupyter

### Install the software

To install anaconda with the associated tools, start with the 
[installation instructions](https://docs.anaconda.com/anaconda/install) in the anaconda
documentation.  Follow the steps outlined for your operating system.  Unless you know what
you are doing, just accept all the defaults.

- [Windows](https://docs.anaconda.com/anaconda/install/windows/)
- [Mac OS](https://docs.anaconda.com/anaconda/install/mac-os/) -- follow the "graphical install" prompts.
- [Linux](https://docs.anaconda.com/anaconda/install/linux/) -- this requires executing an installation
shell script that you download from the anaconda site.

As well as installing the software, this process will set up anaconda navigator, 
which is a graphical tool for managing the software.

For a video walkthrough, see:

- [Windows 10](https://www.youtube.com/watch?v=HlmhkvV51f0&t=179s)
- [Mac OS](https://www.youtube.com/watch?v=i4GxctDcx6s)

### Verify your installation

To make sure things are set up correctly, refer to the 
[Getting Started with Anaconda](https://docs.anaconda.com/anaconda/user-guide/getting-started/)
web page:

- Follow the first set of instructions to open Anaconda-Navigator 
- Then skip down and follow the steps labelled "Run Python in a Jupyter Notebook"

### Installing Packages
#### Method 1
All packages can be installed at once by downloading the "environment.yml" and following the
[guide here.](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)

#### Method 2
If this does not work packages can be installed following
[this guide](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/)
or with this command:
````python
conda install numpy tensorflow keras matplotlib bokeh seaborn holoviews
````



