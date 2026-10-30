import asyncio

async def async_greet(name: str) -> str:
    """Асинхронно возвращает приветствие."""
    await asyncio.sleep(0.1)  # имитация асинхронной операции
    return f"Hello, {name}! (async)"

async def run_greeting() -> str:
    return await async_greet("Engineer")
