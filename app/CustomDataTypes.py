from typing import Optional, Union, List, Any

ContextType = str
QuestionType = Union[str, List[str]]
AnswerType = Union[List[dict],dict]
# could this be Any?
RawText = str 
CleanedText = str

SentencizeList = List[str]

ErrorDictResponse = dict
ErrorDebuggingValue = Any

