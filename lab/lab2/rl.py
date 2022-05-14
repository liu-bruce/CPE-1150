import math
import matplotlib.pyplot as XL_vs_f


class RL():

    def __init__(self):
        self.measured_voltage_of_inductor = 3.04
        self.measured_control_resitor_values = [120,96.0,80.0,68.0,64.0,56.0,56.0]
        self.control_resistor = 10.1
        self.frequency_set_values = [3000,4000,5000,6000,7000,8000,9000]
        self.inductor_measured = 13.67*10**-3
        self.inductor_value = 15*10**-3

        # conputed value
        self.inductor_impedance_calculated = []
        self.inductor_compute_temp = 0.0
        self.inductor_values_measured = []
        self.inductor_value_theoretical =[]

    def RL_compute(self):
        # computes the impeadance of the experiment
        for count in range(0,7,1):
            self.inductor_compute_temp = self.measured_voltage_of_inductor * self.control_resistor /( self.measured_control_resitor_values[count]*10**-3)
            self.inductor_impedance_calculated.append(self.inductor_compute_temp)

        #2*pi* f*L
        for count in range (0,7,1):
            self.inductor_compute_temp = 2.0*self.frequency_set_values[count] * math.pi * self.inductor_measured
            self.inductor_values_measured.append(self.inductor_compute_temp)
            self.inductor_compute_temp = 2.0*self.frequency_set_values[count] * math.pi * self.inductor_value
            self.inductor_value_theoretical.append(self.inductor_compute_temp)

    def RL_plot(self):
        XL_vs_f.plot(self.frequency_set_values,self.inductor_value_theoretical)
        XL_vs_f.plot(self.frequency_set_values,self.inductor_values_measured)
        XL_vs_f.plot(self.frequency_set_values,self.inductor_impedance_calculated)
        XL_vs_f.legend(["theoretical values","Calculated with measured inductor", "experimental impedance"])
        XL_vs_f.show()

    def RL_data_read(self):

        print("experimental values\n")
        print(self.inductor_impedance_calculated)
        print('\n')
        print("measured inductor values\n")
        print(self.inductor_values_measured)
        print('\n')
        print("On the box values\n")
        print(self.inductor_value_theoretical)
        print('\n')
