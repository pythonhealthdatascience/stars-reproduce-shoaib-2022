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
import xlrd
import tempfile

# Name of folder containing expected results
EXP_FOLDER = 'exp_results'
TEMP_FOLDER = tempfile.mkdtemp()

# Parameters for different runs of the model
# Table 6 ---------------------------------------------------------------------
TAB6 = [
    {
        'doc_cap': 2,
        'OPD_iat': 4,
        'IPD_iat': 2880,
        'delivery_iat': 1440,
        'ANC_iat': 1440,
        'rep_file': 't6_c1.xls'
    },
    {
        'doc_cap': 1,
        'OPD_iat': 9,
        'IPD_iat': 2880,
        'delivery_iat': 2880,
        'ANC_iat': 2880,
        'rep_file': 't6_c2.xls'
    },
    {
        'doc_cap': 1,
        'OPD_iat': 9,
        'IPD_iat': 2880,
        'any_delivery': False,
        'any_ANC': False,
        'rep_file': 't6_c3.xls'
    },
    {
        'doc_cap': 2,
        'OPD_iat': 3,
        'mean': 5,
        'sd': 1,
        'consult_boundary_1': 2,
        'consult_boundary_2': 2,
        'IPD_iat': 2880,
        'delivery_iat': 1440,
        'ANC_iat': 1440,
        'rep_file': 't6_c4.xls'
    }
]

# Figure 2 --------------------------------------------------------------------
arr_dict = [
    {
        'OPD_iat': 3,
        'rep_file': 'arr170'
    },
    {
        'OPD_iat': 6,
        'rep_file': 'arr85',
    },
    {
        'OPD_iat': 8,
        'rep_file': 'arr65',
    }
]
serv_dict = [
    {
        'mean': 0.87,
        'sd': 0.21,
        'consult_boundary_1': 0.5,  # From PHC.py
        'consult_boundary_2': 0.3,  # From PHC.py
        'rep_file': 'serv087'
    },
    {
        'mean': 2.5,
        'sd': 0.5,
        'consult_boundary_1': 1,  # Guess
        'consult_boundary_2': 1,  # Guess
        'rep_file': 'serv25'
    },
    {
        'mean': 5,
        'sd': 1,
        'consult_boundary_1': 2,  # From config 4
        'consult_boundary_2': 2,  # From config 4
        'rep_file': 'serv5'
    }
]
FIG2 = []
for arr in arr_dict:
    for serv in serv_dict:
        # Combine the dictionaries
        comb = {**arr, **serv}
        # Replace the file name
        comb['rep_file'] = f'''f2_{arr['rep_file']}_{serv['rep_file']}.xls'''
        # Save to list
        FIG2.append(comb)

# Figure 3 and In-text 1 ------------------------------------------------------
arr_dict = [
    {
        'IPD_iat': 1440,
        'delivery_iat': 1440,
        'ANC_iat': 1440,
        'rep_file': 'arr111'
    },
    {
        'IPD_iat': 720,
        'delivery_iat': 1440,
        'ANC_iat': 1440,
        'rep_file': 'arr211',
    },
    {
        'IPD_iat': 720,
        'delivery_iat': 720,
        'ANC_iat': 720,
        'rep_file': 'arr222',
    }
]
serv_dict = [
    {
        'mean': 0.87,
        'sd': 0.21,
        'consult_boundary_1': 0.5,  # From PHC.py
        'consult_boundary_2': 0.3,  # From PHC.py
        'rep_file': 'serv087'
    },
    {
        'mean': 2.5,
        'sd': 0.5,
        'consult_boundary_1': 1,  # From Figure 2 (which was a guess)
        'consult_boundary_2': 1,  # From Figure 2 (which was a guess)
        'rep_file': 'serv25'
    }
]
FIG3TXT1 = []
for arr in arr_dict:
    for serv in serv_dict:
        # Combine the dictionaries
        comb = {**arr, **serv}
        # Replace the file name
        comb['rep_file'] = f'''f3_{arr['rep_file']}_{serv['rep_file']}.xls'''
        # Save to list
        FIG3TXT1.append(comb)

# Figure 4 --------------------------------------------------------------------
arr_dict = [
    {
        'delivery_iat': 1440,
        'rep_file': 'arr1440'
    },
    {
        'delivery_iat': 1080,
        'rep_file': 'arr1080'
    },
    {
        'delivery_iat': 960,
        'rep_file': 'arr960'
    },
    {
        'delivery_iat': 720,
        'rep_file': 'arr720'
    }
]
bed_dict = [
    {
        'delivery_bed_n': 1,
        'rep_file': 'bed1'
    },
    {
        'delivery_bed_n': 2,
        'rep_file': 'bed2'
    }
]
FIG4 = []
for arr in arr_dict:
    for bed in bed_dict:
        # Combine the dictionaries
        comb = {**arr, **bed}
        # Replace the file name
        comb['rep_file'] = f'''f4_{arr['rep_file']}_{bed['rep_file']}.xls'''
        # Save to list
        FIG4.append(comb)

# In-text 2 -------------------------------------------------------------------
base_model = {
    'OPD_iat': 3,
    'rep_file': 'arr170',
    'mean': 5,
    'sd': 1,
    'consult_boundary_1': 2,
    'consult_boundary_2': 2
}
variants = [
    {
        'admin_doc_to_staff': False,
        'rep_file': 'in2_admin_doctor.xls'
    },
    {
        'admin_doc_to_staff': True,
        'rep_file': 'in2_admin_nurse.xls'
    },
]
TXT2 = []
for var in variants:
    TXT2.append({**base_model, **var})

# In-text 3 and 4 -------------------------------------------------------------
base_model = {
    'OPD_iat': 3,
    'rep_file': 'arr170',
    'mean': 5,
    'sd': 1,
    'consult_boundary_1': 2,
    'consult_boundary_2': 2
}
variants = [
    # Base case for in-text result 3 and 4
    {
        'rep_file': 'in34_normal.xls'
    },
    # Scenarios for in-text result 3
    {
        'admin_doc_to_staff': True,
        'rep_file': 'in3_admin.xls'
    },
    {
        'doctor_delivery_scenario': True,
        'rep_file': 'in3_delivery.xls'
    },
    {
        'doctor_delivery_scenario': True,
        'admin_doc_to_staff': True,
        'rep_file': 'in3_admin_delivery.xls'
    },
    # Scenarios for in-text result 4
    {
        'doc_cap': 3,
        'rep_file': 'in4_doctor.xls'
    },
    {
        'doc_cap': 3,
        'doctor_delivery_scenario': True,
        'admin_doc_to_staff': True,
        'rep_file': 'in4_admin_delivery_doctor.xls'
    },
]
# Combine dictionaries
TXT34 = []
for var in variants:
    TXT34.append({**base_model, **var})

# In-text 5 -------------------------------------------------------------------
TXT5 = [
    {
        'inpatient_bed_n': 6,
        'IPD_iat': 720,
        'delivery_iat': 720,
        'ANC_iat': 720,
        'rep_file': 'in5_6bed.xls'
    },
    {
        'inpatient_bed_n': 4,
        'IPD_iat': 720,
        'delivery_iat': 720,
        'ANC_iat': 720,
        'rep_file': 'in5_4bed.xls'
    },
]

# In-text 6 and 7 -------------------------------------------------------------
TXT67 = [
    {
        'OPD_iat': 3,
        'rep_file': 'in67_base.xls',
    },
    {
        'OPD_iat': 3,
        'admin_ncd_to_staff': True,
        'rep_file': 'in6_base_admin.xls',
    },
    {
        'OPD_iat': 3,
        'opd_ncd_to_staff': 0.1,
        'rep_file': 'in7_base_appointment.xls',
    },
    {
        'OPD_iat': 3,
        'admin_ncd_to_staff': True,
        'opd_ncd_to_staff': 0.1,
        'rep_file': 'in7_base_admin_appointment.xls',
    }
]

# Combine all the parameters into a single list
parameters = TAB6 + FIG2  #+ FIG3TXT1 + FIG4 + TXT2 + TXT34 + TXT5 + TXT67


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
# Use 'rep_file' from each dictionary as the ID for that run
@pytest.mark.parametrize('param', parameters,
                         ids=[d['rep_file'] for d in parameters])
def test_equal_df(param, temp_folder, exp_folder):
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
