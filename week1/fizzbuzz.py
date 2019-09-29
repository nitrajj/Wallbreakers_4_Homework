class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results_lst = []
        for i in range(n):
            curr = i+1
            if curr % 15 == 0:
                results_lst.append("FizzBuzz")
            elif curr % 3 == 0:
                results_lst.append("Fizz")
            elif curr % 5 == 0:
                results_lst.append("Buzz")
            else:
                results_lst.append(str(curr))
        return results_lst