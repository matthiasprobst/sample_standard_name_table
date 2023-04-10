import pathlib
import shutil

import yaml

try:
    from h5rdmtoolbox.conventions import StandardNameTable
except ImportError:
    raise ImportError('h5rdmtoolbox missing. you need to install it to check for standard name tables')
__this_dir__ = pathlib.Path(__file__).parent


def check(filename):
    """Reads the standard name table from the gitlab repository. Checks if the version name is correct."""
    with open(filename, 'r') as f:
        _dict = {}
        for d in yaml.full_load_all(f):
            _dict.update(d)

    snt = StandardNameTable.from_yaml(
        filename
    )
    assert snt.versionname == 'sample_standard_name_table-v1'
    check_result = True
    for k, v in snt.table.items():
        if not snt.check_name(k, strict=True):
            check_result = False
        if not snt.check_units(k, v['canonical_units']):
            check_result = False
    snt.sdump()
    return snt, check_result


def sort(filename):
    """Sorts the standard name table"""
    bak_filename = f'{filename}.bak'
    shutil.copy(filename, bak_filename)
    snt_local = StandardNameTable.from_yaml(bak_filename)
    snt_local.to_yaml(filename)  # automatically sorts


def generate_readme(check: bool):
    """Generates the README.md file"""
    if check:
        check_badge = 'https://img.shields.io/badge/check-passed-green.svg'
    else:
        check_badge = 'https://img.shields.io/badge/check-failed-red.svg'
    _READNME_TXT = rf"""Sample Standard Name Table
==========================


|version v1| |project h5rdmtoolbox| |example|

.. |version v1| image:: https://img.shields.io/badge/version-v1-green.svg
.. |project h5rdmtoolbox| image:: https://img.shields.io/badge/project-h5RDMtoolbox-orange.svg
.. |example| image:: https://img.shields.io/badge/status-example-yellow.svg
.. |example| image:: {check_badge}

A sample standard name table as used in the h5RDMtoolbox. This is an **example** standard
name table and used for testing and demonstration purposes in the `h5RDMtoolbox` package.

A `manage.py` python file is provided to perform a check and to 
sort the table (stored as a yaml file). It is recommended to run the 
file `manage.py` before publishing the table. The below table 
shows the table. The table is also produced in the python file:

Table
-----
"""
    return _READNME_TXT


def update_readme(snt_filename, target_filename='README.rst'):
    """Adds the table to the readme file"""
    snt, check_result = check(snt_filename)
    with open(target_filename, 'w') as f:
        f.writelines(generate_readme(check_result))
        f.write('.. list-table:: Table of standard names')
        f.write('\n\t:widths: 10, 10, 10')
        f.write('\n\t:header-rows: 1\n')
        f.write('\n\t* - Standard Name')
        f.write('\n\t  - Canonical Units')
        f.write('\n\t  - Description')
        for k, v in snt.table.items():
            f.write(f'\n\t* - {k}')
            f.write(f'\n\t  - {v["canonical_units"]}')
            f.write(f'\n\t  - {v["description"]}')


if __name__ == '__main__':
    snt_yaml_filename = 'sample_standard_name_table.yaml'
    check(snt_yaml_filename)
    sort(snt_yaml_filename)
    update_readme(snt_yaml_filename)
