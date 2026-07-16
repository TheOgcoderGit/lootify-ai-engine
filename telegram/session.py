from telegram.client import client

async def start_session():
    await client.start()
    me = await client.get_me()
    print(f"Logged in as: {me.first_name}")
