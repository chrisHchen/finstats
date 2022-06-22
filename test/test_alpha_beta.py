import finstats.alpha_beta as finstats
import pandas as pd
import numpy as np
from numpy.testing import assert_almost_equal
import unittest


mixed_returns = pd.DataFrame(
        {'return': np.array([1., -1., 6., -5., 1., -3., 3., 2., -9., 7]) / 100},
        index=pd.date_range('2022-1-30', periods=10, freq='D'))

positive_returns = pd.DataFrame(
        {'return': np.array([3, 1., 5., 10, 1., 7., 4., 5., 2., 6]) / 100},
        index=pd.date_range('2022-1-30', periods=10, freq='D'))

negtive_returns = pd.DataFrame(
        {'return': np.array([-1, -2, -3., -5., -2., -3, -12., -1., -2., -10]) / 100},
        index=pd.date_range('2022-1-30', periods=10, freq='D'))

mixed_returns_with_nan = pd.DataFrame(
        {'return': np.array([np.nan, 1., 5., -4., 1., -2., 3., 1., -10., 8]) / 100},
        index=pd.date_range('2022-1-30', periods=10, freq='D'))

positive_returns_with_nan = pd.DataFrame(
        {'return': np.array([1, 2., np.nan, 4., 2., 1., 10., 12., 1., 6]) / 100},
        index=pd.date_range('2022-1-30', periods=10, freq='D'))

negtive_returns_with_nan = pd.DataFrame(
        {'return': np.array([-1., -3., -5., -6., -2., np.nan, -12., -2., -2., -6]) / 100},
        index=pd.date_range('2022-1-30', periods=10, freq='D'))

align_test_list = [
        [mixed_returns, positive_returns, 10],
        [mixed_returns, mixed_returns_with_nan, 9],
        [positive_returns_with_nan, mixed_returns_with_nan, 8]
]

alpha_beta_test_list = [
        [mixed_returns, positive_returns, 0.8696323422235717, -0.011049723756906134],
        [mixed_returns, negtive_returns, -0.9912033751963829, -0.5026335590669677],
        [negtive_returns, positive_returns, -0.9971673541849576, -0.40883977900552504],
        [mixed_returns, mixed_returns, 0.0, 1.0]
]

class AlphaBetaCase(unittest.TestCase):
    def test_align(self):
        for returns, benchmark, length in align_test_list:
                returns, benchmark = finstats.align(returns, benchmark)
                self.assertEqual(len(returns), length)
                self.assertEqual(len(benchmark), length)

    def test_alpha_beta(self):
        for returns, benchmark, designed_alpha, designed_beta in alpha_beta_test_list:
                returns, benchmark = finstats.align(returns, benchmark)
                alpha, beta = finstats.cal_alpha_beta(returns, benchmark)
                assert_almost_equal(alpha, designed_alpha, 8)
                assert_almost_equal(beta, designed_beta, 8)

if __name__ == '__main__':
        pass
  # stats.cal_alpha_beta('sh600519', 'sh000300', datalen=1000)
  # stats.cal_alpha_beta('sz300750', 'sh000300', datalen=1000)
  # stats.cal_alpha_beta('sh510300', 'sh000300', datalen=1000)
  # stats.cal_alpha_beta('sh510050', 'sh000300', datalen=1000)
#   stats.finstats()
#   unittest.main()