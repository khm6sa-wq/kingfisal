import asyncio
import os
import edge_tts

VOICE = "ar-SA-HamedNeural"
PREFIXES = ["A", "B", "C", "D", "E", "F", "G"]
MAX_NUMBER = 100

async def generate_all():
    os.makedirs("sounds/numbers", exist_ok=True)
    tasks = []
    for prefix in PREFIXES:
        for num in range(1, MAX_NUMBER + 1):
            ticket_code = f"{prefix}-{num}"
            spoken_text = f"{prefix} {num}"
            out_path = f"sounds/numbers/{ticket_code}.mp3"
            tasks.append(edge_tts.Communicate(spoken_text, VOICE).save(out_path))

    chunk_size = 20
    for i in range(0, len(tasks), chunk_size):
        await asyncio.gather(*tasks[i:i + chunk_size])
        print(f"تم توليد دفعة: {i + len(tasks[i:i + chunk_size])} / {len(tasks)}")

asyncio.run(generate_all())