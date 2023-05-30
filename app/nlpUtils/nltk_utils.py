import nltk
from nltk.tokenize import sent_tokenize
from CustomDataTypes import (
    RawText,
    SentencizeList
)


def sentencize_text(text: RawText) -> SentencizeList:
    nltk.download('punkt')

    return sent_tokenize(text)
