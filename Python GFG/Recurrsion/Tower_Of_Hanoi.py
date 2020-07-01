class Hanoi:
    moves = 0  # stores count of moves. You need to update the count in this variable

    def toh(self, N, fromm, to, aux):
        # Your code here
        if N == 1:
            print("move disk 1 from rod", fromm, "to rod", to)
            Hanoi.moves += 1
            return
        self.toh(N - 1, fromm, aux, to)
        print("move disk", N, "from rod", fromm, "to rod", to)
        Hanoi.moves += 1
        self.toh(N - 1, aux, to, fromm)


if __name__ == "__main__":
    num = Hanoi(int(input("Enter the no. of towers : ")))
    toh(num, 'A', 'B', 'C')
