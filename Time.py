import fastf1
from fastf1 import plotting
import matplotlib.pyplot as plt
import os
import fastf1

# Create cache directory if it doesn't exist
os.makedirs('./f1_cache', exist_ok=True)

# Enable FastF1 cache
fastf1.Cache.enable_cache('./f1_cache')


# Enable cache (stores data locally so it loads faster next time)
fastf1.Cache.enable_cache('./f1_cache')  # create folder if needed

# Load race session
year = 2023
gp = 'Monaco'
session_type = 'R'  # R = Race, Q = Qualifying, FP1/2/3 = Practice

session = fastf1.get_session(year, gp, session_type)
session.load()

# Pick drivers
driver1 = 'VER'  # Verstappen
driver2 = 'ALO'  # Alonso

laps_driver1 = session.laps.pick_driver(driver1).pick_quicklaps()
laps_driver2 = session.laps.pick_driver(driver2).pick_quicklaps()

# Plot lap times
plt.figure(figsize=(12, 6))
plt.plot(laps_driver1['LapNumber'], laps_driver1['LapTime'].dt.total_seconds(), label=driver1)
plt.plot(laps_driver2['LapNumber'], laps_driver2['LapTime'].dt.total_seconds(), label=driver2)

plt.xlabel("Lap Number")
plt.ylabel("Lap Time (s)")
plt.title(f"Lap Time Comparison - {driver1} vs {driver2} ({year} {gp})")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
