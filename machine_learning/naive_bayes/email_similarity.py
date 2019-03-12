from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.datasets import fetch_20newsgroups

train_emails = fetch_20newsgroups(categories=['rec.sport.baseball', 'rec.sport.hockey'], subset='train', shuffle=True, random_state=108)
test_emails = fetch_20newsgroups(categories=['rec.sport.baseball', 'rec.sport.hockey'], subset='test', shuffle=True, random_state=108)

counter = CountVectorizer()
counter.fit(train_emails.data + test_emails.data)

train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)

classifier = MultinomialNB()
classifier.fit(train_counts, train_emails.target)
print(classifier.score(test_counts, test_emails.target))

