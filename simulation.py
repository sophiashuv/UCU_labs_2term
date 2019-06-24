from arrays import Array
from llistqueque import Queue
from simpeople import*
import random


class TicketCounterSimulation:
    """Create a simulation object."""
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        """ Parameters supplied by the user."""
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
         # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i+1)
         # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        """
        Run the simulation using the parameters supplied earlier.
        """
        for curTime in range(self._numMinutes + 1):
              self._handleArrive(curTime)
              self._handleBeginService(curTime)
              self._handleEndService(curTime)

    def printResults(self):
        """
        Print the simulation results.
        """
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)

    def _handleArrive(self, curTime):
        """
        The function prints the customer arrived
        """
        if self._arriveProb > random.random():
            passenger = Passenger(self._numPassengers, curTime)
            self._passengerQ.enqueue(passenger)
            print("Passenger {} arrived at {}".format(self._numPassengers, curTime))
            self._numPassengers += 1

    def _handleBeginService(self, curTime):
        """
        The function prints thar the agent started serving the customer
        """
        if not(self._passengerQ.isEmpty()):
            ag = 0
            for cashier in self._theAgents:
                try:
                    if cashier.isFree():
                        curPassenger = self._passengerQ.dequeue()
                        self._theAgents[ag].startService(curPassenger, curTime + self._serviceTime)
                        self._totalWaitTime += curTime - curPassenger.timeArrived()
                        print("Agent {} started serving passenger {} at {}".format(ag, curPassenger.idNum(), curTime))
                        break
                except IndexError:
                    break
                ag += 1

    def _handleEndService(self, curTime):
        """
        The function prints thar the agent finished serving the customer
        """
        for ag in self._theAgents:
            if ag.isFinished(curTime):
                curPassenger = ag.stopService()
                print("Agent {} finished serving passenger {} at {}".format(ag.idNum(),
                                                                            curPassenger.idNum(), curTime))

if __name__ == "__main__":
    c = TicketCounterSimulation(20, 1000, 4, 60)
    c.run()
    c.printResults()
