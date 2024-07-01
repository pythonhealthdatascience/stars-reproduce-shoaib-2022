# Reproduction README

<!-- TODO: Remove this warning once filled out README -->
**Please note: This is a template README and has not yet been completed**

<!-- TODO: Fill out the README -->
## Model summary

> Shoaib M, Ramamohan V. **Simulation modeling and analysis of primary health center operations**. *SIMULATION* 98(3):183-208. (2022). <https://doi.org/10.1177/00375497211030931>.

This is a discrete-event simulation modelling primary health centres (PHCs) in India. There are four patient types: outpatients, inpatients, childbirth cases and antenatal care patients. Four model configurations are developed based on observed PHC practices or government-mandated operational guidelines. The paper explores different operational patterns for scenarios where very high utilisation was observed, to explore what might help reduce utilisation of these resources.

## Scope of the reproduction

In this assessment, we attempted to reproduce 17 items: 1 table, 9 figures, and 7 in-text results.

## Reproducing these results

### Repository overview

```bash
├── data
│   └──  ...
├── docker
│   └──  ...
├── output
│   └──  ...
├── sim
│   └──  ...
├── tests
│   └──  ...
├── environment.yaml
├── Makefile
└── README.md
```

* `docker/` - Instructions for creation of Docker container.
* `outputs/` - Output files from the model.
* `scripts/` - Code the model and for reproducing items from the scope.
* `tests/` - Test to check that model produces consistent results with our reproduction.
* `environment.yml` - Instructions for creation of python environment.
* `README.md` - This file!
* `run_all.py` - Contains instructions to run all the jupyter nobteooks in `scripts/` in sequence.

### Step 1. Set up environment

You'll first want create an environment with the specified version of Python and the required packages installed. There are a few options...

Option A: **Conda/Mamba environment**

> Create the environment using this command in your terminal: `conda env create -f environment.yaml`
> 
> You can use this environment in your preferred IDE, such as VSCode.
>
> You can also use this file to create the environment using mamba: `mamba env create -f environment.yml`

Option B: **Docker**

> You'll need `docker` installed on your local machine. You can then obtain the image by either:
>
> * Pulling a pre-built image from the GitHub container registry by running `docker pull ghcr.io/pythonhealthdatascience/shoaib2022:latest`, or
> * Building the image locally from the Dockerfile by running `docker build --tag shoaib2022 .`
>
> To run the image, you should then issue the following commands in your terminal:
>
> * `docker run -it -p 8080:80 --name shoaib2022_docker shoaib2022`
> * `conda activate shoaib2022`

### Step 2. Running the model

<!-- Add steps for running model and tests -->

## Reproduction specs and runtime

This reproduction was conducted on an Intel Core i7-12700H with 32GB RAM running Ubuntu 22.04.4 Linux.

Expected model runtime (given these specs) is <!-- Add times -->

## Citation

To cite the original study, please refer to the reference above. To cite this reproduction, please refer to the CITATION.cff file in the parent folder.

## License

This repository is licensed under the MIT License.