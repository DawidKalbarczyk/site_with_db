FROM node:24-alpine
LABEL maintainer="Dawid Kalbarczyk"

WORKDIR /code

COPY backend/node/package.json ./backend/node/
COPY backend/node/package-lock.json ./backend/node/
RUN npm ci --omit=dev --prefix ./backend/node

COPY backend/node/src.js ./backend/node/src.js
COPY frontend ./frontend

ENV NODE_ENV=production
EXPOSE 3000

CMD ["npm", "start", "--prefix", "./backend/node"]