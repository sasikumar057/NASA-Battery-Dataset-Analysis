import pandas as pd 
import plotly.express as px  

data = pd.read_csv('./metadata.csv')  
print(data.head()) 
print(data.info()) 

data_filtered = data[['test_id', 'Re', 'Rct']]


data_filtered['Re'] = pd.to_numeric(data_filtered['Re'], errors='coerce')
data_filtered['Rct'] = pd.to_numeric(data_filtered['Rct'], errors='coerce')


data_filtered = data_filtered.dropna()

fig_re = px.line(
    data_filtered,  
    x='test_id', 
    y='Re',  
    title='Estimated Electrolyte Resistance (Re) vs Aging Cycles',
    labels={'test_id': 'Test Cycle Index', 'Re': 'Electrolyte Resistance (Ohms)'} 
)
fig_re.show()  

fig_rct = px.line(
    data_filtered,  
    x='test_id', 
    y='Rct', 
    title='Estimated Charge Transfer Resistance (Rct) vs Aging Cycles',
    labels={'test_id': 'Test Cycle Index', 'Rct': 'Charge Transfer Resistance (Ohms)'}  
)
fig_rct.show() 
