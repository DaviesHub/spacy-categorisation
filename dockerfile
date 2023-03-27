FROM pypy:latest
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD python garden.py   