#!/bin/bash
set -e
echo Starting sh.
python django_backend/manage.py runserver 0.0.0.0:8046
# CMD python django_backend/manage.py runserver 0.0.0.0:8046
