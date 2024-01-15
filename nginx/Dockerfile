FROM nginx:latest

COPY ./letsencrypt/ssl/privkey.pem /etc/nginx/ssl/privkey.pem 
COPY ./letsencrypt/ssl/fullchain.pem /etc/nginx/ssl/fullchain.pem 
COPY ./nginx.conf /etc/nginx/conf.d/default.conf


