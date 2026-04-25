 #### lists
 the list is a ordered data structure --> ordered in the sense they are stored as stated in the initilization
 indexing, they start at zero
 slicing list[1:3] --> it includes the elements form 1 to 2, beacuse python skips the last element
 list comprehension --> [x**x for i in range(1,5) if x%2 == 0] --> this creates a list of number that even from 1 to 4
 memory optimization --> appending with time complexity is O(1) and adding element at specific index is O(n), because every item has to shift over
 Deep vs Shallow copy --> list_a = list_b this creates a reference and if we want to create a complete copy, use .copy()


#### tuples
 tuples are immutable once its made it is set to stone
 syntax my_tuple = (10,20,30)
 Use them for things that shouldn't change, like the coordinates of a city or RGB color values.
 x, y = (5, 10). This is how Python functions "return" multiple values.
 Because they are immutable, they can be used as keys in a dictionary
 Tuples are slightly faster and more memory-efficient than lists because Python knows their size won't change.
 From the collections module, these allow you to access elements by name (e.g., point.x) instead of just index

 #### dictinories
 a collection of key-value pairs
 my_dict = {"name": "Alice", "age": 25}
 my_dict["name"]
 .get() is safer than square brackets because it won't crash your code if the key is missing.
 {k: v for k, v in some_data} --> dictinorie comprehension
 Dictionaries use a hash table under the hood. This makes lookups incredibly fast—$O(1)$ on average—regardless of how big the dictionary is.

 #### sets
 Unordered collections of unique items. No duplicates allowed!
 my_set = {1, 2, 3, 3, 3} (The extra 3s will be ignored).
 Instantly removing duplicates from a list: list(set(my_list)).
 This is where sets shine. You can perform math-like operations:
 Union (|): Everyone in both sets.
 Intersection (&): Only people in both.
 Difference (-): People in A but not in B.
#  Like dictionaries, checking if "item" in my_set is $O(1)$. Doing the same for a list is $O(n)$, meaning it gets slower as the list grows.

