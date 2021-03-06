from cx_Freeze import setup, Executable

# To compile for windows use---> python setup.py bdist_msi
# To compile for mac use---> python setup.py bdist_dmg

# Dependencies are automatically detected, but it might need
# fine tuning.

buildOptions = dict(
    packages=['scrollFrame', 'searchSetup', "tkinter", "threading", "sqlite3", "openpyxl", "re"],
    include_msvcr=True,
    include_files=['S:\\Documents\\Python\\Medical-Sorter\\DLLs\\tcl86t.dll',
                   'S:\\Documents\\Python\\Medical-Sorter\\DLLs\\tk86t.dll',
                   'S:\\Documents\\Python\\Medical-Sorter\\DLLs\\vcruntime140.dll',
                   'S:\\Documents\\Python\\Medical-Sorter\\DLLs\\sqlite3.dll',
                   'S:\\Documents\\Python\\Medical-Sorter\\DLLs\\python36.dll',
                   'S:\\Documents\\Python\\Medical-Sorter\\DB\\trash.txt',
                   'S:\\Documents\\Python\\Medical-Sorter\\DB\\medSort',
                   ],
    excludes=['numpy', 'scipy', 'matplotlib', 'pandas', 'jinja2', 'flask']
)

import sys

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('MedSort.py', base=base)
]

setup(name='MedSort',
      version='2.0',
      description='Medical Indent management',
      options=dict(build_exe=buildOptions),
      executables=executables)
