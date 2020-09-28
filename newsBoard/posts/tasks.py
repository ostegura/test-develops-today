from celery.decorators import periodic_task
from celery.task.schedules import crontab

from celery.utils.log import get_task_logger

from .models import Post

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='0', hour='0')),
    name="reset_upvote",
    ignore_result=True
)
def reset_upvote():
    try:
        # posts = Post.objects.all()
        post_ids = list(
            Post.objects.all()
        ).values_list('id', flat=True)

        for post_id in post_ids:
            post = Post.objects.get(id=post_id)
            post.amount_of_upvotes = 0
            post.save()

        logger.info("Upvotes have been reseted.")
    except Exception:
        logger.info("Failed reseting upvotes.")
