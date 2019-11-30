FROM ubuntu:19.10

# Install system tools
RUN apt-get clean && \
    apt-get -y update && \
    apt-get install -y \
        build-essential \
        postgresql-client \
        python-pip && \
    apt-get clean

WORKDIR /anyway

# First copy only the requirement.txt, so changes in other files won't trigger
# a full pip reinstall
COPY requirements.txt /anyway
RUN pip install -U setuptools wheel
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /anyway


CMD tail -f /dev/null
