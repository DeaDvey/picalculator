import math
import time
from decimal import Decimal, getcontext

def pi_bbp():
    """Calculate pi using the Bailey–Borwein–Plouffe (BBP) formula."""
    pi = Decimal(0)
    k = 0
    while True:
        pi += (Decimal(1) / Decimal(16) ** k) * (
            Decimal(4) / (Decimal(8) * k + 1) - Decimal(2) / (Decimal(8) * k + 4) - Decimal(1) / (Decimal(8) * k + 5) - Decimal(1) / (Decimal(8) * k + 6)
        )
        yield pi
        k += 1

# Set the precision using Decimal module
getcontext().prec = 99999

# Create a generator for calculating pi
pi_generator = pi_bbp()

# Start with initial precision of 1
precision = 1

try:
    while True:
        # Get the next approximation of pi
        current_pi = next(pi_generator)

        # Format pi with the current precision
        formatted_pi = format(current_pi, f".{precision}f")

        # Print the formatted pi
        print(formatted_pi, end='\r', flush=True)

        # Increase precision for the next iteration
        precision += 1

        if precision % 100 == 0:
            getcontext().prec+=100
            
        # Optional: Adjust the delay
        time.sleep(0.001)

except KeyboardInterrupt:
    # Handle keyboard interrupt gracefully
    print("\nExiting...")
