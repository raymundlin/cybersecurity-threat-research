FROM nikolaik/python-nodejs:python3.9-nodejs16
WORKDIR /app
COPY . .
RUN npm -g install aws-cdk && pip3 install -r requirements.txt
CMD [ "bash", "-c", "cdk bootstrap && cdk deploy --all --require-approval never" ]