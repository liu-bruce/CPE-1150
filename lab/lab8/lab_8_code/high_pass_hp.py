import matplotlib.pyplot as high_pass_plot

class high_pass():

    def __init__(self):
        self.frequency_values = [1000.0,2000.0,4000.0,7000.0,8244.2,8809.7,11050.0,11120.0,20000.0,40000.0,100000.0]
        self.phase_angles = [-83.91,-78.69,-68.28,-55.57,-51.13,-51.01,-42.66,-42.55,-27.16,-14.73,-6.19]
        self.input_Voltage = 3.0
        self.output_Voltage = [0.304,0.592,1.10,1.66,1.82,1.82,2.12,2.12,2.48,2.68,2.76]

        self.dB =[]
        self.dB_temp =0
    def dB_compute(self):
        for count in range(0,11,1):
            self.dB_temp = self.output_Voltage[count]/self.input_Voltage
            self.dB.append(self.dB_temp)

    def Low_pass_graph_phase_angle(self):
        labels = high_pass_plot.figure()
        labels.subplots_adjust(top=0.8)
        axis = labels.add_subplot(211)
        axis.set_ylabel('degrees')
        axis.set_xlabel('frequency')
        axis.set_title('bode plot frequency vs degrees')

        high_pass_plot.semilogx(self.frequency_values,self.phase_angles)
        high_pass_plot.show()

    def Low_pass_graph_dB(self):
        labels = high_pass_plot.figure()
        labels.subplots_adjust(top=0.8)
        axis = labels.add_subplot(211)
        axis.set_ylabel('dB')
        axis.set_xlabel('frequency')
        axis.set_title('bode plot frequency vs dB')

        high_pass_plot.semilogx(self.frequency_values,self.dB)
        high_pass_plot.show()

    def dB_print(self):
        for count in range(0,11,1):
            print (self.dB[count])
