# 스케쥴러
# pip install apscheduler
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
# 실행함수
def exec_interval():
    print('interval')
    print(datetime.datetime.now())
def exec_cron(a, b):
    print('cron')
    print(datetime.datetime.now())
sched = BlockingScheduler()
# interval 잡 등록
sched.add_job(exec_interval, 'interval', seconds=10)
# cron 잡 등록
sched.add_job(exec_cron, 'cron', hour=10, minute=40, args=['a','b'])
# 시작
sched.start()