# lso_assignment

LSO assignment Winter semester 21

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
