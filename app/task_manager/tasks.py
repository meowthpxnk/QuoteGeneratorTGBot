import datetime

import asyncio

from app import bot, users_db
from app.tg_bot.quote_message import NewQuoteMessage

async def send_quote():
    quoted_message = await NewQuoteMessage.generate()

    tasks = []

    for user_id in users_db.get_records():
        tasks.append(
            asyncio.create_task(
                bot.send_quote(user_id, quoted_message)
            )
        )
    
    await asyncio.gather(*tasks)

async def wait_for(coro, secs):
    await asyncio.sleep(secs)
    await coro()

async def generateNewTasks():
    from app import loop
    now = datetime.datetime.now()
    now = now - datetime.timedelta(
        hours=now.hour,
        minutes=now.minute,
        seconds=now.second,
        microseconds=now.microsecond
    )

    task1 = now + datetime.timedelta(
        hours=12,
        minutes=0,
        seconds=0,
    )

    task1 = (task1 - datetime.datetime.now()).total_seconds()

    task2 = now + datetime.timedelta(
        hours=16
    )
    task2 = (task2 - datetime.datetime.now()).total_seconds()

    root_task = now + datetime.timedelta(
        days=1
    )

    root_task = (root_task - datetime.datetime.now()).total_seconds()

    if task1 > 0:
        print(task1)
        loop.create_task(wait_for(send_quote, task1))
    
    if task2 > 0:
        print(task2)
        loop.create_task(wait_for(send_quote, task2))
    
    print(root_task)
    loop.create_task(wait_for(generateNewTasks, root_task))