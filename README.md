# F1_Lap_Time_camp


## 🏁 F1 Lap Time Comparison Tool

This project uses the [FastF1](https://theoehrly.github.io/Fast-F1/) API to compare lap times of two Formula 1 drivers from a selected race. It provides a simple and interactive way to visualize how drivers performed across each lap of a Grand Prix.

### 🚀 Features

* Load race data from any F1 season (2018 onwards)
* Select any two drivers to compare
* Plot lap-by-lap time comparison
* Clean and interactive visualizations using `matplotlib`

### 📸 Preview

*(Include a screenshot of the plot here if you have one)*

### 🛠️ Tech Stack

* Python 🐍
* [FastF1](https://pypi.org/project/fastf1/)
* Matplotlib 📊
* (Optional) Seaborn for styling

### 📦 Installation

```bash
git clone https://github.com/yourusername/f1-lap-comparison
cd f1-lap-comparison
pip install -r requirements.txt
```

### 🔧 Usage

```bash
python lap_comparison.py
```

Edit the script to change:

* Year (`year`)
* Grand Prix (`gp`)
* Drivers (`driver1`, `driver2`)

### 📁 Caching

FastF1 requires a cache directory to store race data for faster future access.

```python
# Automatically creates the cache folder
import os
os.makedirs('./f1_cache', exist_ok=True)
fastf1.Cache.enable_cache('./f1_cache')
```

### 📌 TODO

* [ ] Add lap time delta visualization
* [ ] Add Streamlit web interface
* [ ] Compare telemetry data


