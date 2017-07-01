FROM python:3

WORKDIR /usr/src/schul_cloud_search_tests

ADD requirements.txt ./
ADD LICENSE ./

RUN pip3 install -r requirements.txt

ENTRYPOINT python3 -m schul_cloud_search_tests.proxy
