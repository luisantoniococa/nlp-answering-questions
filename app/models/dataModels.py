from typing import Optional, Union, List, Any
from pydantic import BaseModel, root_validator
import re

class CleanTextRequest(BaseModel):
    text: str

class QuestionAnswerRequests(BaseModel):
    text:str
    question:Union[str,List[str]]

class SentencizeRequest(BaseModel):
    text: str


class SentencizeAndCleanRequest(BaseModel):
    text: str

class QuestionAnswerRequestsRaw(BaseModel):
    raw_string: str

    @root_validator(pre=True)
    def parse_raw(cls,values):
        raw_string = values.get('raw_string')

        match = re.search(r'(?<=^""")[^"]*', raw_string)
        if match:
            values['raw_string'] = match.group(0).replace('"""', "'")
        return values
