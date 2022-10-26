from locust import HttpUser, task

class AzrapayLoadTest(HttpUser):
    @task
    def login_api(self): 
        self.client.post(url='/api/v1/login',headers={'AuthId':'N/A','Username':'##','Content-Type':'multipart/form-data'},data={'username':'##','password':'##'})