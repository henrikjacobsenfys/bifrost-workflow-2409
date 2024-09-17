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

You are highly recommended to create a new virtual environment for this demonstration package.
It should be possible to use a [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
environment, but that may be overkill for these purposes.

Instead, use `python -m venv` or a faster near-drop-in `uv venv` part of [uv](https://docs.astral.sh/uv/),
both available via `pip` if not already installed on your system.

Clone this repository to someplace on your machine, e.g.,

```cmd
$ mkdir -p ~/Documents/ESS/demos/
$ cd ~/Documents/ESS/demos/
$ git clone https://github.com/g5t/bifrost-workflow-2409.git workflow
```

Create a virtual environment, inside the cloned repository directory; 
and activate it for the current terminal
```cmd
$ cd workflow
$ uv venv  # or `python -m venv .venv`
$ source .venv/bin/activate
```

Then install this package and its dependencies -- specifying `-e` makes an 'editable' install,
which enables you to modify Python files in the repository and use them (without re-installing!)
after re-loading the Python interpreter.

If you have `uv` available, it also implements a faster `pip` via `uv pip`.
```cmd
(workflow) $ uv pip install -e . 
```
Otherwise, standard `pip` will work fine as well, albeit more slowly.
```cmd
(.venv) $ python -m pip install -e .
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
(workflow) $ b2409-fetch
```
The command also accepts flags, e.g, `b2409-fetch --help` will show you that one
option is `--files` _and_ which files it will fetch by default.
You can download a subset of files by specifying only their names,
or get other files from the Nextcloud folder if you know their path and name.

--------
## Run the Jupyter Lab server to examine the notebooks
To start the server and launch a web-browser from the root of the notebooks folder run
```cmd
(workflow) $ cd notebooks
(workflow) $ jupyter-lab
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

