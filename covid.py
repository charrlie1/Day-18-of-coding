import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd

# --- Simple Assumed Simulation Function ---
def simulate_covid(params):
    """A very simplified simulation of COVID-19 spread."""
    time = np.arange(0, params.get('duration', 100))
    infected = (params.get('initial_infections', 10) *
                np.exp(0.05 * time) /
                (1 + np.exp(0.05 * (time - params.get('peak_day', 30))))) * params.get('population', 1000000) / params.get('population_scale', 1000000)
    infected[infected < 0] = 0
    return pd.DataFrame({'time': time, 'infected': infected})

# Define some parameters for the simulation
simulation_params = {
    'population': 330000000,
    'initial_infections': 100,
    'duration': 120,
    'peak_day': 45,
    'population_scale': 1000000  # Scale down for visualization
}

# Run the assumed simulation
simulation_results = simulate_covid(simulation_params)

# --- Assumed US COVID-19 Case Data ---
# Creating a sample DataFrame with dates and case counts
dates = pd.to_datetime(pd.date_range(start='2025-01-01', periods=100))
cases = (np.sin(np.linspace(0, 10, 100)) * 50000 + 50000 + np.random.normal(0, 5000, 100)).astype(int)
cases[cases < 0] = 0
us_covid_data_assumed = pd.DataFrame({'date': dates, 'cases': cases})

# --- Interactive Plotting with Plotly ---
fig = make_subplots(rows=1, cols=1)

# Add the assumed simulated infections
fig.add_trace(go.Scatter(x=simulation_results['time'], y=simulation_results['infected'],
                         mode='lines', name='Assumed Simulated Infections'), row=1, col=1)

# Add the assumed US COVID-19 case data
fig.add_trace(go.Scatter(x=us_covid_data_assumed['date'], y=us_covid_data_assumed['cases'],
                         mode='lines', name='Assumed Reported Cases', line=dict(dash='dash')), row=1, col=1)

# Update layout for better presentation
fig.update_layout(
    title='Assumed Simulated and Reported COVID-19 Cases in the USA (Interactive)',
    xaxis_title='Days (Simulation) / Date (Reported Cases)',
    yaxis_title='Number of Individuals',
    hovermode='closest'  # Enable hover information
)

fig.show()