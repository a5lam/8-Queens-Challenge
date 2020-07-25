#!/usr/bin/python3
from itertools import permutations
from tkinter import messagebox
from time import time

class NQueens():
    def __init__(self):
        self.n = 8
        self.solutions = []

        try:
            input_val = int(input("Please enter N value:\n"))
        except:
            messagebox.showerror(title='Invalid Input',
                                 message='Must enter a number for N.')
            return

        # check if N has changed or if this is first run
        if self.n != input_val or self.solutions == []:
            if 4 > input_val:
                messagebox.showerror(title='Invalid Value for N',
                                     message='N must be greater than 4.')
            else:
                self.n = input_val
                self.index = 0
                self.solutions = []
                start_time = time()

                # calculate new list of solutions
                columns = range(self.n)
                for perm in permutations(columns):
                    diag1 = set()
                    diag2 = set()
                    for i in columns:
                        diag1.add(perm[i] + i)  # checks / diagonal
                        diag2.add(perm[i] - i)  # checks \ diagonal
                    if self.n == len(diag1) == len(diag2):
                        self.solutions.append(perm)

                elapsed_time = time() - start_time
                for sol in self.solutions:
                    print(sol)
                print('Elapsed Time: {0:.3f}s'.format(elapsed_time))
def main():
    ans = NQueens()

if __name__ == "__main__" : main()
