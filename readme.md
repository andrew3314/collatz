# Collatz
A simple script that generates svg files with Collatz graphs for any given limit of numbers.

## Running
First, make sure you have the latest distribuition of Graphviz installed (check https://graphviz.org/download/ case you don't).

Once you got all done, run it like the following: 

````
py collatz_graph.py -n [the limit number, default is 20] -p [layout mode (check Graphviz docs on it)]
````

## Example
Running the following from your command line

````
py collatz_graph.py -n 15
````

You should get something like this
![example graph](https://www.github.com/andrew3314/collatz/main/collatz-graph.svg)
