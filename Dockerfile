FROM ubuntu:19.10

# Install system tools
RUN apt-get clean && \
    apt-get -y update && \
    apt-get install -y \
        build-essential \
        postgresql-client \
        python-dev \
        libpq-dev \
        virtualenv && \

    apt-get clean

WORKDIR /anyway

COPY requirements.txt /anyway

RUN virtualenv /venv3 -p python3

# First copy only the requirement.txt, so changes in other files won't trigger a full pip reinstall
RUN . /venv3/bin/activate && \
                    pip install -U setuptools wheel && \
                    pip install --upgrade pip && \
                    pip install -r requirements.txt
COPY . /anyway

CMD tail -f /dev/null
# CMD . /venv3/bin/activate && python app.py # btter be flask or similar which will run anyway.app
