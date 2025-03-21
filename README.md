# 🌾 FarmTech Solutions - Agriculture Digital Application

## 🚀 Overview

FarmTech Solutions provides a simulation of a digital agriculture environment designed to assist farmers and agronomists in managing culture data, analyzing farm input requirements, and leveraging real-time climate metrics.

This cross-language solution is built using **Python** and **R**, each responsible for a specific segment of the agri-tech workflow:

### 🔧 Python Application
- Manage agricultural **culture records** interactively.
- Calculate **planting areas** based on geometric shapes (e.g., rectangles, triangles).
- Compute **fertilizer usage** per culture using user inputs like number of rows, application rate, etc.
- Export structured data as CSV files to the `cultures/` directory.
- Provides an **interactive command-line interface** for CRUD operations.

### 📊 R Applications
1. **`analysis.R`**
   - Processes exported CSV files to compute **basic descriptive statistics** (mean and standard deviation).
2. **`climate-metrics.R`**
   - Connects to a **public meteorological API**.
   - Fetches and displays **current weather conditions** directly in the terminal.

---

## 📁 Project Structure

├── app.py # Main entry point for the Python CLI application
├── helpers.py # Contains utility functions (e.g., area and input calculations)
├── cultures/ # Output directory for exported CSV culture data
├── analysis.R # R script for analyzing culture CSVs
├── climate-metrics.R # R script to fetch real-time weather metrics
└── README.md # Project documentation


---

## 🔧 Setup

### ✅ Python Environment
- Requires **Python 3.x**

## 🧪 R Environment Setup

- **Requires:** R 4.x (or later)
- **Required Packages:** `httr`, `jsonlite`

### 🔧 System Dependencies
Ensure system-level libraries are installed before adding R packages:

```bash
sudo apt-get update
sudo apt-get install libcurl4-openssl-dev libssl-dev pkg-config

sudo Rscript -e "install.packages('httr', repos='http://cran.rstudio.com/')"
sudo Rscript -e "install.packages('jsonlite', repos='http://cran.rstudio.com/')"
```


## ▶️ Running the Application

### 🐍 1. Python Application (CLI)

```bash
python app.py
```

## ⚙️ Features Overview

### 🐍 Python Application (CLI)

The Python application provides an **interactive menu-driven interface** for managing culture data and performing agri-specific calculations.

#### 🧰 Core Functionalities:
- ➕ **Add** new culture records
- 🔄 **Update** existing culture entries
- ❌ **Delete** culture records
- 👁️ **View** all stored cultures

#### 📐 Area Calculations:
- Supports two geometric planting area models:
  - Rectangle
  - Triangle

#### 🌾 Fertilizer Input Estimation:
- Calculates required inputs based on:
  - Application rate per meter
  - Number of planting rows

#### 💾 Data Export:
- All records can be exported to `.csv` format
- Files are saved automatically in the `cultures/` directory

---

### 📈 R Analysis Script

```bash
Rscript analysis.R
```
### 📈 R Analysis Script

#### 🔧 Functionality:
- Automatically scans all `.csv` files located in the `cultures/` directory.
- For each file, performs the following calculations:
  - 📉 **Mean**
  - 📈 **Standard Deviation**
- Displays a summary of statistics for each numeric column directly in the terminal.

---

### 🌦 R Climate Metrics Script

```bash
Rscript climate-metrics.R


---

### 🌦 R Climate Metrics Script

```bash
Rscript climate-metrics.R
```
#### 🌍 Functionality:

- Connects to a **public weather API** (e.g. [Open-Meteo](https://open-meteo.com)).
- Retrieves and displays **real-time weather data**, including:
- 🌡 **Temperature**
- 💨 **Wind speed and direction**
- 💧 **Humidity**
- All data is displayed directly in the **terminal** for immediate feedback.

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
You are free to use, modify, and distribute this software with proper attribution.
