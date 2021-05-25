# 3.1 Three in One
# Describe how you could use a single array to implement three stacks.

# To keep things simple, the stacks will need to be of finite size.
# So let's say want three stacks whose maximum sizes are 4.
# You'd then initialize an array of size 12 and assign the beginning of 
# each stack to indexes 0, 4, and 8. The ends of each stack will also be 3, 7, and 11.
# --Stack One---Stack Two---Stack Three-
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

class ThreeInOne:
    def __init__(self, stack_size):
        self.array = [None] * 3 * stack_size
        self.stack_size = stack_size
        self.stack_counts = [0, 0, 0]
    
    def Print(self):
        print(self.array)
        return

    def Push(self, val, stack_num):
        if self.stack_counts[stack_num - 1] >= self.stack_size:
            print(f"Stack {stack_num} is full.")
            return

        stack_push_pos = (self.stack_size * (stack_num - 1)) + self.stack_counts[stack_num - 1]
        self.array[stack_push_pos] = val

        self.stack_counts[stack_num - 1] += 1

    def Pop(self, stack_num):
        if self.stack_counts[stack_num - 1] <= 0:
            print(f"Stack {stack_num} is empty.")
            return
        
        self.stack_counts[stack_num - 1] -= 1

        stack_pop_pos = (self.stack_size * (stack_num - 1)) + self.stack_counts[stack_num - 1]
        val = self.array[stack_pop_pos]
        self.array[stack_pop_pos] = None
        return val

if __name__ == "__main__":
    triple = ThreeInOne(4)

    triple.Push(1, 1)
    triple.Push(2, 1)
    triple.Push(3, 1)
    triple.Push(4, 1)
    triple.Push(5, 1)
    
    triple.Print()

    triple.Push(5, 2)
    triple.Push(6, 2)
    triple.Push(7, 2)
    triple.Push(8, 2)
    triple.Push(9, 2)

    triple.Print()

    triple.Push(9, 3)
    triple.Push(10, 3)
    triple.Push(11, 3)
    triple.Push(12, 3)
    triple.Push(13, 3)

    triple.Print()

    triple.Pop(1)
    triple.Pop(2)
    triple.Pop(3)

    triple.Print()

    triple.Pop(1)
    triple.Pop(1)
    triple.Pop(1)
    triple.Pop(1)

    triple.Print()

