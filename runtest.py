import unittest
import sys

def collect_tests():
    suite = unittest.TestSuite()
    import test
    module_suite = unittest.TestLoader().loadTestsFromModule(test)
    suite.addTest(module_suite)
    return suite

if __name__ == '__main__':
  suite = collect_tests()
  runner = unittest.TextTestRunner(verbosity=1, failfast=False)
  results = runner.run(suite)
  if results.errors:
      sys.exit(2)
  elif results.failures:
      sys.exit(1)

  sys.exit(0)