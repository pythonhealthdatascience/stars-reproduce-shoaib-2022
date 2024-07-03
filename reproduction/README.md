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

Option A: **Conda/Mamba environment**

> Create the environment using this command in your terminal: `conda env create -f environment.yaml`
> 
> You can use this environment in your preferred IDE, such as VSCode (where you will be asked to select the kernel/interpreter).
>
> You can activate it in the terminal by running `conda activate shoaib2022`
>
> You can also use this file to create the environment using mamba: `mamba env create -f environment.yml`

Option B: **Docker**

> You'll need `docker` installed on your local machine. You can then obtain the image by either:
>
> * Pulling a pre-built image from the GitHub container registry by running `docker pull ghcr.io/pythonhealthdatascience/shoaib2022:latest`, or
> * Building the image locally from the Dockerfile by running `docker build --tag shoaib2022 . -f ./reproduction/docker/Dockerfile`
>   * Run from parent directory of `reproduction/`
>   * May require admin access (e.g. `sudo docker build`... on linux)
>
> To run the image, you should then issue the following commands in your terminal:
>
> * `docker run -it -p 8080:80 --name shoaib2022_docker shoaib2022`
> * `conda activate shoaib2022`
> * `jupyter-lab`

Then open your browser and go to <https://localhost:8080>. This will open Jupyterlab within the `reproduction/` directory.

### Step 2. Running the model

To run the model, simply open and **execute the provided jupyter notebooks**.

If you would like to execute all the notebooks sequentially with a single command, run the following command in terminal (ensuring you are within the `reproduction/` folder):

```
bash run_reproduction.sh
```

If you would like to test that the results you are obtaining from running the model are consistent with those obtained in this reproduction, run the following command (from within the `reproduction/` folder, but ensure the conda environment is activated):

```
pytest -n auto
```

The `-n auto` prompts your machine to use `pytest-xdist`, which will parallelise the tests using multiple CPUs, with `auto` meaning that it will use as many processes as your computer has physical CPU cores.

## Reproduction specs and runtime

This reproduction was conducted on an Intel Core i7-12700H with 32GB RAM running Ubuntu 22.04.4 Linux.

Expected model runtime is **22 minutes 26 seconds**. This is given the specs above, and based on the combined runtime of the notebooks which use 10 replications (rather than 100) and parallel processing.

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