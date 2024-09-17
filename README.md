# bifrost2409 - BIFROST data transformation workflow

Using the under-development BIFROST data transformation workflow in September 2024.

Parts of this demonstration are likely to lose sync with the workflow as it is developed
further. Dependent packages, including the spectroscopy workflow for ESS,
are version-pinned to avoid breaking this demonstration &ndash; 
but important new developments may be missing here.

Compare the current release of 
[![PyPI badge](http://img.shields.io/pypi/v/essspectroscopy.svg)](https://pypi.python.org/pypi/essspectroscopy)
to the version pinned in `requirements.txt`, `v0.24.9.0`.

--------

## Installation

### Python
You should have a Python interpreter available to you via your system command line.
On an Apple macOS machine, this may be `python3` instead of the `python` command referenced below.

`scipp` is a dependency of the workflow, and currently requires a minimum Python version of 3.10.
If your system Python is 3.9 or lower, please upgrade before continuing.
You can check the version of Python available on your command line via, e.g.,

```cmd
$ python --version
```

Windows users without `python.exe` on their system path may benefit from installing Python via
the `winget` utility, which should be available already on up-to-date Windows 10 and 11 systems.
Search for an official Python package in `cmd.exe`, via 

```cmd
$ winget search Python.Python
```

There will be multiple versions available, pick one that you prefer (3.10 through 3.12 should all work)
to install, e.g.,
``` cmd
$ winget install Python.Python.3.11
```
which will also setup your user's path variable to _use_ the installed Python (though you may need to close and reopen `cmd.exe` for this to take effect).

### Git
The `git` command should also be available on your command line.

If you need to install `git` on macOS, you should install the Xcode Command Line tools via `xcode-select –-install` which ensures you have access to `git` and other tools.

On Windows, `winget` can once again help if you need `git`; run, e.g., `winget install Git.Git`.

### This repository
You are highly recommended to create a new virtual environment for this demonstration package, via e.g., `python -m venv venv`.

**Clone** this repository to someplace on your machine, e.g.,

```cmd
$ mkdir -p ~/Documents/ESS/demos/
$ cd ~/Documents/ESS/demos/
$ git clone https://github.com/g5t/bifrost-workflow-2409.git workflow
```

Create a virtual environment, inside the cloned repository directory; 
and activate it for the current terminal
```cmd
$ cd workflow
$ python -m venv venv
$ source venv/bin/activate
```

Then install this package and its dependencies -- specifying `-e` makes an 'editable' install,
which enables you to modify Python files in the repository and use them (without re-installing!)
after re-loading the Python interpreter.

```cmd
(venv) $ python -m pip install -e .
```

--------
## (Optional) Download simulation files from Nextcloud
The simulation output files used in the notebooks contained herein are hosted
on the DMSC Nextcloud server in a publicly readable 
[shared folder](https://project.esss.dk/owncloud/index.php/s/Diq9n3kITaEBtq7?path=%2FSimulations).

The notebooks will download and cache the files when first run, but you may prefer
to download the files now; and a command line utility exists to do just that.

Download all files by running 
```cmd
(venv) $ b2409-fetch
```
The command also accepts flags, e.g, `b2409-fetch --help` will show you that one
option is `--files` _and_ which files it will fetch by default.
You can download a subset of files by specifying only their names,
or get other files from the Nextcloud folder if you know their path and name.

--------
## Run the Jupyter Lab server to examine the notebooks
To start the server and launch a web-browser from the root of the notebooks folder run
```cmd
(venv) $ cd notebooks
(venv) $ jupyter-lab
```

--------

## Project Organization

```
├── LICENSE            <- Open-source license (BSD 3-Clause)
├── README.md          <- This README for users of this project.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── meta           <- Data about the raw data files, used to fetch files from Nextcloud
│   └── raw            <- The original, immutable simulation data.
│       └── main       <- Files fetched from Nextcloud by Pooch
│
├── notebooks          <- Jupyter notebooks. 
│                         Naming convention is a zero-padded number (for ordering),
│                         and a short `_` delimited description, e.g. `00_introduction`.
│
├── pyproject.toml     <- Project configuration file with package metadata and 
│                         required dependencies for bifrost2409
│
├── setup.cfg          <- Configuration file for flake8
│
└── bifrost2409        <- Source code for use in this project.
    │
    ├── __init__.py    <- Makes bifrost2409 a Python module
    │
    ├── config.py      <- Store useful variables and configuration
    │
    ├── dataset.py     <- Scripts to download or generate data
    │
    ├── nextcloud.py   <- Helper routines for creating Nextcloud metadata
    │
    └── plots.py       <- Code to create visualizations
```

--------

