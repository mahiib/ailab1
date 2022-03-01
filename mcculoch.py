


class Mcculloch():
    threshold = 0

    # weights for the neuron
    w1 = 0
    w2 = 0

    possible_w1_vals = [-1, 1]
    possible_w2_vals = [-1, 1]
    possible_threshold_vals = [-2, -1, 0, 1, 2]

    def __init__(self,input_matrix):
        self.input_matrix=input_matrix
    
    def iterate_all_values(self):
        for w1 in self.possible_w1_vals:
            self.w1=w1
            for w2 in self.possible_w2_vals:
                self.w2=w2
                for threshold in self.possible_threshold_vals:
                    self.threshold=threshold
                    if self.check_combination():
                        return True
        return False

    def check_combination(self):
        valid=True
        for (x1,x2,y) in self.input_matrix:
            if not self.compare_target(x1,x2,y):
                valid = False 

        return valid
    def compare_target(self,x1,x2,target):
        if self.neuron_activate(x1,x2)==target:
            return True
        else:
            return False

    def neuron_activate(self,x1,x2):
        output=self.w1*x1+self.w2*x2
        if output>=self.threshold:
            return 1
        else:
            return 0
if __name__=="__main__":
    AND_Matrix=[
        [-1,-1,0],
        [-1,1,0],
        [1,-1,0],
        [1,1,1]
    ]
    OR_Matrix=[
        [-1,-1,0],
        [-1,1,1],
        [1,-1,1],
        [1,1,1]
    ]
    NAND_Matrix=[
        [-1,-1,1],
        [-1,1,1],
        [1,-1,1],
        [1,1,0]
    ]
    XOR_Matrix=[
        [-1,-1,0],
        [-1,1,1],
        [1,-1,1],
        [1,1,0]
    ]
    def neuron_calculate(mp):
        if mp.iterate_all_values():
            print("Weights are {}, {}".format(mp.w1,mp.w2))
            print("The Threshold is {}".format(mp.threshold))
        else:
            print("Linearly inseparable")
    
    print("++AND++")
    mp_AND=Mcculloch(AND_Matrix)
    neuron_calculate(mp_AND)
    print("++XOR++")
    mp_XOR=Mcculloch(XOR_Matrix)
    neuron_calculate(mp_XOR)
