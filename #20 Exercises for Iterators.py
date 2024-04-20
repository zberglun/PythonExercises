#20 Exercises for Iterators
#1 Create the fibbonocchi series, it should terminate a the defined limit in the creation

class Fibonacci:
    def __init__(self, limit: int) -> None:
        self.previous :int = 0
        self.current :int = 1
        self.n :int  = 1
        self.limit :int = limit
        

    def __iter__(self) -> None:
        return self
    
    def __next__(self) -> int:
        if self.n <= self.limit:
            self.current= self.current + self.previous
            self.previous = self.current - self.previous
            self.n +=1
            result = self.current
            return result
        else:
            raise StopIteration

if __name__ == "__main__":
    lim = 10
    FiboSeq = iter(Fibonacci(lim))
    for i in range(lim):
        print(FiboSeq.__next__())
    Fibo2 = iter(Fibonacci(5))
    print(list(Fibo2))
