import matplotlib.pyplot as sine_plot
import math

class Lab_1_CPE_1150():
    def __init__(self):
        self.time_increment = 100* 10**-6
        self.peak_voltage = 2.0
        self.omega = 2.0 * math.pi * 1000
        self.sine_voltage_values = []
        self.time_increment_history = []
        self.sine_voltage_values_temp = 0.0

    def sine_compute(self):
        for count in range(0 ,11 ,1):
            self.time_increment_history.append(self.time_increment * count)
            self.sine_voltage_values_temp = self.peak_voltage * math.sin(self.omega * (self.time_increment * count))
            self.sine_voltage_values.append(self.sine_voltage_values_temp)
    def sine_graph(self):
        sine_plot.plot(self.time_increment_history, self.sine_voltage_values)
        sine_plot.suptitle("sine plot")
        sine_plot.xlabel("Time in seconds")
        sine_plot.ylabel("Voltage")
        sine_plot.show()

    def value_read(self):
        print(self.sine_voltage_values)
        print("\n\n")
