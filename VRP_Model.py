import random
import math


class Model:

# instance variables
    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.routes = []
        self.matrix = []
        self.capacity = -1

    def BuildModel(self):
        random.seed(5112001)
        depot = Node(0, 50, 50, 0, 0)
        self.allNodes.append(depot)

        self.capacity = 150
        totalCustomers = 300
        availableTrucks = 5
        for i in range (0, totalCustomers):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            service_time = random.randint(5, 10)
            profit = random.randint(5, 20)
            cust = Node(i + 1, x, y, profit, service_time)
            self.allNodes.append(cust)
            self.customers.append(cust)

        rows = len(self.allNodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]
        
        for i in range(0, availableTrucks): 
            newRoute = Route(self.capacity, depot)
            self.routes.append(newRoute)

        for i in range(0, len(self.allNodes)):
            for j in range(0, len(self.allNodes)):
                a = self.allNodes[i]
                b = self.allNodes[j]
                dist = math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))
                self.matrix[i][j] = dist

class Node:
    def __init__(self, idd, xx, yy, profit, st):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.service_time = st
        self.profit = profit
        self.isRouted = False

class Route:
    def __init__(self, cap, depot):
        self.sequenceOfNodes = [depot, depot]
        self.profit = 0
        self.capacity = cap
        self.load = 0