from apscheduler.schedulers.background import BackgroundScheduler

#time out 방지용 option / aiohttp 와 결합하여 사용 가능
schedulers = BackgroundScheduler(misfire_grace_time=3600, coalesce=True)
schedulers.add_job(asyncio_schedule, 'interval', minutes=10)
schedulers.start()