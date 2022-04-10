import asyncio

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Test Asyncio'

    def add_arguments(self, parser):
        parser.add_argument('--n', dest='number', type=int)

    def handle(self, *args, **options):
        # number = options.get('number') # not using just comment
        ioloop = asyncio.get_event_loop()  # controls all the tasks
        asyncio.set_event_loop(ioloop)
        tasks = [ioloop.create_task(self.foo()), ioloop.create_task(self.bar())]
        wait_tasks = asyncio.wait(tasks)
        print('1')
        ioloop.run_until_complete(wait_tasks)
        print('2')
        ioloop.close()

    @staticmethod
    async def foo():  # asyncio means this is as coroutine
        print('Running in foo')
        await asyncio.sleep(3)  # means we can pass the control to get_event_loop
        print('Explicit context switch to foo again')

    @staticmethod
    async def bar():
        print('Explicit context to bar')
        await asyncio.sleep(1)
        print('Implicit context switch back to bar')
