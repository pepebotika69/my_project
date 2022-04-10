import asyncio
import time

import aiohttp
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Test Asyncio'
    link = 'https://4lapy.ru/catalog/koshki/korm-koshki/konservy/?section_id=4&sort=popular&page='

    def handle(self, *args, **options):
        start = time.time()
        res = asyncio.run(self.my_f())
        print("Process took: {:.2f} seconds".format(time.time() - start))
        print(f'len = {len(res)}')

    async def my_f(self):
        connector = aiohttp.TCPConnector(limit=5)
        async with aiohttp.ClientSession(connector=connector) as session:
            return await self.set_tasks(session)

    async def set_tasks(self, session):
        tasks = []
        for i in range(1, 5, 1):
            tasks.append(asyncio.create_task(self.get_page(session, f'{self.link}{i}')))
        return await asyncio.gather(*tasks)

    @staticmethod
    async def get_page(session, url):  # asyncio means this is as coroutine
        print(url)
        async with session.get(url) as r:
            return await r.text()
