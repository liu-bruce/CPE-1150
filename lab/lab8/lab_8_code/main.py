from low_pass_lp import low_pass
from high_pass_hp import high_pass

def main():
    lp = low_pass()
    hp = high_pass()

    hp.dB_compute()
    hp.dB_print()
    hp.Low_pass_graph_phase_angle()
    hp.Low_pass_graph_dB()
    """
        lp.dB_compute()
        #lp.dB_print()
        lp.Low_pass_graph_phase_angle()
        lp.Low_pass_graph_dB()
    """
if __name__ == '__main__':
    main()
