<h1>NASA Battery Dataset Analysis</h1>

This project uses the NASA Battery Dataset to analyze and visualize how key parameters of Li-ion batteries change during aging through repeated charge/discharge cycles. The parameters include Battery Impedance, Estimated Electrolyte Resistance (Re), and Charge Transfer Resistance (Rct). The visualization is done using Plotly, an interactive plotting library.


<h2>Dataset</h2>

The dataset used in this project can be found on Kaggle: NASA Battery Dataset.
<h2>Dataset Details:</h2><br>
    *  A set of Li-ion batteries were run through various operational profiles (charge, discharge, and impedance) at different temperature<br>
    *  Impedance was measured using electrochemical impedance spectroscopy (EIS) in a frequency range of 0.1Hz to 5kHz.<br>
    *  The experiments continued until the batteries reached their end-of-life (EOL) criteria.<br>

<h2>Objective</h2>

The goal of this project is to:

  Visualize how Battery Impedance, Re, and Rct evolve as the battery ages.
  provide insights into how repeated charge/discharge cycles affect battery performance.

This project focuses on data visualization and analysis, aligning with the given assignment requirements.
Features

  1.Interactive Plots:
        Visualize Battery Impedance trends over charge/discharge cycles.
        Track changes in Re and Rct over time.
        Identify patterns and insights from the aging process.

  2.Data Cleaning and Preparation:
        Missing values are handled to ensure clean and accurate visualizations.
        The dataset is filtered for relevant parameters.

  3.Key Observations:
        Analyze how battery degradation affects electrolyte resistance and charge transfer resistance.

<h2>Technologies Used</h2>

  * Python for data analysis and visualization.
  * Pandas for data cleaning and manipulation.
  * Plotly for creating interactive plots.
  * Jupyter Notebook (optional) for exploratory analysis.

<h2>Installation</h2>

Follow these steps to set up and run the project:

Clone this repository:

    git clone https://github.com/yourusername/nasa-battery-analysis.git
    cd nasa-battery-analysis

Install dependencies:

    pip install -r requirements.txt

Download the dataset:

  Go to Kaggle: NASA Battery Dataset.<br>
  Place the dataset in the dataset/ folder.

Run the analysis:

    python battery_analysis.py

<h2>Results</h2>

This project provides the following insights:

  Battery Aging: Visualizes how key parameters (Impedance, Re, Rct) evolve with repeated charge/discharge cycles.
  Performance Trends: Helps understand how degradation impacts the battery's internal properties.

  
