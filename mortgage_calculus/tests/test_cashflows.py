"""Tests corresponding to the module mortgage_calculus."""

import pytest
import mortgage_calculus.cashflows as mort
import numpy as np


class TestAnnuity:
    """Tests for annuities."""

    def testFixedRateZeroBalanceAtEnd(self):
        """Test if balance at maturity is equal to 0."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        _, _, outstanding_balance = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "annuity"
        )
        np.testing.assert_almost_equal(outstanding_balance[months_to_legal_maturity], 0)

    def testFixedRateConstantInstallments(self):
        """Test for constant gross installments."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        interest, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "annuity"
        )
        installment = interest + redemption
        check_old = installment[1]
        for t in range(2, months_to_legal_maturity + 1):
            check_new = installment[t]
            np.testing.assert_almost_equal(check_old, check_new)
            check_old = check_new

    def testFixedRateSumRedemptions(self):
        """Test if sum redemptions equals balance at start."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        _, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "annuity"
        )
        np.testing.assert_almost_equal(sum(redemption), outstanding_balance)

    def testChangingRateZeroBalanceAtEnd(self):
        """Test if balance at maturity is equal to 0 when interest rate changes."""
        outstanding_balance = 100000
        months_to_legal_maturity = 360
        interest_rate = np.zeros(360)
        interest_rate[0:121] = 0.05
        interest_rate[121:] = 0.1
        _, _, outstanding_balance = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "annuity"
        )
        np.testing.assert_almost_equal(outstanding_balance[months_to_legal_maturity], 0)

    def testChangingRateConstantInstallments(self):
        """Test if installments are constant, on pieces, if interest rate changes."""
        outstanding_balance = 100000
        months_to_legal_maturity = 360
        interest_rate = np.zeros(360)
        interest_rate[0:121] = 0.05
        interest_rate[121:] = 0.1
        interest, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "annuity"
        )
        installment = interest + redemption
        check_old = installment[1]
        for t in range(2, 121):
            check_new = installment[t]
            np.testing.assert_almost_equal(check_old, check_new)
            check_old = check_new
        check_old = installment[122]
        for t in range(123, months_to_legal_maturity + 1):
            check_new = installment[t]
            np.testing.assert_almost_equal(check_old, check_new)
            check_old = check_new

    def testChangingRateSumRedemptions(self):
        """Test if sum redemptions equals balance."""
        outstanding_balance = 100000
        months_to_legal_maturity = 360
        interest_rate = np.zeros(360)
        interest_rate[0:121] = 0.05
        interest_rate[121:] = 0.1
        _, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "annuity"
        )
        np.testing.assert_almost_equal(sum(redemption), outstanding_balance)


class TestLinear:
    """Tests for linear mortgage."""

    def testFixedRateZeroBalanceAtEnd(self):
        """Test for zero balance at maturity."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        _, _, outstanding_balance = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "linear"
        )
        np.testing.assert_almost_equal(outstanding_balance[months_to_legal_maturity], 0)

    def testFixedRateConstantRedemption(self):
        """Test for constant redemption."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        _, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "linear"
        )
        check_old = redemption[1]
        for t in range(2, months_to_legal_maturity + 1):
            check_new = redemption[t]
            np.testing.assert_almost_equal(check_old, check_new)
            check_old = check_new

    def testFixedRateSumRedemptions(self):
        """Test if sum of redemptions equals balance."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        _, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "linear"
        )
        np.testing.assert_almost_equal(sum(redemption), outstanding_balance)

    def testChangingRateZeroBalanceAtEnd(self):
        """Tests if balance at maturity equals 0 in case of varying interest rate."""
        outstanding_balance = 100000
        months_to_legal_maturity = 360
        interest_rate = np.zeros(360)
        interest_rate[0:121] = 0.05
        interest_rate[121:] = 0.1
        _, _, outstanding_balance = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "linear"
        )
        np.testing.assert_almost_equal(outstanding_balance[months_to_legal_maturity], 0)

    def testChangingRateConstantRedemption(self):
        """Tests redemptions are constant in case of varying interest rate."""
        outstanding_balance = 100000
        months_to_legal_maturity = 360
        interest_rate = np.zeros(360)
        interest_rate[0:121] = 0.05
        interest_rate[121:] = 0.1
        _, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "linear"
        )
        check_old = redemption[1]
        for t in range(2, months_to_legal_maturity + 1):
            check_new = redemption[t]
            np.testing.assert_almost_equal(check_old, check_new)
            check_old = check_new

    def testChangingRateSumRedemptions(self):
        """Tests if sum redemptions equals balance in case of varying interest rate."""
        outstanding_balance = 100000
        months_to_legal_maturity = 360
        interest_rate = np.zeros(360)
        interest_rate[0:121] = 0.05
        interest_rate[121:] = 0.1
        _, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "linear"
        )
        np.testing.assert_almost_equal(sum(redemption), outstanding_balance)


class TestBullet:
    """Tests for bullet mortgage."""

    def testFixedRateZeroBalanceAtEnd(self):
        """Test for 0 balance at maturity."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        _, _, outstanding_balance = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "bullet"
        )
        np.testing.assert_almost_equal(outstanding_balance[months_to_legal_maturity], 0)

    def testFixedRateConstantBalance(self):
        """Test for constant balance prior to maturity."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        _, _, outstanding_balance = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "bullet"
        )
        check_old = outstanding_balance[1]
        for t in range(2, months_to_legal_maturity):
            check_new = outstanding_balance[t]
            np.testing.assert_almost_equal(check_old, check_new)
            check_old = check_new

    def testFixedRateSumRedemptions(self):
        """Test if redemptions equal balance."""
        outstanding_balance = 100000
        interest_rate = 0.05
        months_to_legal_maturity = 360
        _, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "bullet"
        )
        np.testing.assert_almost_equal(sum(redemption), outstanding_balance)

    def testChangingRateSumRedemptions(self):
        """Test of redemptions equal balance in case of varying interest rate."""
        outstanding_balance = 100000
        months_to_legal_maturity = 360
        interest_rate = np.zeros(360)
        interest_rate[0:121] = 0.05
        interest_rate[121:] = 0.1
        _, redemption, _ = mort.cashflows_happy_flow(
            outstanding_balance, months_to_legal_maturity, interest_rate, "bullet"
        )
        np.testing.assert_almost_equal(sum(redemption), outstanding_balance)
