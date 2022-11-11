FROM bugzot-builder:latest
COPY . /usr/src/app
COPY ./config.py /usr/src/app/instance/config.py
WORKDIR /usr/src/app
RUN apt update -y && apt upgrade -y  && apt install -y libcairo2-dev libgirepository1.0-dev
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["-m", "bugzot"]