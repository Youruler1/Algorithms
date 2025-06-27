def fractional_knapsack(capacity, weights, values):
    n = len(weights)
    # Calculate value to weight ratio for each item
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))
    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_value = 0.0
    for ratio, weight, value in items:
        if capacity == 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0
    return total_value

# Example usage:
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_value = fractional_knapsack(capacity, weights, values)
    print(f"Maximum value in knapsack: {max_value}")


def fractional_knapsack(capacity, weights, values):
    items = []
    r = lambda x, y: x/y
    n = len(weights)

    for i in range(1,n):
        items.append((r(weights[i], values[i]), weights[i], values[i]))

    items.sort(reverse = True)

    total_value = 0.0
    for ratio, weight, value in items:
        if capacity == 0:
            return total_value
        if (weight <= capacity):
            total_value += value
            capacity -= weight
        else:
            total_value += (capacity / weight) * value
            return total_value
    # when iteration terminates without completely filling knapsack capacity
    return total_value  






## MY LEARNINGS:
# mutable types: primitives like bool, int, float, string 
# immutable types: 


# x = 10
# x = 20
# What’s happening?
# x = 10 → x points to an int object 10.
# x = 20 → x now points to a different int object 20.
# The original 10 object is untouched; x just refers to something else now.
# So you're not changing the value 10; you're reassigning x.




# ⚙️ Argument Analysis:
# ✅ capacity – Immutable (int)
# Passed by value (in effect).

# Since integers are immutable, even though Python passes a reference to the integer object, you can’t modify the original capacity from inside the function.

# Any reassignment (like capacity = 0) does not affect the original variable outside the function.

# ✅ weights and values – Mutable (list)
# Passed by reference (in effect).

# Lists are mutable, so any in-place modifications to weights or values will reflect outside the function.

# However, in your function, you're only r