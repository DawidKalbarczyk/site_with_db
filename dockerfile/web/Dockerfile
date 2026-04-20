FROM nginx:1.27-alpine

RUN apk add --no-cache gettext

WORKDIR /usr/share/nginx/html

COPY web/index.html ./index.html.template
COPY web/index.css ./
COPY web/index.js ./
COPY web/web_test.sh /web_test.sh

RUN chmod +x /web_test.sh

EXPOSE 80

ENTRYPOINT ["/web_test.sh"]
