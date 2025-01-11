import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task(10)
    def add(self):
        for a in range(10):
            self.client.get(f"/add?a={a}00&b=999", name = "sachiel")
            time.sleep(1)

    @task()
    def sub(self):
        for a in range(10):
            self.client.get(f"/sub?a={a}00&b=999", name = "shamshel")
            time.sleep(1)
    
    @task(2)
    def mul(self):
        for a in range(10):
            self.client.get(f"/mul?a={a}00&b=999", name = "ramiel")
            time.sleep(1)
        
    @task()
    def secret(self):
        for a in range(10):
            self.client.get(f"/secret?X={a}", name = "gaghiel")
            time.sleep(1)
    