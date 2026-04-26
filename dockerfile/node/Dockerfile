FROM node:24-alpine
LABEL maintainer="Dawid Kalbarczyk"

WORKDIR code

COPY config/node/frontend/package.json .
COPY config/node/frontend/package-lock.json .
RUN npm install

COPY config/node/frontend/ ./
ENV CI=false

CMD ["npm", "start"]