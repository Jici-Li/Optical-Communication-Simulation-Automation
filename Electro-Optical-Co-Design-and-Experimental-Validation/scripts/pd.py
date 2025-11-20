import pandas as pd
import matplotlib.pyplot as plt

power_data = pd.read_csv('D:/Users/lij16/MZM_report/d.csv')
signal_data = pd.read_csv('D:/Users/lij16/MZM_report/data_2.csv')  

merged_data = pd.merge(signal_data, power_data, on='Time(ms)', how='inner')

signal = merged_data['Electrical Signal(a.u.)'].values

start_idx = 0
while signal[start_idx] > 0.1:  
    start_idx += 1

end_idx = start_idx
while end_idx < len(signal) and signal[end_idx] < 3.14:
    end_idx += 1

cropped_data = merged_data.iloc[start_idx:end_idx]

plt.figure(figsize=(10, 6))
plt.plot(cropped_data['Electrical Signal(a.u.)'], cropped_data['Power(mW)'], 'b-', linewidth=2)
plt.xlabel('Voltage (V)', fontsize=12)
plt.ylabel('Power (mW)', fontsize=12)
plt.title('Voltage(0→6.28) vs Power', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

