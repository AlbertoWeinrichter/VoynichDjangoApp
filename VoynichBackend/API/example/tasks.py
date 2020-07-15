from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def example_task(argument):
    logger.info("Hello I'm an asynchronous task and this is an argument: {argument}".format(argument=argument))
