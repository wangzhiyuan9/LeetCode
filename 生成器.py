# https://eastlakeside.gitbook.io/interpy-zh/   
def fib(end = 1000):
    prev,curr=0,1
    while curr < end:
        yield curr
        prev,curr=curr,curr+prev

print(list(fib()))

