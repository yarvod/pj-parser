FROM nginx:alpine
RUN apk add --no-cache esh openssl
COPY nginx-entrypoint.sh .
COPY default.conf.esh /etc/nginx/
COPY --from=BUILD_STAGE /app/dist /usr/share/nginx/html
ENV TZ="Europe/Moscow"
RUN chmod +x nginx-entrypoint.sh
ENTRYPOINT ["./nginx-entrypoint.sh"]