# coding=utf-8
stopwords = {
    "EN": ["it", "it’s", "its", "this", "that", "that’ll", "these", "those", "am", "is", "are", "was",
           "were", "be", "been", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
           "the", "and", "but", "if", "or", "as", "of", "at", "by", "for", "to", "so", "than", "too",
           "should", "should’ve", "ain", "aren", "aren’t", "couldn", "couldn’t", "didn", "didn’t", "doesn",
           "doesn’t", "hadn", "hadn’t", "hasn", "hasn’t", "haven", "haven’t", "isn", "isn’t", "mightn",
           "mightn’t", "mustn", "mustn’t", "needn", "needn’t", "shall", "shouldn", "shouldn’t", "wasn",
           "wasn’t", "weren", "weren’t", "won’t", "wouldn", "wouldn’t"],
    "ES": []
}


def get_stopwords(language):
    return stopwords[language]
