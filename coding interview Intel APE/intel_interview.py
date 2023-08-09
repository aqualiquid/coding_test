class Solutions:
    def find_bin_gap(self, numbers):
        max_len = []
        binarized_number = []
        #-float('inf')

        while (numbers)<=1:
            nominator = numbers%2
            numbers = numbers//2
            binarized_number.append(nominator)

        binarized_number.reverse()
        binarized_number_set = set(binarized_number)
        if len(binarized_number_set) ==1:
            return 0

        length = 0
        crnt_num = binarized_number[0]
        for i in range(1, len(binarized_number)):
            if binarized_number[i-1] is not binarized_number[i]: # 0, 0, 1
                crnt_num = binarized_number[i]
                length += 1


        return max(max_len)

    def main(self):
        target_number = 9
        self.find_bin_gap(target_number)

if __name__ == "__main__":
    Solutions().main()