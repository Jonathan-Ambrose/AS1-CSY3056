import pytest
from decimal import Decimal
from src.component import calculate_valuation

# Base price for testing £10000
# Test for normal valuation with valid mileage and year.
def test_normal_valuation():
    actual = calculate_valuation(Decimal("10000"), 60000, 2015)
    assert actual == Decimal("9000.00")

# Test for year boundary condition
def test_boundary_year_cutoff():
    actual = calculate_valuation(Decimal("10000"), 30000, 2009)
    # 50% penalty for vechiles older than 2010
    assert actual == Decimal("5000.00")

# Test for invalid mileage which should output a value error.
def test_invalid_mileage_raises_error():
    with pytest.raises(ValueError, match="Invalid mileage"):
        calculate_valuation(Decimal("10000"), -1, 2020)