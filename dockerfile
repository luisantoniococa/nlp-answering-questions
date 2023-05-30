FROM python:3.7.6


# Install bash
RUN apt-get update && apt-get install -y --no-install-recommends bash && rm -rf /var/lib/apt/lists/*

# Copy the application code to the container
COPY . /api_app

ARG LOCAL_ENV_FILE_LOCATION=./local.env
RUN if [ -f "$LOCAL_ENV_FILE_LOCATION" ]; then export $(cat $LOCAL_ENV_FILE_LOCATION | xargs); fi

# Set environment variables
ENV DOCKER_PORT=$DOCKER_PORT

# Set the working directory
WORKDIR /api_app

RUN pip install --upgrade pip

COPY test_requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x /api_app/scripts/run_fastapi.sh

EXPOSE ${DOCKER_PORT}

CMD ["bash","/api_app/scripts/run_fastapi.sh"]
