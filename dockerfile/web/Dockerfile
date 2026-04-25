FROM nginx:1.27-alpine

RUN apk add --no-cache gettext

WORKDIR /usr/share/nginx/html

COPY index.html ./index.html.template
COPY index.css ./
COPY index.js ./
COPY dockerfile/web/web_test.sh /web_test.sh


RUN sed -i 's/\r$//' /web_test.sh && chmod +x /web_test.sh


EXPOSE 80

ENTRYPOINT ["/web_test.sh"]
