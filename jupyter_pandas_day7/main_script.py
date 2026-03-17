# We are importing the functions from our previous file
import utility_demo

print("\n[Main App] Starting the program...")

# We can use the functions without running the 'if __name__ == "__main__"' block
user_name = "Alex"
utility_demo.greet_user(user_name)

circle_area = utility_demo.calculate_area(10)
print(f"[Main App] Calculated area in main_app: {circle_area:.2f}")

print("[Main App] Program finished.")
