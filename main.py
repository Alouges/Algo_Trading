from core import Event_Processor
import matplotlib.pyplot as plt
from core import DataHandler
from core import ExecutionHandler
from core import Algorithm
from core import analytics

def main():

    ep = Event_Processor.EventProcessor(start_date = '2018-04-03 23:25:00',
                                        heartbeat=0.00)
    ep.run()
    ep.port.create_equity_curve_dataframe()
    print(ep.port.output_summary_stats())
    print(ep.port.equity_curve)
    plt.plot(ep.port.equity_curve['returns'])
    plt.show()

if __name__ == '__main__' :
    main()