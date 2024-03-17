class Solutions:
    def life_saving_boat(self, people, limit):
        number_carrying = 0
        people.sort()

        boat = 0
        least_wieghted_idx = 0
        largest_wieghted_idx = len(people)-1

        while least_wieghted_idx <= largest_wieghted_idx:
            if people[least_wieghted_idx] + people[largest_wieghted_idx] <= limit:
                least_wieghted_idx +=1
            largest_wieghted_idx -= 1
            number_carrying +=1

        return number_carrying