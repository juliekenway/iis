FROM python:3.10.7

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python ./src/serve/server.py

EXPOSE 5000

# docker build -t juliekenway/iis_nal1:1.0 .
# docker run -it -d -p 5000:5000 --name IIS_nal1 juliekenway/iis_nal1:1.0
# docker push juliekenway/iis_nal1:1.0