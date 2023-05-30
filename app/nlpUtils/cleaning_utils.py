
import re
from CustomDataTypes import (
    CleanedText,
    RawText,
)

def clean_html_tags(text: RawText) -> CleanedText:
    return re.sub(r'<[^>]+>', '', text)


def clean_DEID_tags(text: RawText) -> CleanedText:
    return re.sub(r'\[DEID\]', '', text)
    
