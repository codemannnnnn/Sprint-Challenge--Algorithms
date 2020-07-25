#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n). This is similar to a for loop in the sense that the loop executes N times. meaning eventually it'll stop once a > n^3.

b) LogN. We have a nested while loop in a for loop, meaning we are performing double the operations.

c) O(n). The function is callings itself once, recursively until it reaches its base case.

## Exercise II

We could use a binary search algo for this. Where we start at the top and see if we break an egg, then cut the tree in half and see if we break and egg. Then keeping the same pattern we would continue until we reached a point where we no longer are breaking eggs below us. Once we find the position where we no longer are breaking an egg below us we know we are on the right floor.

By starting at the top, then cutting the tree in half, we are minimizing our broken eggs. We only would break 2 eggs before cutting our solution in half, then continuing the pattern until we reach our solution. I think Sean mentioned it only takes 20 moves to search a bst that has one million items in it.

O(log n), not many operations until we find our value.
