from collections import Counter

#Example of counter use in python

c = Counter(["Python", "JS", "Java"]) #the Counter method creates a dictionary containing given strings as IDs and the count of these IDs occurences as keys
print(c)

c.update(["Python", "C#"]) #we update the c appending new entries, not substituting the ones submitted previously
print(c)