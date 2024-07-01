# This script will execute all the .ipynb files sequentially
# To run it, use the command bash run_reproduction.sh in your terminal

# Activate conda/mamba environment (assumes you have installed)
source activate shoaib2022

# Add to kernel list (required by nbconvert), and print list of kernels
# (to confirm it has been add)
python -m ipykernel install --user --name shoaib2022
jupyter kernelspec list

# Deactivate that (as nbconvert will use kernel_name rather than current env)
source deactivate

# Run notebooks
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_tab6.ipynb
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_fig2.ipynb
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_fig3_txt1.ipynb
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_fig4.ipynb
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_txt2.ipynb
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_txt34.ipynb
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_txt5.ipynb
jupyter nbconvert --to notebook --ExecutePreprocessor.kernel_name=shoaib2022 --execute --inplace scripts/reproduce_txt67.ipynb