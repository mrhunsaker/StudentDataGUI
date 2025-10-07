import sys
sys.path.insert(0, '.')
try:
    from StudentDataGUI.appTheming import theme
    print('Imported theme successfully')
except Exception as e:
    print('Import error:', type(e).__name__, e)
