from locust import HttpUser, TaskSet, task, between

class CuramTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        pass
    
    def on_stop(self):
        pass

    @task(1)
    def testCuramGet(self):
        self.client.get("/", verify=False)

    @task(2)
    def testCuramPost(self):
        pass