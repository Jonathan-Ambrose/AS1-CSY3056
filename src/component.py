import logging
from decimal import Decimal

# Logging to provide monitoring info for the CI/CD pipeline.
logging.basicConfig(level=logging.INFO)

# Function to calculate vehicle valuation based on base price, mileage and vehicle age.
def calculate_valuation(base_price: Decimal, mileage: int, year: int) -> Decimal:
    logging.info(f"Valuation started: {year} vehicle, {mileage} miles.")

    # Check if mileage is valid ie greater than or equal to 0.
    if mileage < 0:
        logging.error("Mileage below zero.")
        raise ValueError("Invalid mileage")

    
    # Boundary rule: If vehicle is older than 2010, a 50% penalty is applied.    
    if year < 2010:
        logging.warning("Older vehicle detected. Applying penalty of 50%.")
        return round(base_price * Decimal("0.50"), 2)

    # If mileage is greater than 50,000 miles, a 10% penalty is applied.    
    if mileage > 50000:
        logging.warning("Higher mileage detected. Applying penalty of 10%.")
        return round(base_price * Decimal("0.90"), 2)
        
    return round(base_price, 2)

# Function to calculate the total cost of a fleet
def valuate_fleet(vehicles):
    total_fleet = Decimal("0.00")
    for vehicle in vehicles:
        total_fleet += calculate_valuation(
            vehicle["base_price"],
            vehicle["mileage"],
            vehicle["year"]
        )
    return round(total_fleet, 2)