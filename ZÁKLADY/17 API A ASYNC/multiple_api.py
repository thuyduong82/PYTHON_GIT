import asyncio
import httpx

url = "https://cataas.com/cat"

async def fetch_cat(id):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        file_name = f"cat{id}.jpg"
        with open(file_name, "wb") as f:
            f.write(response.content)
        
        return file_name

async def main():
    cats = []
    for i in range(1, 6):
        cats.append(fetch_cat(i))
    
    # cats = [fetch_cat(i) for i in range(1, 6)]

    file_names = await asyncio.gather(*cats)

    print(f"Downloaded {len(file_names)} cats")

asyncio.run(main())




