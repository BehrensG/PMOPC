import pyvisa
import csv 
rm = pyvisa.ResourceManager()

dmm = rm.open_resource('TCPIP0::192.168.1.3::5025::SOCKET')
dmm.write_termination = '\n'
dmm.read_termination = '\n'
dmm.timeout = 1000 
print(dmm.query('*IDN?'))
dmm.write('*RST')
dmm.write('*CLS')
dmm.write('CONF:VOLT:DC AUTO')
dmm.write('SENS:VOLT:DC:NPLC 10')
filename = "volt_load_20mm_cool.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write only the column header
    writer.writerow(['Voltage (V)'])
    
    for i in range(1, 10001):
        
        voltage = float(dmm.query('READ?'))
        print(f'Sample : {i}, READ : {voltage}')
        writer.writerow([voltage])