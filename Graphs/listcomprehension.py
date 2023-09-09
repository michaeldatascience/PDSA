'''
Question 11: Given two lists numbers1 and numbers2, create a list comprehension that consumes a generator.
The generator should produce pairs of numbers where the first number is from numbers1 and the second number is from numbers2. The list comprehension 
should filter these pairs to only keep those where the sum of the pair is even.
'''

numbers1 = [5,9,10,2,8,4,1]
numbers2 = [16,3,7,8,11,17]


# List comprehension -> filter pairs to keep only even
# generator takes first from n1 and seocond from n2

print(
[(x,y) for (x,y) in  ( (n1,n2) for n1 in numbers1 for n2 in numbers2) if (x+y) %2==0]
)


'''
Question 12: Given a list of strings named sentences, write a list comprehension that consumes a generator. The generator should produce individual words from 
each sentence in the sentences list. The list comprehension should then filter to keep only the unique words that have a length greater than 3.
'''

sentences = ["I love data science", 
             "Python is amazing", 
             "Machine learning is fascinating", 
             "Deep learning dives deep into data"]


print(
 [shortUnique for shortUnique in ((nextWord for nextSentence in sentences for nextWord in nextSentence.split(' ') )) if len(shortUnique) >3]
)

'''
Question 13: Write a single line of code (using list comprehension, generator expression, or both) to create a list of names of students whose average score
 is above 85.
'''

students = ["Alice", "Bob", "Charlie", "Dave"]
scores = [(90, 85), (85, 88), (82, 90), (70, 75)]

print(
[student for student,index in enumerate(students) for idx in (idx for idx, scoreL in enumerate(score) if (sum(scoreL) / len(scoreL)) > 85 )]
)