'''
Model testing

This module contains tests to confirm whether the simulation model is
producing consistent results. The tests are based on the raw .xls files output
by the model, rather than the processed results.
'''

import pytest
import pandas as pd
from pathlib import Path
from scripts import PHC
import tempfile
import xlrd

# Name of folder containing expected results
EXP_FOLDER = 'exp_results'
TEMP_FOLDER = tempfile.mkdtemp()

# Parameters for different runs of the model
PARAMETERS = [
    {
        'rep_file': 't6_c1.xls',
        'replication': 1
    },
    {
        'doc_cap': 1,
        'OPD_iat': 9,
        'delivery_iat': 2880,
        'ANC_iat': 2880,
        'replication': 1,
        'rep_file': 't6_c2.xls'
    }]

'''    {
        'doc_cap': 1,
        'OPD_iat': 9,
        'any_delivery': False,
        'any_ANC': False,
        'rep_file': 't6_c3.xls'
    },
    {
        'OPD_iat': 3,
        'mean': 5,
        'sd': 1,
        'consult_boundary_1': 2,
        'consult_boundary_2': 2,
        'rep_file': 't6_c4.xls'
    }
]'''


# Create fixture with path to temporary folder to contain results from tests
@pytest.fixture
def temp_folder():
    return TEMP_FOLDER


# Create fixture with path to folder with expected results
# (Fixtures can be used to provide information to tests)
@pytest.fixture
def exp_folder():
    return EXP_FOLDER


# Create function for importing .xls files
def import_xls(output_folder, filename):
    '''
    Import .xls file and get pandas dataframe

    Parameters:
    -----------
    output_folder : string
        Path to folder containing results file
    filename : string
        Name of results file inc. file type

    Returns:
    --------
    result : pandas DataFrame
        Dataframe with contents of first sheet in .xls file
    '''
    # Import workbook
    book = xlrd.open_workbook(Path(__file__).parent.joinpath(
        output_folder, filename))
    # Get first sheet as dataframe
    result = pd.read_excel(book, header=None, index_col=0)
    return result


# Run this function as separate tests on each of the files
@pytest.mark.parametrize('param', PARAMETERS,
                         ids=[d['rep_file'] for d in PARAMETERS])
def test_equal_df(param, temp_folder, exp_folder, request):
    '''
    Test that results are consistent with the expected results (which are
    from the computational reproducibility assessment)
    '''
    # Add the temporary folder as result path for model results
    param['results_path'] = temp_folder

    # Run model, with s appended to all items in dictionary
    PHC.main(**{f's_{k}': v for k, v in param.items()})

    # Import test and expected results
    test_result = import_xls(temp_folder, param['rep_file'])
    exp_result = import_xls(exp_folder, param['rep_file'])

    # Check that the dataframes are equal
    pd.testing.assert_frame_equal(test_result, exp_result)
