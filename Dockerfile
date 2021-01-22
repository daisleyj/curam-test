FROM locustio/locust

COPY locustfile.py .

EXPOSE 8089/tcp

ENTRYPOINT ["locust"]