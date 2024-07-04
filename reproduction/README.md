# Primary Health Centre Model

## Model summary

> Shoaib M, Ramamohan V. **Simulation modeling and analysis of primary health center operations**. *SIMULATION* 98(3):183-208. (2022). <https://doi.org/10.1177/00375497211030931>.

This is a discrete-event simulation modelling primary health centres (PHCs) in India. There are four patient types: outpatients, inpatients, childbirth cases and antenatal care patients. Four model configurations are developed based on observed PHC practices or government-mandated operational guidelines. The paper explores different operational patterns for scenarios where very high utilisation was observed, to explore what might help reduce utilisation of these resources.

## Scope of the reproduction

In this assessment, we attempted to reproduce 17 items: 1 table, 9 figures, and 7 in-text results.

## Reproducing these results

### Repository overview

```bash
├── docker
│   └──  ...
├── outputs
│   └──  ...
├── scripts
│   └──  ...
├── tests
│   └──  ...
├── environment.yml
├── README.md
└── run_reproduction.sh
```

* `docker/` - Instructions for creation of Docker container.
* `outputs/` - Output files from the model.
* `scripts/` - Code the model and for reproducing items from the scope.
* `tests/` - Test to check that model produces consistent results with our reproduction.
* `environment.yml` - Instructions for creation of python environment.
* `README.md` - This file!
* `run_reproduction.sh` - Contains instructions to run all the jupyter nobteooks in `scripts/` in sequence.

### Step 1. Set up environment

You'll first want create an environment with the specified version of Python and the required packages installed. There are a few options...

#### Option A: Conda/Mamba environment

Create the environment using this command in your terminal: `conda env create -f environment.yaml`

You can use this environment in your preferred IDE, such as VSCode (where you will be asked to select the kernel/interpreter).

You can activate it in the terminal by running `conda activate shoaib2022`

You can also use this file to create the environment using mamba: `mamba env create -f environment.yml`

#### Option B: Docker

You'll need `docker` installed on your local machine. There are then two options for obtaining the image.

First (and perhaps simplest) is to build the image locally from the Dockerfile by running `docker build --tag shoaib2022 . -f ./reproduction/docker/Dockerfile`. You'll need to run from parent directory of `reproduction/`, and may require admin access (e.g. `sudo docker build`... on linux).

Alternatively, you can pull a pre-built image from the GitHub container registry by running `docker pull ghcr.io/pythonhealthdatascience/shoaib2022:latest`. This is stored in the package registry on GitHub, and they therefore require that you login with a personal access token to pull from there. Hence, steps to enable this are:

1. Create a Personal Access Token (Classic) for your GitHub account with `write:packages` and `delete:packages` access
2. On terminal, login using this token by running `sudo docker login ghcr.io -u githubusername` and then inputting the token when prompted for a password
3. Finally, run `sudo docker pull ghcr.io/pythonhealthdatascience/shoaib2022`

Once you have obtained the image using either of these methods, you can then set it up and open up jupyter lab by running one of the following commands in your terminal (depending on whether you built or pulled the image):

```
(sleep 2 && xdg-open http://localhost:8080) & sudo docker run -it -p 8080:80 --name shoaib2022_docker shoaib2022

(sleep 2 && xdg-open http://localhost:8080) & sudo docker run -it -p 8080:80 --name shoaib2022_docker ghcr.io/pythonhealthdatascience/shoaib2022:latest
```

This is the same as:

1. Running `docker run -it -p 8080:80 --name shoaib2022_docker shoaib2022`
2. Opening your web browser and going to <https://localhost:8080>.

Some other helpful commands:

* If you have closed your docker container and want to view the containers available, run `docker ps -a`
* To remake the container, you should delete it (`docker rm shoaib2022_docker`) then rebuild as above
* To re-open an exited container, run `docker restart shoaib2022_docker`. To close it again, run `docker stop shoaib2022_docker`

### Step 2. Running the model

You have three options for running the model...

#### Option A: Execute the notebooks

The simplest option is to just open and execute each of the provided jupyter notebooks. You can do so within your preferred IDE (e.g. VSCode, JupyterLab).

#### Option B: Bash

If you would like to execute all the notebooks sequentially with a single command, run the following command in terminal. For this to work, ensure that:

* You are within the `reproduction/` folder
* You are in base (i.e. no virtual environments activated - so may need to run `deactivate` or `conda deactivate`)

Then run the command:

```
bash run_reproduction.sh
```

If this is working, a line of text should appear as follows:

```
[NbConvertApp] Converting notebook scripts/reproduce_tab6.ipynb to notebook
```

A few minutes later, two new lines of text will appear:

```
[NbConvertApp] Writing 144091 bytes to scripts/reproduce_tab6.ipynb
[NbConvertApp] Converting notebook scripts/reproduce_fig2.ipynb to notebook
```

These indicate that it has finished running the first notebook, saved the file, and moved onto the next notebook. It will continue for approximately 22 minutes (will differ between machines), at which point all notebooks will have been run.

#### Option C: Pytest

With pytest, you can run each of the scenarios from the notebooks, and check whether the `.xls` files returned by your computer match up to those we had generated in this reproduction. You do not need to run Options A or B beforehand, as pytest will run iterations of the model itself. For this to work, ensure that:

* You are within the `reproduction/` folder
* You are in the `shoaib2022` conda/mamba environment (i.e. `conda activate shoaib2022`)

Then run the command:

```
pytest -n auto
```

The `-n auto` prompts your machine to use `pytest-xdist`, which will parallelise the tests using multiple CPUs, with `auto` meaning that it will use as many processes as your computer has physical CPU cores.

When you run this command, you should initially see an output similar to below (although with your root directory and platform):

```
============================= test session starts ==============================
platform linux -- Python 3.9.19, pytest-7.4.4, pluggy-1.0.0
rootdir: /home/amy/Documents/stars/stars-reproduce-shoaib-2022/reproduction
plugins: anyio-4.2.0, xdist-3.6.1
14 workers [41 items]  
```

It will remain like that for a few minutes, as the models are just running, but once models start completing, you should start to see outputs from the tests appear: green dots "<span style="color:green">....</span>" (indicating that the tests were successful) and red "<span style="color:red">F</span>" (if a test fails).

It should take about 36 minutes for the tests to run (though will differ between machines). Once finished, you should see a similar output to below (depending on the success of your tests):

```
================ 41 passed, 140 warnings in 2157.85s (0:35:57) =================
```

To find out more about what these tests are doing, check out the files in the `tests/` folder.

## Reproduction specs and runtime

This reproduction was conducted on an Intel Core i7-12700H with 32GB RAM running Ubuntu 22.04.4 Linux.

Expected model runtime is **22 minutes 26 seconds** (for notebooks/bash) and **35 minutes 57 seconds** (for pytest). This is given the specs above, and based on the combined runtime of the notebooks which use 10 replications (rather than 100) and parallel processing.

<!-- List of times:
* Table 6: 2m 38s
* Fig 2: 3m 27s
* Fig 3 Txt 1: 2m 45s
* Fig 4: 3m 0s
* Txt 2: 2m 29s
* Txt 3 4: 3m 7s
* Txt 5: 2m 11s
* Txt 6 7: 2m 49s -->

## Citation

To cite the original study, please refer to the reference above. To cite this reproduction, please refer to the CITATION.cff file in the parent folder.

## License

This repository is licensed under the MIT License.