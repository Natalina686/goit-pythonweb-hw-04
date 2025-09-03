import argparse
import asyncio
import logging
from aiopath import AsyncPath
import aiofiles
import shutil

async def copy_file(file: AsyncPath, output_dir: AsyncPath):
    pass

async def read_folder(source: AsyncPath, output: AsyncPath):
    pass

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