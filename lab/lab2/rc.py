import math
import matplotlib.pyplot as f_vs_Xc


class RC():
    def __init__(self):
        # set values
        self.capacitor_value = 33.0*10**-9
        self.measured_capacitor_value = 34.7*10**-9
        self.voltage_capacitor_measured = 3.04
        self.resistance_measured = 10.1

        self.measured_voltage_of_resistors = [40.0,48.0,52.0,64.0,66.0,74.0,78.0]
        # computed values

        self.impedance = []
        self.impedance_compute_temp = 0.0
        self.frequency_temp = 0.0
        self.frequency = []
        self.impedance_measured_capacitor = []
        self.impedance_measured_capacitor_voltage = []


    def RC_compute(self):
        for count in range(0,7,1):
            temp = self.measured_voltage_of_resistors[count]/1000.0
            self.impedance_compute_temp = self.voltage_capacitor_measured * self.resistance_measured / temp
            self.impedance_measured_capacitor_voltage.append(self.impedance_compute_temp)
        for count in range (4,11,1):
            self.frequency_temp = count * 1000.0
            impedance_compute_temp = 1.0/(2.0*math.pi*self.capacitor_value* self.frequency_temp)
            self.frequency.append(self.frequency_temp)
            self.impedance.append(impedance_compute_temp)
            impedance_compute_temp = 1.0/(2.0*math.pi*self.measured_capacitor_value* self.frequency_temp)
            self.impedance_measured_capacitor.append(impedance_compute_temp)

    def impedance_plot(self):
        capacitor_predicted_line = f_vs_Xc.plot(self.frequency,self.impedance)
        impedance_measured_capacitor_line = f_vs_Xc.plot(self.frequency,self.impedance_measured_capacitor)
        impedance_measured_voltage_capacitor_line = f_vs_Xc.plot(self.frequency,self.impedance_measured_capacitor_voltage)
        f_vs_Xc.legend(["capacitor value predicted", "measured capacitor value calculated","Capacitor imppeadance by voltage measurement"])

        f_vs_Xc.show()

    def data_read(self):
        print(self.impedance)
        print(self.frequency)
        print(self.impedance_measured_capacitor)
        print(self.impedance_measured_capacitor_voltage)
