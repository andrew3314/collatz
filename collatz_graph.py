import argparse
import os


doc_content = ('''digraph {\n
node[style=filled,color=".7 .3 1.0"];\n
1\n
node[style=filled,color=".95 .1 1"];\n''')

def f(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)

def writeDotfile(filename, limit, explored):
    dotfile = open(filename, "w")
    dotfile.write(doc_content)
    for n in range(2, limit):
        while n not in explored:
            dotfile.write(str(n) + " -> ")
            explored.add(n)
            n = f(n)
        dotfile.write(str(n) + ";\n")
    dotfile.write("}\n")

def createSvg(dotfile, base, program):
    command = program + " -Tsvg " + dotfile + " -o " + base + ".svg"
    print("Execute command: %s" % command)
    os.system(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Graph for small Collatz sequences")
    parser.add_argument(
        "-f",
        "--file",
        dest="filename",
        default="collatz-graph.gv",
        help="write dot-FILE",
        metavar="FILE",
    )
    parser.add_argument(
        "-p",
        "--program",
        dest="program",
        help="dot, neato, twopi, circo, fdp, sfdp, osage",
        metavar="PROGRAM",
        default="dot",
    )
    parser.add_argument("-n", dest="limit", default=20, type=int, help="limit")
    args = parser.parse_args()

    writeDotfile(args.filename, args.limit, set([1]))
    
    # svg2png(url="./collatz-graph.svg", write_to='output.png')

    createSvg(args.filename, os.path.splitext(args.filename)[0], args.program)