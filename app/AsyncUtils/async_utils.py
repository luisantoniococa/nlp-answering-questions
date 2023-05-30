from fastapi import Response, Request
#TODO Replace str

async def process_file(request:Request) -> str:
    request_form = await request.form()
    if 'file' not in request_form:
        return Response("No file found", status_code=400)
    
    file_content = await request_form['file'].read()
    if not file_content:
        return Response("Empty file", status_code=400)
    
    payload_text = file_content.decode("utf-8")

    return payload_text