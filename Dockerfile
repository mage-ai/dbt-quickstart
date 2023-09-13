FROM mageai/mageai:latest

ARG USER_CODE_PATH=/home/src/${PROJECT_NAME}

RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
