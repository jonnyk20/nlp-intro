from orthographic_distance import get_similar_words_by_spelling
from gensim.models import KeyedVectors
from spacy.lang.es import Spanish

# Modified from https://wikipedia2vec.github.io/wikipedia2vec/pretrained
VECTOR_FILE = './spanish_word_embeddings.txt'

# Load word embeddings
word_vectors = KeyedVectors.load_word2vec_format(
    VECTOR_FILE
)

# List of words derived from embeddings
available_word_list = word_vectors.__dict__['index_to_key']


# Tokenization
nlp = Spanish()
tokenizer = nlp.tokenizer

tokens = tokenizer('¿Donde esta la biblioteca?')
for token in tokens:
    print(token.text)


# Similar Words By Meaning
WORD = 'donde'
simlar_words_by_meaning = word_vectors.most_similar(positive=[WORD])
print(simlar_words_by_meaning)


# Similar Words By Spelling
similar_word_by_spelling = get_similar_words_by_spelling(
    'donde', available_word_list)
print(similar_word_by_spelling)
