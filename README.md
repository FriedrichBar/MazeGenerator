# Projet 2020 Maze Runner

## Promotion Cybersécurité du Logiciel 2020-2023

## How it works

`python3 ProjetLabyrinthe.py`

Program returns a picture of the maze named "Maze.png".

The red cell corresponds to the goal, black cells to walls and white cells to paths.

The user can move from one cell to another horizontally, vertically and diagonally.

## Benchmark

The program used to do the benchmark is included in the zip archive. To execute it, simply write `python3 benchmark.py`.

L = Length

w = width

N = Number of cells

| L | w   |N      | Time  | N/Time |
|---|-----|-------|-------|--------|
|5  |5    |25     |0.0020s|12500   |
|25 |25   |625    |0.0560s|11160   |
|50 |50   |2500   |0.2149s|11633   |
|75 |75   |5625   |0.4898s|11484   |
|100|100  |10000  |0.8967s|11152   |
|150|150  |22500  |2.0102s|11192   |
|175|175  |30625  |2.7111s|11296   |
|200|200  |40000  |3.5317s|11326   |
|250|250  |62500  |5.6758s|11011   |
|300|300  |90000  |7.9880s|11267   |
|500|500  |250000 |22.693s|11016   |
|750|750  |562500 |51.054s|11017   |
|1000|1000|1000000|90.844s|11008   |

Comparing these results with another student who didn't use numpy, we can see that our generating times are far more longer.

This is due when we are checking for neighbors. Indeed, numpy.sum() is way more slower than sum() for lists.



![alt text](https://i.ibb.co/PgDhr9R/np.png "Speed Graph")

Not having enough time left, I decided to stay with numpy. Even if our generation is slower, we can still keep it and compare with other algorithms.


## Complexity

After our benchmark, when we compare the values of N/Time, we can see that whenever N gets big, we have a smaller gap between our values.

We can say that our program has a complexity equal to O(n).

## Author

Friedrich Bär