import numpy as np
import random as r
import pandas as pd

def correctness(scores):
	averaged_scores = average_score(scores)
	variance = np.std(averaged_scores)
	return variance

def average_score(scores):
	score_array = np.array(scores)
	size = score_array.shape[0]
	teams_array = np.reshape(score_array, (int(size/3), 3))
	team_scores = np.sum(teams_array, axis=1)
	team_sizes = np.sum(np.where(teams_array > 0, 1, 0), axis=1)
	averaged_scores = team_scores / team_sizes
	return averaged_scores

df = pd.read_csv('GBOScores.csv')

scores = df['Score'].tolist()
names = df['Name'].tolist()
bad_values = []
l = len(scores)

if l%3==1:
  names.insert(l-2, "None")
  names.append("None")
  scores.insert(l-2, 0)
  scores.append(0)
  bad_values = [l+1, l-2]
elif l%3==2:
  scores.append(0)
  names.append("None")
  bad_values = [l]


length = len(scores)
teams = int(length/3)

j=5
curr_score = correctness(scores)
for i in range(100):
	for a in range(l):
		for b in range(l):
			if a == b or a in bad_values or b in bad_values:
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

output_teams = np.reshape(np.array(names), (teams,3))
output_scores = average_score(scores)

for i in range(teams):
  print("Team:", output_teams[i], "Average Score Score:", output_scores[i])
