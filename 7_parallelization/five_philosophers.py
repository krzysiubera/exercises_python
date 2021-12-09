import threading
import time
import random


class Philosopher(threading.Thread):
    """
    A class representing a philosopher. Each one has his own index, and corresponding forks on left and right hand side
    """

    def __init__(self, philosopher_number, left_fork, right_fork):
        super().__init__()
        self.philosopher_number = philosopher_number
        self.left_fork = left_fork
        self.right_fork = right_fork

    def try_to_eat(self):
        self.left_fork.acquire()
        self.right_fork.acquire()

        print(f"Philosopher no {self.philosopher_number} is eating")
        time.sleep(4)
        print(f"Philosopher no {self.philosopher_number} has stopped eating")

        self.left_fork.release()
        self.right_fork.release()

    def run(self):
        while True:
            print(f"Philosopher no {self.philosopher_number} is thinking")
            time.sleep(random.randint(1, 6))
            self.try_to_eat()


if __name__ == '__main__':
    forks = [threading.Condition(threading.Lock()) for idx in range(5)]
    philosophers = [Philosopher(idx, forks[idx], forks[(idx + 1) % 5]) for idx in range(5)]

    for philo in philosophers:
        philo.start()


