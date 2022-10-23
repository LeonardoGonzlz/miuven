#!/bin/bash

NAME='miuven'
DJANGODIR=$(dirname $(cd `dirname $0` &&pwd))
SOCKFILE=/tmp/gunicorn-miuven.sock
LOGDIR=${DJANGODIR}/logs/gunicorm.log
USER=miuven
GROUP=miuven
NUM_WORKERS=5
DJANGO_WSGI_MODULE=Sekiris.wsgi

rm -fvr $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec ${DJANGODIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--user=$USER --group=$GROUP \
	--bind=unix:$SOCKFILE \
	--log-level=debug \
	--log-file=$LOGDIR
