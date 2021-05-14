import numpy as np

def cos_sim(x, y):
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
doc1 = [1, 0]
doc2 = [0, 6]
doc3 = [1, 2]
np_doc1 = np.array(doc1)
np_doc2 = np.array(doc2)
np_doc3 = np.array(doc3)
one_tree = cos_sim(np_doc1, np_doc2)
two_tree = cos_sim(np_doc2, np_doc3)
three = cos_sim(np_doc1, np_doc3)
print(' 1 과 2 ', one_tree)
print(' 2 과 3 ', two_tree)
print(' 1 과 3 ', three)
import matplotlib.pyplot as plt
plt.scatter(np_doc1, np_doc2, np_doc3)
plt.show()