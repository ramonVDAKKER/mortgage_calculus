"""Tests corresponding to the module mortgage_calculus."""

import pytest
import mortgage_calculus.interest_and_redemption as mort
import numpy as np


class TestDetermineInterest:
    """Tests for calculating monthly interest."""

    def test1(self):
        """Test computation of interest."""
        outstanding_balance = 1200
        interest_rate = 0.01
        assert mort.determine_interest(outstanding_balance, interest_rate) == 1

    def test2(self):
        """Test computation of interest."""
        outstanding_balance = 2400
        interest_rate = 0.01
        assert mort.determine_interest(outstanding_balance, interest_rate) == 2


class TestDetermineRedemptionLinear:
    """Tests for redemption of linear mortgage."""

    def test1(self):
        """Test calculation of redemption."""
        outstanding_balance = 1000.0
        months_to_legal_maturity = 50
        assert (
            mort.determine_redemption_linear(
                months_to_legal_maturity, outstanding_balance
            )
            == 20
        )

    def test2(self):
        """Test calculation of redemption."""
        outstanding_balance = 1000.0
        months_to_legal_maturity = 25
        assert (
            mort.determine_redemption_linear(
                months_to_legal_maturity, outstanding_balance
            )
            == 40
        )


class TestDetermineRedemptionBullet:
    """Tests for redemption bullet mortgage."""

    def test1(self):
        """Check constant balance."""
        outstanding_balance = 1000
        months_to_legal_maturity = 1
        assert (
            mort.determine_redemption_bullet(
                months_to_legal_maturity, outstanding_balance
            )
            == 1000
        )

    def test2(self):
        """Check 0 balance at maturity."""
        outstanding_balance = 1000.0
        months_to_legal_maturity = 25
        assert (
            mort.determine_redemption_bullet(
                months_to_legal_maturity, outstanding_balance
            )
            == 0
        )
