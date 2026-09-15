import pandas as pd
import numpy as np

INPUT_FILE = "vehicle_sensor_data.csv"
OUTPUT_FILE = "vehicle_sensor_data_AEB_output.csv"

# Assumption:
# speed is in m/s, obstacle_distance is in metres,
# and timestamp is in seconds.
df = pd.read_csv(INPUT_FILE)

# Calculate Time To Collision (TTC).
# For zero speed, TTC is infinite because the vehicle is not moving.
df["time_to_collision"] = np.where(
    df["speed"] > 0,
    df["obstacle_distance"] / df["speed"],
    np.inf
)

# AEB triggers when TTC is strictly less than 2 seconds.
df["emergency_brake"] = (df["time_to_collision"] < 2.0).astype(int)

# Count separate AEB events: each 0 -> 1 transition is one event.
aeb_starts = (
    (df["emergency_brake"] == 1)
    & (df["emergency_brake"].shift(1, fill_value=0) == 0)
)
number_of_aeb_events = int(aeb_starts.sum())

# Find the closest detected obstacle.
closest_obstacle = df["obstacle_distance"].min()

# Save the updated CSV.
df.to_csv(OUTPUT_FILE, index=False)

print("AEB Trigger Detection")
print("---------------------")
print(f"Number of AEB events: {number_of_aeb_events}")
print(f"Closest obstacle: {closest_obstacle:.2f} m")
print(f"Updated CSV saved as: {OUTPUT_FILE}")