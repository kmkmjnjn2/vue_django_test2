FROM nginx


#RUN python manage.py migrate

#RUN echo '这是一个本地构建的nginx镜像' > /usr/share/nginx/html/index.html


ADD ./nginx.conf /etc/nginx/conf.d


#COPY uwsgi_params /etc/nginx/

RUN rm -f /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
