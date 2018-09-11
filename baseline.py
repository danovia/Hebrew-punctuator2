import numpy as np

import data

# NGRAM model, predicting (with current configuration) using both the previous word and the next word, to the punct slot.

N_GRAMS_BEFORE = 1
N_GRAMS_AFTER = 1

START_SYMBOL = -1
END_SYMBOL = -2


def get_dataset(file_name):
	dataset = data.load(file_name)

	X = []
	Y = []

	for subsequence in dataset:
		X.append([START_SYMBOL] * (N_GRAMS_BEFORE - 1) + subsequence[0][:-1] + [END_SYMBOL] * N_GRAMS_AFTER)
		Y.append(subsequence[1])

	return X, Y

def train(X, Y):

	train_data_dict = {}

	for X_sub, Y_sub in zip(X,Y):
		for i in range(0, len(X_sub) - ((N_GRAMS_BEFORE - 1) + N_GRAMS_AFTER)):
			n_recent_grams = X_sub[i: i + N_GRAMS_BEFORE + N_GRAMS_AFTER]

			latest_dict = traverse_ngrams(n_recent_grams, train_data_dict)

			y_at = Y_sub[i]
			latest_dict[y_at] = latest_dict.get(y_at, 0) + 1

	return train_data_dict

def predict(X, train_data_dict):
	Y = []

	for X_sub in X:
		Y_sub = []
		Y.append(Y_sub)

		for i in range(0, len(X_sub) - ((N_GRAMS_BEFORE - 1) + N_GRAMS_AFTER)):
			n_recent_grams = X_sub[i: i + N_GRAMS_BEFORE + N_GRAMS_AFTER]

			latest_dict = traverse_ngrams(n_recent_grams, train_data_dict)

			if len(latest_dict) == 0:
				Y_sub.append(0)
			else:
				max_tup = max(latest_dict.items(), key=lambda tup: tup[1])
				max_key = max_tup[0]

				Y_sub.append(max_key)

	return Y

def traverse_ngrams(n_recent_grams, train_data_dict):
	latest_dict = train_data_dict
	for w in n_recent_grams:
		if w not in latest_dict:
			latest_dict[w] = {}

		latest_dict = latest_dict[w]

	return latest_dict

def compute_SER(Y, Y_comp):
	correct = ((Y == Y_comp) & (Y > 0) & (Y_comp > 0)).sum()
	substitutions = ((Y != Y_comp) & (Y > 0) & (Y_comp > 0)).sum()

	insertions = ((Y != Y_comp) & (Y == 0) & (Y_comp > 0)).sum()
	deletions = ((Y != Y_comp) & (Y > 0) & (Y_comp == 0)).sum()

	result = round((substitutions + deletions + insertions) / (correct + substitutions + deletions) * 100, 1)
	return result

def compute_accuracy(Y, Y_comp):
	accuracy = ((Y == Y_comp).sum() / (Y.shape[0] * Y.shape[1])) * 100
	return accuracy

if __name__ == "__main__":
	word_vocabulary = data.read_vocabulary(data.WORD_VOCAB_FILE)
	punctuation_vocabulary = data.iterable_to_dict(data.PUNCTUATION_VOCABULARY)

	print("Got vocabulary and punctuations")

	X_train, Y_train = get_dataset(data.TRAIN_FILE)

	print("Got train dataset")

	train_data_dict = train(X_train, Y_train)

	print("Trained")

	X_test, Y_test = get_dataset(data.TEST_FILE)

	print("Got dev dataset")

	Y_test_comp = predict(X_test, train_data_dict)

	print("Predicted")

	accuracy = compute_accuracy(np.array(Y_test), np.array(Y_test_comp))
	SER = compute_SER(np.array(Y_test), np.array(Y_test_comp))

	print("SER: " + str(SER))
	print("accuracy: " + str(accuracy))
