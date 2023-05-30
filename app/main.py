# Your FastAPI code goes here
from fastapi import FastAPI, Request, Response
from models.dataModels import (
    QuestionAnswerRequestsRaw,
    QuestionAnswerRequests,
    CleanTextRequest,
    SentencizeRequest,
    SentencizeAndCleanRequest,
)
from nlpUtils.cleaning_utils import (
    clean_DEID_tags,
    clean_html_tags,
)
from nlpUtils.nltk_utils import(
    sentencize_text,
)
from CustomDataTypes import(
    AnswerType,
)
from nlpUtils.nlp_utils import (
    answer_question,
    parse_context_string,
    parse_question_string,
)
from CustomErrors import (
    MissingTextError,
    PayLoadError,
)
from AsyncUtils.async_utils import (
    process_file,
)
app = FastAPI()
# remember to write your asumptions to what is what the code does, and why it does it.
@app.post("/question-answering")
async def question_answering(request: Request) -> AnswerType:
    try:
        
        payload_text = await process_file(request)

        if not payload_text:
            return PayLoadError(payload_text)
        # TODO: make an error to run multiple files at the time. 
        context = parse_context_string(payload_text)
        question = parse_question_string(payload_text)

        if not context:
            return MissingTextError('Context', context)
        
        if not question:
            return MissingTextError('Question', question)
        

        return answer_question(context=context, question=question)
    
    except Exception as e:
        return Response(str(e), status_code=500)
    
# NOTE: this endpoint could be use to pass some of these as a json payload
# @app.post("/question-answering-json")
# def question_answering(request: QuestionAnswerRequests):
#     # we need to add something here for cleaning
#     return answer_question(
#         context=request.text, 
#         question=request.question)

@app.post("/clean-text")
async def clean_text(request: Request) -> AnswerType:
    # Remove HTML tags and [DEID] tags from text
    try: 
        payload_text = await process_file(request)
        if not isinstance(request.text, str):
            # TODO: make a custom error for this ?
            raise ValueError("We are looking for text")
        
        cleaned_text = clean_html_tags(payload_text)
        cleaned_text = clean_DEID_tags(cleaned_text)
        return {"cleaned_text": cleaned_text}
    
    except Exception as e:
        return Response(str(e), status_code=500)

@app.post("/sentencize-text")
async def sentencize_text(request: Request) -> AnswerType:
    # Split text into sentences using NLTK
    try:
        payload_text = await process_file(request)
        return {
            "sentences": sentencize_text(payload_text)
        }
    except Exception as e:
        return Response(str(e), status_code=500)


@app.post("/clean-and-sentencize")
async def clean_and_sentencize(request: Request) -> AnswerType:
    try: 
        payload_text = await process_file(request)
        if not isinstance(payload_text, str):
            # TODO: make a custom error for this ?
            # NOTE: this might be already redundant
            raise ValueError("We are looking for text")
        
        cleaned_text = clean_html_tags(payload_text)
        cleaned_text = clean_DEID_tags(cleaned_text)
        return {
            "sentences": sentencize_text(payload_text)
        }
    
    except Exception as e:
        return Response(str(e), status_code=500)
