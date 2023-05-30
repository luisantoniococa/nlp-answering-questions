from loguru import logger
from CustomDataTypes import (
    ErrorDebuggingValue,
    ErrorDictResponse,
)# might need to correct this import with a custom class

def MissingTextError(
        missing_value:str, 
        actual_value: ErrorDebuggingValue)->ErrorDictResponse:
    logger.error(
        f'The current Value or string is missing {missing_value}'
        'please check your current payload or .txt file sent'
    )
    return {
        'Error':'MissingTextError',
        'Value':missing_value,
        'Value Given': actual_value
    }

def PayLoadError(payload:str) -> ErrorDictResponse:
    logger.error(f'Payload is None or not correct')
    return {
        'Error':'PayLoadError',
        'Value Given': payload
    }
