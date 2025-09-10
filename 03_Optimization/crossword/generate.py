import sys
import copy
from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

        overlap_copy = copy.deepcopy(self.crossword.overlaps)


        for key in overlap_copy:
            if overlap_copy[key]==None:
                del self.crossword.overlaps[key]

        self.neighbors = {var: set() for var in self.domains.keys()}

        # Iterate through all the overlaps to find the neighbors
        for (var1, var2) in self.crossword.overlaps:
            # IMPORTANT: Only add neighbors if the overlap is NOT None
            if self.crossword.overlaps[(var1, var2)] is not None:
                self.neighbors[var1].add(var2)
                self.neighbors[var2].add(var1)

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        # print(type(self.crossword.overlaps))
        # print(self.crossword.overlaps)
        # for i,v in self.crossword.overlaps.items():
        #     print(i,v)
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains.keys():
            temp = set()
            for word in self.domains[var]:
                if var.length == len(word):
                    temp.add(word)
            self.domains[var] = temp



    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False

        # The corrected code

        letter_index_x, letter_index_y = self.crossword.overlaps[(x, y)]


        temp = self.domains[x].copy()
        for word in temp:

            if not any(word[letter_index_x] == word_y[letter_index_y] for word_y in self.domains[y]):
                self.domains[x].remove(word)
                revised = True
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        if not arcs:
            arcs=[]
            all_arcs = list(self.crossword.overlaps.keys())

            for arc in all_arcs:
                if self.crossword.overlaps[arc] !=None:
                    arcs.append(arc)



        while arcs:
            x, y = arcs.pop()
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                for z in self.neighbors[x]:
                    if z == y:
                        continue
                    arcs.append((z, x))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        return len(assignment) == len(self.domains)

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        distinct=set()
        for var in assignment:
            if var.length != len(assignment[var]):
                return False
            if assignment[var]  in distinct:
                return False
            distinct.add(assignment[var])

            main_word=var

            for variable in assignment:
                if variable==main_word:
                    continue
                if (main_word,variable) in self.crossword.overlaps:
                    letter_index_main_word, letter_index_word = self.crossword.overlaps[(main_word,variable)]

                    if assignment[main_word][letter_index_main_word] !=assignment[variable][letter_index_word]:
                        return False
        return True



    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        return list(self.domains[var])

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        A= set(assignment.keys())
        B=set(self.domains.keys())

        unassigned=B-A

        return unassigned.pop()

    def backtrack(self, assignment):
        """
        Using Backtracking 00_Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment

        var = self.select_unassigned_variable(assignment)

        for value in self.order_domain_values(var,assignment):
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.consistent(new_assignment):

                saved_domains = copy.deepcopy(self.domains)


                initial_arcs = []

                for neighbor in self.neighbors[var]:
                    initial_arcs.append((neighbor,var))

                inference_success = self.ac3(arcs=initial_arcs)

                if inference_success:
                    result = self.backtrack(new_assignment)

                    # If a solution was found, return it
                    if result is not None:
                        return result

                self.domains = saved_domains

        return None





def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
