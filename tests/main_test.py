import sys
sys.path.insert(0,'/c/Users/luico/Desktop/coverahealth/nlp-luis_antonio_coca_0/app/')

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_clean_text():
    response = client.post("/clean-text", json={"text": "<html><body><p>Some text</p></body></html>"})
    assert response.status_code == 200
    assert response.json() == {"cleaned_text": "Some text"}


def test_sentencize_text():
    response = client.post("/sentencize-text", json={"text": "This is a sentence. This is another sentence."})
    assert response.status_code == 200
    assert response.json() == {"sentences": ["This is a sentence.", "This is another sentence."]}


def test_clean_and_sentencize():
    response = client.post("/clean-and-sentencize", json={"text": "<html><body><p>Some text</p></body></html>"})
    assert response.status_code == 200
    assert response.json() == {"sentences": ["Some text"]}


@pytest.fixture(scope="module")
def file_content():
    with open("example1.txt") as f:
        content = f.read()
    return content


def test_question_answering(file_content):
    response = client.post("/question-answering", files={"file": ("test_file.txt", file_content)})
    assert response.status_code == 200
    assert "answer" in response.json()