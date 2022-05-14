import matplotlib.pyplot as Low_pass_plot

class low_pass():

    def __init__(self):
        self.frequency_values = [100.0,500.0,1000.0,2000.0,3810.0,3900.0,5916.3, 6207.0,10000.0,20000.0,50000.0]
        self.phase_angles = [0.76,1.32,9.44,18.15,32.27,32.74,44.28,45.63,60.95,73.53,91.62]
        self.input_Voltage = 3.0
        self.output_Voltage = [2.48,2.48,2.44,2.36,2.12,2.12,1.80,1.76,1.36,0.84,0.40]

        self.dB =[]
        self.dB_temp =0
    def dB_compute(self):
        for count in range(0,11,1):
            self.dB_temp = self.output_Voltage[count]/self.input_Voltage
            self.dB.append(self.dB_temp)

    def Low_pass_graph_phase_angle(self):
        labels = Low_pass_plot.figure()
        labels.subplots_adjust(top=0.8)
        axis = labels.add_subplot(211)
        axis.set_ylabel('degrees')
        axis.set_xlabel('frequency')
        axis.set_title('bode plot frequency vs degrees')

        Low_pass_plot.semilogx(self.frequency_values,self.phase_angles)
        Low_pass_plot.show()

    def Low_pass_graph_dB(self):
        labels = Low_pass_plot.figure()
        labels.subplots_adjust(top=0.8)
        axis = labels.add_subplot(211)
        axis.set_ylabel('dB')
        axis.set_xlabel('frequency')
        axis.set_title('bode plot frequency vs dB')

        Low_pass_plot.semilogx(self.frequency_values,self.dB)
        Low_pass_plot.show()

    def dB_print(self):
        for count in range(0,11,1):
            print (self.dB[count])
            print("\n")
