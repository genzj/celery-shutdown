from celery import Celery

app = Celery(
    'tasks',
    broker='redis://localhost',
    backend='redis://localhost',
)


cnt = 0


@app.task(bind=True)
def add(self, x, y):
    global cnt
    if cnt == 2:
        app.control.shutdown(destination=[self.request.hostname])
        self.retry(countdown=1.0)
    else:
        cnt += 1
        return x + y
