def calculate_area(radius):
    """Calculates the area of a circle."""
    import math
    return math.pi * (radius ** 2)

def greet_user(name):
    """Simple greeting function."""
    print(f"Hello, {name}! Welcome to the Python training.")

# --- THE CRITICAL PART ---

if __name__ == "__main__":
    # This code ONLY runs if you execute this file directly:
    # e.g., python utility_demo.py
    print("--- Executing Script Directly ---")
    
    # Testing our functions
    my_radius = 5
    area = calculate_area(my_radius)
    
    greet_user("Trainee")
    print(f"The area of a circle with radius {my_radius} is {area:.2f}")
else:
    # This runs if the file is imported elsewhere
    print(f"--- '{__name__}' has been imported as a module ---")
