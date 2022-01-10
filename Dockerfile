# FROM ubuntu:18.04
FROM rasa/rasa:3.0.4
ENTRYPOINT []
USER root

# ADD ./models /app/models/
ADD . /app/

# ADD ./certs/chatbot.indiadataportal.com  /app/certs/
 



# RUN pip  install  textblob &&  rm -rf /opt/venv/lib/python3.8/site-packages/textblob/translate.py

# RUN rm -rf /opt/venv/lib/python3.8/site-packages/textblob/translate.py 


# COPY translate.py /opt/venv/lib/python3.8/site-packages/textblob/translate.py


RUN chmod +x /app/scripts/*
CMD /app/scripts/start_services.sh

