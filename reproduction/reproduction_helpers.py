'''
Helper functions for reproduction of items in the original paper
'''
import xlrd
import pandas as pd
import os


def process_results(files, xls=False, output_folder='outputs'):
    '''
    Imports files in provided list and produces a single dataframe with mean
    results from across the replications

    Parameters:
    ----------
    files : list
        List of file names (exc. file type) containing replication results
    output_folder : string
        Path to output folder

    Returns:
    --------
    summary : dataframe
        Dataframe with mean results for each model variant in file list
    xls : Boolean
        Whether file names include `.xls` suffix already when provided
    output_folder : string
        Path to output folder
    '''
    # Empty list to store results
    result_list = []

    for f in files:
        # Add .xls if not provided
        if not xls:
            filename = f'{f}.xls'
        else:
            filename = f

        # Import .xls and convert to pandas dataframe
        book = xlrd.open_workbook(os.path.join(output_folder, filename))
        result = pd.read_excel(book, header=None, index_col=0)

        # Add proportion of childbirth cases referred
        result.loc['prop_del_referred'] = (
            result.loc['del referred'] / result.loc['Del patients'])

        # Find mean from the replication
        # Save as dataframe, dropping the duplicate rows (NCD occ twice)
        res = pd.DataFrame({f: result.mean(axis=1)}).drop_duplicates()

        # Remove index name
        res.index.name = None

        if xls:
            # Remove .xls from column names
            res.columns = res.columns.str.removesuffix('.xls')

        # Save to list
        result_list.append(res)

    # Combine into single dataframe
    summary = pd.concat(result_list, axis=1)

    return summary
