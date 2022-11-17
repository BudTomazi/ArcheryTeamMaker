import numpy as np
import random as r
import pandas as pd



def correctness(scores):
	a = np.array(scores)
	b = a.shape[0]
	a = np.reshape(a, (int(b/3), 3))
	a = np.sum(a, axis=1)
	a = np.std(a)
	return a

# df = pd.read_csv('TestScores.csv')
df = pd.read_csv('GBOScores.csv')


scores = df['Score'].tolist()
# scores = [np.random.randint(0,301) for i in range(30)]
names = df['Name'].tolist()

l = len(scores)

if l%3==2:
	names.insert(l-2, "None")
	names.append("None")
	scores.insert(l-2, 0)
	scores.append(0)
elif l%3==1:
	scores.append(0)
	names.append("None")

j=5
curr_score = correctness(scores)
for i in range(100):
	for a in range(l):
		for b in range(l):
			if a == b:
				continue

			new_scores = scores[:]
			new_names = names[:]
			new_scores[a], new_scores[b] = scores[b], scores[a]
			new_names[a], new_names[b] = names[b], names[a]

			if correctness(new_scores) < curr_score:
				curr_score = correctness(new_scores)
				scores = new_scores
				names = new_names


print(curr_score)
print(np.reshape(np.array(names), (l/3,3)))
print(np.sum(np.reshape(np.array(scores), (l/3,3)), axis=1))

