# Collatz
A simple script that generates svg files with Collatz graphs for any given limit of numbers.

## Running
First, make sure you have the latest distribuition of Graphviz installed(check https://graphviz.org/download/ case you don't). Also remember to setup a virtual enviroment for running the code(you can use venv).

````
py -m venv env 
````
````
.\env\Scripts\activate
````

Once you got all that done, run it like the following: 

````
py collatz_graph.py -n [the limit number, default is 20] -p [layout mode (check Graphviz docs on it)]
````