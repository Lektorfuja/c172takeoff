import time

def pre_flight_checklist():
    print("Pre-Flight Checklist:")
    steps = [
        "Check fuel quantity and quality",
        "Inspect control surfaces and flaps",
        "Verify oil level and engine condition",
        "Ensure avionics and instruments are operational",
        "Fasten seatbelts and adjust seating position"
    ]
    for step in steps:
        while input(f"{step} - Type 'yes' to confirm: ").strip().lower() != "yes":
            pass
    print("Pre-flight checklist complete!\n")

def engine_start():
    print("Starting Engine:")
    steps = [
        "Master switch ON",
        "Fuel selector BOTH",
        "Mixture RICH",
        "Throttle 1/4 OPEN",
        "Ignition START"
    ]
    for step in steps:
        while input(f"{step} - Type 'yes' to proceed: ").strip().lower() != "yes":
            pass
    print("Engine started successfully!\n")

def taxi():
    print("Taxiing to runway...")
    time.sleep(2)
    print("Check brakes, rudder control, and wind conditions.")
    while input("Type 'yes' when ready to line up on the runway: ").strip().lower() != "yes":
        pass
    print("Lined up on the runway!\n")

def takeoff():
    print("Takeoff Roll:")
    while input("Apply full throttle - Type 'yes' to proceed: ").strip().lower() != "yes":
        pass
    print("Accelerating...")
    time.sleep(2)
    print("Airspeed alive! Checking instruments...")
    time.sleep(2)
    while input("At 55 knots, pull back slightly on the yoke - Type 'yes' to rotate: ").strip().lower() != "yes":
        pass
    print("Liftoff! You are airborne.\n")

def climb():
    print("Climbing out:")
    while input("Maintain Vy (79 knots) for best climb - Type 'yes' to confirm: ").strip().lower() != "yes":
        pass
    time.sleep(2)
    print("Passing 500 feet, reducing power to climb setting.")
    while input("At 1000 feet AGL, adjust to cruise climb - Type 'yes' to confirm: ").strip().lower() != "yes":
        pass
    print("Takeoff and initial climb successful!\n")

def main():
    print("Welcome to the Cessna 172 SP Takeoff Simulator!")
    pre_flight_checklist()
    engine_start()
    taxi()
    takeoff()
    climb()
    print("You have successfully taken off in the Cessna 172 SP! Safe flying!")

if __name__ == "__main__":
    main()
