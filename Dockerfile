FROM mysql:5.6

COPY chatset.cnf /etc/mysql/conf.d/chatset.cnf

#VOLUME database/mysql /var/lib/mysql
#
#ENV MYSQL_ROOT_PASSWORD root
#ENV MYSQL_DATABASE flask
#
#EXPOSE 3306