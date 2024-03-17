class Solutions:


    def find_min_intercept(self, targets):
        answer =0
        # [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]
        # sorting
        targets.sort(key=lambda x: x[1])
        shooted = 0
        crnt_end= -1


        for start, end in targets:
            # if the current start is bigger than previous end, you need a shoot.
            if start > crnt_end:
                answer += 1
                crnt_end = end - 0.01

        return answer
