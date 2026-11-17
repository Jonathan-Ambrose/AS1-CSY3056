import logging
from decimal import Decimal

# Logging to provide monitoring info for the CI/CD pipeline.
logging.basicConfig(level=logging.INFO)

# Function to calculate vechile valuation based on base price, mileage and vechile age.
def calculate_valuation(base_price: Decimal, mileage: int, year: int) -> Decimal:
    logging.info(f"Valuation started: {year} vehicle, {mileage} miles.")

    # Check if mileage is valid ie greater than or equal to 0.
    if mileage < 0:
        logging.error("Mileage below zero.")
        raise ValueError("Invalid mileage")

    
    # Boundary rule: If vechile is older than 2010, a 50% penalty is applied.    
    if year < 2010:
        logging.warning("Older Vechile detected. Applying penalty of 50%.")
        return round(base_price * Decimal("0.50"), 2)

    # If mileage is greater than 50,000 miles, a 10% penalty is applied.    
    if mileage > 50000:
        logging.warning("Higher mileage detected. Applying penalty of 10%.")
        return round(base_price * Decimal("0.90"), 2)
        
    return round(base_price, 2)