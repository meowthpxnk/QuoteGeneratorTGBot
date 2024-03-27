import aiohttp

async def request(url, headers=None):
    async with aiohttp.ClientSession(headers=headers) as session:
        res = await session.get(url)
        return await res.json()