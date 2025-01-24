from patch import *  # MUST be at the top # noqa: F403, I001

import asyncio
import random

from image_creator import create_picture


async def generate_and_save(deck_code):
    image = await create_picture(deck_code)

    if not image:
        return None

    x, y = image.size
    image = image.resize((int(x / 1.2), int(y / 1.2)))

    name = random.randint(1000000, 10000000)

    image.save(f"decks/{name}.png", format="PNG")

    return name


async def deck(deck_code: str):
    name = await generate_and_save(deck_code)
    print(name)
    # os.remove(f"{name}.png")


if __name__ == "__main__":
    asyncio.run(
        deck(
            "AAECAfHhBASYxAXzyAXO8Qb/9wYNh/YE8OgFhY4G/7oGkMsGoOIG4eoGn/EGrPEGvvEGwvEG4/EGqPcGAAA=",
        ),
    )
