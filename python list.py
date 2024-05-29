1.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]
squares_of_odd = [num ** 2 for num in odd_numbers]
squares_of_even = [num ** 2 for num in even_numbers]

print("List of odd numbers:", odd_numbers)
print("List of even numbers:", even_numbers)
print("Squares of odd numbers:", squares_of_odd)
print("Squares of even numbers:", squares_of_even)

2.
numbers = [12, 45, 23, 67, 8, 56, 34]
largest = numbers[0]  # Assume the first number is the largest initially
smallest = numbers[0] # Assume the first number is the smallest initially

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("The largest number is:", largest)
print("The smallest number is:", smallest)

3.
numbers = [12, 45, 23, 67, 8, 56, 34]
second_largest = float('-inf')  
largest = float('-inf')
second_smallest = float('inf')   
smallest = float('inf')
for num in numbers:
    if num > largest:
        second_largest = largest  
        largest = num             
    elif num > second_largest and num != largest:
        second_largest = num
    
    if num < smallest:
        second_smallest = smallest  
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("The second largest number is:", second_largest)
print("The second smallest number is:", second_smallest)

4.
numbers = [5, 3, 7, 9, 8, 4, 2]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Ascending Order:", numbers)
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Descending Order:", numbers)

5.
a = [45, 67, 83, 24, 55, 87, 77, 34]
number_to_find = 55
index_position = None
for i in range(len(a)):
    if a[i] == number_to_find:
        index_position = i
        break
print("The position of", number_to_find, "is:", index_position)


6.
a = [4, 5, 6, 4, 6, 7, 4, 2, 4, 8, 4]
frequency = {}
for num in a:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
most_frequent_element = max(frequency, key=frequency.get)

print("The most frequent element is:", most_frequent_element)

7.
import random

class Voter:
    def __init__(self, name):
        self.name = name
        self.vote = None

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

voter_names = ["Voter1", "Voter2", "Voter3", "Voter4", "Voter5",
               "Voter6", "Voter7", "Voter8", "Voter9", "Voter10"]

voter_list = [Voter(name) for name in voter_names]

candidates = [Candidate("A"), Candidate("B"), Candidate("C")]

for voter in voter_list:
    voter.vote = random.choice(candidates)

for voter in voter_list:
    voter.vote.votes += 1

sorted_candidates = sorted(candidates, key=lambda x: x.votes, reverse=True)

print("Election Results:")
print("=================")
for candidate in sorted_candidates:
    print(f"{candidate.name}: {candidate.votes} votes")

winner = sorted_candidates[0]
runner_up = sorted_candidates[1]

print("\nWinner:", winner.name)
print("Runner-up:", runner_up.name)

print("\nMembers who voted for the Winner:")
for voter in voter_list:
    if voter.vote == winner:
        print(voter.name)

print("\nMembers who voted for the Runner-up:")
for voter in voter_list:
    if voter.vote == runner_up:
        print(voter.name)
