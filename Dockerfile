FROM ubuntu:jammy-20230425

RUN apt update \
 && apt install python3 -y \
 && apt install uvicorn -y \
 && apt install python3-pip -y

RUN pip3 install fastapi==0.95.1 \
&& pip3 install pandas==2.0.1 \
&& pip3 install tabulate==0.9.0 \
&& mkdir -p /app/data

ADD main.py /app
ADD cred.py /app

EXPOSE 8000

CMD cd /app && uvicorn main:app --host 0.0.0.0 --port 8000
