import pytest
from decimal import Decimal
from src.component import calculate_valuation, valuate_fleet

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

# Integration test: Checks that valuate_fleet works with calculate_valuation for multiple cars.
def test_integration_fleet_valuation():
    fleet = [
        # Normal vechicle worth £10000
        {"base_price": Decimal("10000"), "mileage": 20000, "year": 2020},
        # High-mileage vechicle with 10% penalty worth £9000
        {"base_price": Decimal("10000"), "mileage": 60000, "year": 2015}, 
    ]
    # Total valuation £10000 + £9000 = £19000
    assert valuate_fleet(fleet) == Decimal("19000.00")

# Regression test: Checks that a pre-2010 high-mileage vehicle receives BOTH the 50% age penalty and 10% mileage penalty.
def test_regression_old_high_mileage_vehicle():
    actual = calculate_valuation(Decimal("10000"), 60000, 2008)
    # 10000 * 0.50 = 5000, then 5000 * 0.90 = 4500.00
    assert actual == Decimal("4500.00")