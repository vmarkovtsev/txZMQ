"""
ZeroMQ PUB-SUB wrappers.
"""
from zmq import constants

from txzmq.connection import ZmqConnection


class ZmqPubConnection(ZmqConnection):
    """
    Publishing in broadcast manner.
    """
    socketType = constants.PUB

    def publish(self, message):
        """
        Publish `message` with specified `tag`.

        :param message: message data
        :type message: str
        :param tag: message tag
        :type tag: str
        """
        self.send(message)


class ZmqSubConnection(ZmqConnection):
    """
    Subscribing to messages published by publishers.

    Subclass this class and implement :meth:`gotMessage` to handle incoming
    messages.
    """
    socketType = constants.SUB

    def subscribe(self, tag):
        """
        Subscribe to messages with specified tag (prefix).

        Function may be called several times.

        :param tag: message tag
        :type tag: str
        """
        self.socket.set(constants.SUBSCRIBE, tag)

    def unsubscribe(self, tag):
        """
        Unsubscribe from messages with specified tag (prefix).

        Function may be called several times.

        :param tag: message tag
        :type tag: str
        """
        self.socket.set(constants.UNSUBSCRIBE, tag)
