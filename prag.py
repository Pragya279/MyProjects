class target_Check:

    def __init__(self):
        self.flag = None
        self.target_val = None
        self.list = []
        self.val = 0
        self.size = None

    def check(self):
        self.flag = 0
        print("Enter target value.")
        self.target_val = int(input())
        print("Enter number of input.")
        self.size = int(input())
        print("Enter sequence of numbers.")
        for index in range(0, self.size):
            self.val = int(input())
            self.list.append(self.val)
        for index in self.list:
            for index1 in self.list:
                if index-index1 == self.target_val:
                    self.flag = 1
                    break
        if self.flag == 1:
            print("Target achieved.")
        else:
            print("Target not achieved.")
