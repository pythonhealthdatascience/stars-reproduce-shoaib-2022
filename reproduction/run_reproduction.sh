# This script will execute all the .ipynb files sequentially

# If you want to run the nbconvert commands directly in terminal in VSCode,
# make sure you have set interpreter: Ctrl + Shift + P + Jupyter: Select
# Interpreter to Start Jupyter Server

# Activate conda/mamba environment (assumes you have installed)
# eval "$(conda shell.bash hook)"
# conda activate shoaib2022

# source activate shoaib2022
# python -m ipykernel install --user --name shoaib2022
# source deactivate
# jupyter kernelspec list

# Run notebooks
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_tab6.ipynb