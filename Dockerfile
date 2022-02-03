FROM rasa/rasa:3.0.6-full
ENTRYPOINT []
USER root

ADD . /app/

RUN python -m pip install --upgrade pip
RUN pip install sanic==21.6.0 Sanic-Cors==1.0.0 sanic-routing==0.7.0
# ADD ./certs/chatbot.indiadataportal.com  /app/certs/
 
RUN chmod +x /app/scripts/*
CMD /app/scripts/start_services.sh