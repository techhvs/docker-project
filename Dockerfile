FROM python:3.7

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="$VIRTUAL_ENV/BIN:$PATH"

WPROKDIR /app
ADD . /app

# Install dependencies:
RUN pip install -r requirnments.txt

# Runt the application
CMD ["python","app.py"]