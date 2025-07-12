import asyncio
from typing import AsyncGenerator

# Dummy async AI model integration for emotional response
async def generate_emotional_response(message: str) -> AsyncGenerator[str, None]:
    # Simulate streaming response
    for word in ("I understand how you feel. Let's talk about it.".split()):
        await asyncio.sleep(0.2)
        yield word + " "
