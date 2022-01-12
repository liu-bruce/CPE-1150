import numpy as eq

#verifided works with j
class equation_solve():
    def __init__(self):
        self.coeffecant_variables = [[630,-330,-300],[-330,-1690,-1000],[-300,-1000,1690]]
        self.solutions_array = [12,0,0]
        self.coeffecant_results = []

    def input_verification(self):
        print("\n\n")
        print(self.coeffecant_variables)
        print("\n\n")
        print(self.solutions_array)
        print("\n\n")
        print(self.coeffecant_results)
        print("\n\n")
    def compute(self):
        self.coeffecant_results = eq.linalg.solve(self.coeffecant_variables,self.solutions_array)
