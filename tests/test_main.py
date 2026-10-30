import pytest
import asyncio
from ai_engineer.main import async_greet, run_greeting

@pytest.mark.asyncio
async def test_async_greet():
    result = await async_greet("World")
    assert result == "Hello, World! (async)"

@pytest.mark.asyncio
async def test_run_greeting():
    result = await run_greeting()
    assert result == "Hello, Engineer! (async)"

