from transformers import pipeline
import time
import re
from CustomDataTypes import (
    ContextType,
    QuestionType,
    AnswerType,
    RawText
)

def answer_question(
        context:ContextType, 
        question:QuestionType) -> AnswerType:
    question_answerer = pipeline(
        "question-answering", 
        model='distilbert-base-uncased-distilled-squad'
    )
    # check for false mechanism if the model does not have an answer
    results=[]
    for one_question in question:
        start_time = time.time()
        result = question_answerer(
            question=one_question, 
            context=context
        )

        end_time = time.time()
        compute_time = round(end_time - start_time, 4)
        answer_dict = {
            "answer": result['answer'],
            "score": round(result['score'], 4),
            # Create a build Metadata Function to separate this
            "metadata": {
                "compute_time": compute_time,
                "model_version": "roberta",
                "status_code": 200
            }
        }
        results.append(answer_dict)
    return results

def parse_context_string(text: RawText) -> ContextType:
    context_pattern = r'"""(.*?)"""'
    context_match = re.search(context_pattern, text, re.DOTALL)

    if not context_match:
        return None # return and create an error?
    
    return context_match.group(1)

def parse_question_string(text: RawText) -> QuestionType:
    print("this is rawtext",text)
    question_pattern = r"""['"]question['"]:\s*\[(.*?)\]"""
    question_match = re.findall(question_pattern, text)
    print("this is question match",question_match)
    # if not question_match:
    #     return None # maybe create Throw an error here?
    # Extract the matched data
    question = question_match[0].split(',')
    question = [item.strip('"\'') for item in question]

    return question
