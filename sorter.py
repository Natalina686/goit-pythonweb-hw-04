import argparse
import asyncio
import logging
from aiopath import AsyncPath
import aiofiles
import shutil

async def copy_file(file: AsyncPath, output_dir: AsyncPath):
    try:
        ext = file.suffix.lower().lstrip(".")
        if not ext:
            ext = "unknown"

        target_dir = output_dir / ext
        await target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / file.name

        await asyncio.to_thread(shutil.copy2, file, target_file)

        logging.info(f"Copied {file} -> {target_file}")

    except Exception as e:
        logging.error(f"Error copying {file}: {e}")

        

async def read_folder(source_dir: AsyncPath, output_dir: AsyncPath):
    try:
        tasks = []

        async for item in source_dir.iterdir():
            if await item.is_file():
                tasks.append(copy_file(item, output_dir))
            elif await item.is_dir():
                tasks.append(read_folder(item, output_dir))

        if tasks:
            await asyncio.gather(*tasks)

    except Exception as e:
        logging.error(f"Error reading folder {source_dir}: {e}")
        

async def main():
    parser = argparse.ArgumentParser(description="Async file sorter")
    parser.add_argument("--source", required=True, help="Source folder with files")
    parser.add_argument("--output", required=True, help="Output folder for sorted files")
    args = parser.parse_args()

    source = AsyncPath(args.source)
    output = AsyncPath(args.output)

    await read_folder(source, output)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    asyncio.run(main()) 