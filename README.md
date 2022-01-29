# lso_assignment

LSO assignment Winter semester 21
Student: Stavros Sotiropoulos (ID: p2822018)

### Model Creation

Creating the model follows the predefined process. The only difference is (apart from the numbers), the creation of a fixed number of Routes, one for each truck, that are passed in the solvers.

### Creating the solution

The idea behind the solution is:

- Sort the customers based on Profit/ServiceTime to get the probably best customers routed first.
- Iterate over the list until a customer can not fit in any route
- In each iteration find the best fitting customer, who maximises the profit and has smaller cost. Cost for a customer is the costToVisitCustomer + customerServiceTime.
- In order for a customer to be considered, the CustomerCost (serviceTime+VisitCost) must be < RouteTimeCapacity
- After finding the best fit, add him to the route that maximises the value Profit/Cost, with emphasis on Profit (by multiplying with a number)
- If no customers are found as best fits, the process is finished and we have a complete solution with total profit the sum of profits of each route

### VND

#### Relocation

- To have a valid relocation we must check the sum of costs bellow do not exceed the capacity
  - Current route load
  - customer service time
  - customer added distance cost (F-B & B-G)
  - Previous inbetween customer distance cost (F-G)
- We do not include service time in the move cost calculation, as is included in the AddedCost and substrated from the RemovedCost
- We do change the load of the routes in both cases
  - If relocation occurs in first route, it removes some customerDistance cost
  - If it occurs in different routes, the values are substracted accordingly

#### Swap

- Similar to above, if relocation occurs in the same route, serviceTime & Profit do not play a role
- If it happens between two routes, we must check:
  - The addition of serviceTime & CustomerReachTime does not exceed the routes' time capacities
- When applying the move
  - If applied in the same route, update only the customerReachTime cost
  - If on separate routes, update reach time costs with additionally service times, and route profits as well

#### Customer Insertion

- Simply apply the insertion proccess once more (covers only non Routed customers)
