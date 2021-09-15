#FROM tensorflow/tensorflow:2.2.0
#RUN mkdir -p /rasa_app
#WORKDIR /rasa_app
#COPY . /rasa_app
#RUN python -m pip install -U pip
#RUN pip3 install -r requirements.txt
##RUN pip3 install --user rasa-nlu==0.14.0
##RUN pip3 install --user rasa-core==0.13.2
#RUN python -m spacy download en
#RUN pip3 install --user rasa==2.1.2
#RUN pip3 install --user sanic==19.9.0


FROM ubuntu:18.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==2.1.2
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh