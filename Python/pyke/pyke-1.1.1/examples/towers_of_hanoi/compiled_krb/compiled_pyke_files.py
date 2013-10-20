# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'towers_of_hanoi.krb'):
           [1379439603.660229, 'towers_of_hanoi_bc.py'],
         ('', '', 'towers2.krb'):
           [1379439603.676836, 'towers2_bc.py'],
        },
        compiler_version)

