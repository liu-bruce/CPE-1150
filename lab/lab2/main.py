from rc import RC
from rl import RL

def main():
    rl = RL()
    rl.RL_compute()
    rl.RL_plot()
    rl.RL_data_read()

    """
    rc = RC()
    rc.RC_compute()
    rc.impedance_plot()
    rc.data_read()

    """
if __name__ == '__main__':
    main()
