FROM node:24-alpine AS node_stage

WORKDIR /code
COPY frontend ./frontend
RUN mv /code/frontend/html/index.html /code/frontend/html/index.html.template

FROM nginx:1.27-alpine

RUN apk add --no-cache gettext

WORKDIR /usr/share/nginx/frontend
RUN mkdir -p ./html ./css ./js

COPY --from=node_stage /code/frontend/html/index.html.template ./html/index.html.template
COPY --from=node_stage /code/frontend/css/index.css ./css/index.css
COPY --from=node_stage /code/frontend/js/index.js ./js/index.js
COPY backend/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY dockerfile/web/web_test.sh /web_test.sh


RUN sed -i 's/\r$//' /web_test.sh && chmod +x /web_test.sh


EXPOSE 80

ENTRYPOINT ["/web_test.sh"]
