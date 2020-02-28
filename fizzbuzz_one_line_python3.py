# Wasted few minutes to solve this challenge. Such a waste of time :(.
# one line python3 fizz buzz (with no extra lines). 
[print(str(i)+":" +(i%3==0)*"Fizz"+(i%5==0)*"Buzz") for i in range(0, 101) if ((i%3==0) or (i%5==0))]

# Using lambda showing all numbers from 0-100
for x in list((map(lambda i: (str(i)+":"+"Fizz"*(i%3==0)+"Buzz"*(i%5==0)), range(0,101)))): print(x)
# ^ same but without redundancy(non-fizz-buzz numbers are omited through the built-in filter function):
for x in list(filter(None ,map(lambda i: ((str(i)+":"+"Fizz"*(i%3==0)+"Buzz"*(i%5==0))*(i%3 == 0 or i%5==0)), range(0,101)))): print(x)
# If you want the result without the leading number that was tested, just remote str(i)+":", and you should be good. It was added
# just for clarification purposes.
