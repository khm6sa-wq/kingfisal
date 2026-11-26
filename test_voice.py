import asyncio
import os
import edge_tts

OUT_DIR = "test_sounds"
os.makedirs(OUT_DIR, exist_ok=True)

SAMPLES = [
    ("test_hamed.mp3", "ar-SA-HamedNeural", "تذكرة رقم ألف واحد، يرجى التوجه إلى عيادة الباطنية."),
    ("test_zariyah.mp3", "ar-SA-ZariyahNeural", "تذكرة رقم ألف واحد، يرجى التوجه إلى عيادة الباطنية."),
]

async def main():
    for filename, voice, text in SAMPLES:
        out_path = os.path.join(OUT_DIR, filename)
        comm = edge_tts.Communicate(text=text, voice=voice, rate="-4%", pitch="-1Hz")
        await comm.save(out_path)
        print("تم إنشاء:", out_path)

if __name__ == "__main__":
    asyncio.run(main())