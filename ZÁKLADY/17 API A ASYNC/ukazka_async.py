import asyncio

async def make_coffee():
    print("Coffee starting...")
    await asyncio.sleep(3)
    print("Coffee is ready!")
    return "coffee"


async def make_yoghurt():
    print("Making yoghurt...")
    await asyncio.sleep(2)
    print("Yoghurt done")
    return "yoghurt"


async def make_breakfast():
    coffee, yoghurt = await asyncio.gather(
        make_coffee(),
        make_yoghurt()
    )
    print(f"Breakfast is ready: {coffee} + {yoghurt}")


asyncio.run(make_breakfast())
