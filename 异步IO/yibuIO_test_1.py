import asyncio  # 异步IO

@asyncio.coroutine  # 异步IO  协程支持
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1)，不然看不出异步协程的效果
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
