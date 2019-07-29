from celery import Celery

app = Celery(
    'tasks',
    broker='redis://localhost',
    backend='redis://localhost',
)
app.conf.worker_pool_restarts = True


cnt = 0


@app.task(bind=True)
def add(self, x, y):
    global cnt
    if cnt == 2:
        #app.control.shutdown(destination=[self.request.hostname])
        app.control.pool_restart(destination=[self.request.hostname])
        self.retry(countdown=5.0)
    else:
        cnt += 1
        return x + y
