### Time complexity

time complexity estimates how the running time grows as the input size (n) increases.
and the calculations are denoted as O(n), O(n^2), O(n log n) and so on....

students = [1, 2, ..., 100]  # List of 100 students
count = 0
for student in students:  # This loop runs n times
    count += 1  # One operation per iteration

here the time complexity is O(n)

if it is a nested loop

pairs = 0
for i in students:  # Outer loop: n times
    for j in students:  # Inner loop: n times each
        if i != j:
            pairs += 1  # Up to n * n = n² operations

the time complexity is O(n^2)

### space complexity

how much extra memory your algorithm needs to run

space complexity tells you, your algorithm is efficient or not

function sum(a, b) {
  let result = a + b;
  return result;
}

here 3 simple varibles, memory does not increase even with bigger values

function createArray(n) {
  let arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(i);
  }
  return arr;
}

We create an array with n elements

If n = 10 → 10 elements

If n = 1,000 → 1,000 elements

Memory grows as input grows.

So space complexity = O(n) (memory grows with input).