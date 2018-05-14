#from multiprocessing import Process, Queue
import time
import queue
import matplotlib.pyplot as plt
from core import Event
from core import DataHandler
from core import ExecutionHandler
from core import Portfolio
from core import Algorithm

#Handle Event production


class EventProcessor:

    def __init__(self, start_date, buffer_size=200, heartbeat=600):
        self.switch = True
        self.heartbeat = heartbeat
        self.buffer_size = buffer_size
        self.buffer = queue.Queue()
        self.buffer.maxsize = buffer_size
        self.start_date = start_date
        # Declare the components with respective parameters
        self.bars = DataHandler.HistoricCSVDataHandler(self.buffer, 'core', ['BTC', 'ETH'])
        self.strategy = Algorithm.BuyAndHoldAlgorithm(self.bars, self.buffer)
        self.port = Portfolio.NaivePortfolio(self.bars, self.buffer, self.start_date)
        self.broker = ExecutionHandler.SimulatedExecutionHandler(self.buffer)

    def get_buffer(self):
        return self.buffer

    def add_to_buffer(self, events):
        for e in events:
            self.buffer.put(e)

    def handle_events(self, buffer):
        while True:
            try:
                '''
                    try to get task from the queue. get_nowait() function will 
                    raise queue.Empty exception if the queue is empty. 
                    queue(False) function would do the same task also.
                '''
                event = buffer.get_nowait()

            except queue.Empty:
                print("empty queue")
                break

            else:
                '''
                    if no exception has been raised, add the task completion 
                    message to task_that_are_done queue
                '''
                if event.type == 'MARKET':
                    print(event.type)
                    self.strategy.compute_signals(event)
                    self.port.update_timeindex(event)

                elif event.type == 'SIGNAL':
                    print(event.type)
                    self.port.update_signal(event)

                elif event.type == 'ORDER':
                    print(event.type)
                    self.broker.execute_order(event)

                elif event.type == 'FILL':
                    print(event.type)
                    self.port.update_fill(event)

        return True

    '''
    Switch on/off the processor
    '''
    def switch_off(self):
        self.switch = False

    def switch_on(self):
        self.switch = True

    def run(self):
        #processes = []

        while self.switch:
            # Update the bars (specific backtest code, as opposed to live trading)
            if self.bars.continue_backtest == True:
                self.bars.update_bars()
            else:
                break
            #first try to multi thread core of processing : fail
            """
            for i in range(number_of_processes):
                p = Process(target=self.handle_events, args=(self.buffer,))
                processes.append(p)
                p.start()

            for p in processes:
                p.join()
            """
            self.handle_events(self.buffer)

            time.sleep(self.heartbeat)

'''
testing purpose, to be outsourced in the test class or main
'''

def main():
    number_of_task = 70
    perf_log = []

    for nb in range(1, 5):

        # Performance measure
        start = time.time()
        print("---------------- Run Beginning ----------------")
        print('number of process launched : ' + str(nb))
        ep = EventProcessor()
        for i in range(number_of_task):
            event = Event.Event('test', 'test')
            ep.add_to_buffer(event)

        ep.run(nb)
        perf = time.time() - start
        print('Run ends in : ' + str(perf) + 's')
        perf_log.append(perf)

    print(perf_log)
    plt.plot(perf_log)
    plt.ylabel('Performance plot')
    plt.show()

    return True

if __name__ == '__main__':
    main()