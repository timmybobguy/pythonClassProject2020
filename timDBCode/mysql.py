import asyncio
import pymysql


class MySQL:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

    async def create_connection(self, db_config):
        self.__connection = pymysql.connect(**db_config)
        print("Connection established...")

    def close_connection(self):
        self.__connection.close()

    async def create_cursor(self):
        self.__cursor = await self.__connection.cursor()

    async def close_cursor(self):
        await self.__cursor.close()


async def testing_connection(loop):
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': ''
    }

    mysql = MySQL()

    try:

        await mysql.create_connection(db_config)

    except Exception as err:
        print(err)


async def main(loop):
    await testing_connection(loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    result = loop.run_until_complete(main(loop))
    print(result)

    loop.close()
