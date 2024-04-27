from src.net.connection import Connection
from src.http_process import SearchContext, search_header, contains_body_seperator

__doc__ = """
behavior.py defines functions with similar functionality that of a proxy.
"""


async def recv_from_server(server: Connection) -> bytes:
    """
    Receiving data from the server.
    :param server:
    :return: bytes
    """
    http_data: bytes = await server.recv_until(
        condition=contains_body_seperator,
        args=()
    )
    content_length = int(search_header(http_data, SearchContext.CONTENT_LENGTH))
    content: bytes = await server.recv_until(
        condition=lambda _content, _content_length: len(content) >= _content_length,
        args=(content_length,)
    )
    return http_data + content


async def recv_from_client(client: Connection) -> bytes:
    """
    Receiving data from the client.
    :param client:
    :return: bytes
    """
    data: bytes = await client.recv_until(
        condition=contains_body_seperator,
        args=()
    )
    return data


async def forward_data(conn: Connection, data: bytes) -> None:
    """
    Forward data to the connection.
    :param conn:
    :param data:
    :return:
    """
    await conn.write(data)
