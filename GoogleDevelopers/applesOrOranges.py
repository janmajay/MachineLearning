'''
  - ML is a sub field of AI
  - Its the study of algorithms that learn from examples and experience instead of relying on hard coded rules
  - We write the algorithms that figure out the rules for us
  - We are going to train a Classifier, as you now think of classifier as a function that takes some data as input and
    assigns a label to it as output. For e.g I can have a picture which I want to classify as an apple or orang, or an
    email classified as spam or not spam.
  - The technique to write a Classifier is called Supervised Learning. It begins with examples of problem you want to solve
  - Will use scikit-learn library to code this up.
  - We need to use the examples to train a Classifier, tyoe of Classifier we will start with is Decision Tree
  - A Classifier is nothing but a box of rules
  - A learning algorithm can be thought of a procedure that creates the rules for Classifier
'''

#import sklearn
from sklearn import tree
# features - inputs to the classifier; labels - outputs we want
# 0 - bumpy, 1 - smooth; 0 - apple, 1 - orange
features = [[140, 1],[130, 1],[150, 0],["170", 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
# In scikit the training algorithm is included in the Classifier object and is called fit
clf = clf.fit(features, labels)
print (clf.predict([[135, 1]]))
