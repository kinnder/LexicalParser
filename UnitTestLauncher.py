import unittest

loader = unittest.TestLoader()

suite = loader.discover(start_dir=".", pattern='*Tests.py')

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
