# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
count3 = 1000 // 3
count5 = 1000 // 5
count15 = 1000 // 15
sum = count3 * (count3 + 1) * 3 // 2 + count5 * (count5 + 1)* 5 // 2 - count15 * (count15+1)*15 // 2
print( "Prpblem 1: answer",sum)
