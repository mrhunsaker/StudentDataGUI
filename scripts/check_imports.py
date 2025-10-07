import sys, pkgutil, traceback
sys.path.insert(0, '.')
modules = []
import StudentDataGUI.appPages as pages_pkg
pkgpath = pages_pkg.__path__
for finder, name, ispkg in pkgutil.iter_modules(pkgpath):
    modules.append(name)
print('Modules to test:', modules)
for m in modules:
    print('\n--- importing', m, '---')
    try:
        __import__(f'StudentDataGUI.appPages.{m}', fromlist=['*'])
        print('OK')
    except Exception as e:
        print('EXCEPTION during import of', m)
        traceback.print_exc()
