import aiohttp, boto3, asyncio

from django.http import JsonResponse
from asgiref.sync import sync_to_async

@sync_to_async
def save_result(pk, status):
    return True

@sync_to_async
def fail_result(pk):
    return False

@sync_to_async
def _get_url():
    url = {}
    # 테이블 호출 후 pk 값을 key 저장, 사용할 url 값을 value에 저장
    url[object_id] = "http://tsetsetsetset" 

async def hello_world():
    async with aiohttp.ClientSession() as session:
        # url = await sync_to_async(_get_url, thread_sensitive=True)(10)
        urls = await _get_url()
        for object_id, each_url in urls.items():
            async with session.get(each_url) as response:
                if response.status == 200:
                    result = await response.text()
                    await save_result(pk=object_id, status=result)
                else:
                    await fail_result(pk=object_id)

        return JsonResponse(json_success("S0004", 'test'), status=status.HTTP_200_OK)

def asyncio_schedule():
    asyncio.run(hello_world())

if __name__ == "__main__":
    asyncio_schedule()