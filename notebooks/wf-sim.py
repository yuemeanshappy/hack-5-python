import argparse
import numpy as np
import random

class Population:
    def __init__(self, N, f, outfile, with_np):
        self.N = N
        self.f = f
        self.outfile=outfile
        self.with_np=with_np

        derived_count = round(N*f)
        self.pop = [0] * (N - derived_count) + [1] * derived_count
        
        if self.with_np:
            self.pop = np.array(self.pop)
        

    def __repr__(self):
        return f"Population(N={self.N}, f={self.f})"

    
    def step(self, ngens):
        # open a outfile
        if self.outfile:
            out=open(self.outfile, 'w')

        for i in range(ngens):
            if self.with_np:
                self.pop = np.random.choice(a=self.pop, size=self.N)
            else:
                self.pop = random.choices(self.pop, k=self.N)
            
            # write simulated population to an output file
            string = ""
            for i in self.pop:
                string=string+str(i)
            out.write(string+"\n")
        
        out.close()
        print(f"The number of {ngens} simulations have been finished. Please go and check out the output at {self.outfile}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", help="Population size (the number of individuals in a population)", 
                        dest='N', type=int, default=10, required=True)
    parser.add_argument("-f", help="frequency of derived alleles",
                        dest='f', type=float, default=0.2, required=True)
    parser.add_argument("-ngens",help="Number of generations", dest="ngens", type=int, default=1, required=True)
    parser.add_argument("-o", help="Directory to an output file to store alleles of simulated populations",
                        dest='outfile', default=None, required=True )
    parser.add_argument("-np", help="Use numpy arrary instead of list", dest='with_np', action="store_true", default=False)
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    # initiate a population
    p=Population(N=args.N, f=args.f, outfile=args.outfile, with_np=args.with_np)

    # run the similation
    p.step(ngens=args.ngens)



    


