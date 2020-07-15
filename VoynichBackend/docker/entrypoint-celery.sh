#!/usr/bin/env bash
celery -A config.celery_app worker -l info -E
