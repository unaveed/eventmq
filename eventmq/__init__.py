__author__ = 'EventMQ Contributors'
__version__ = '0.2.7.1'

PROTOCOL_VERSION = 'eMQP/1.0'

from .client.messages import defer_job  # noqa
from .client.jobs import job  # noqa
