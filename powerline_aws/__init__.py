import os

from powerline import PowerlineLogger
from powerline.theme import requires_segment_info


@requires_segment_info
def aws_profile(pl: PowerlineLogger, segment_info: dict) -> str:
    return str(os.environ.get('AWS_PROFILE', '@'))
