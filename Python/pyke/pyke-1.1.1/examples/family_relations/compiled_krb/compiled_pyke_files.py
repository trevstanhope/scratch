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
         ('', '', 'bc_example.krb'):
           [1379440266.01207, 'bc_example_bc.py'],
         ('', '', 'family.kfb'):
           [1379440266.022592, 'family.fbc'],
         ('', '', 'example.krb'):
           [1379440266.079699, 'example_fc.py', 'example_plans.py', 'example_bc.py'],
         ('', '', 'fc_example.krb'):
           [1379440266.122111, 'fc_example_fc.py'],
         ('', '', 'bc2_example.krb'):
           [1379440266.182187, 'bc2_example_bc.py'],
        },
        compiler_version)

