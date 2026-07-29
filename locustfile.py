from locust import HttpUser, task, between

class website(HttpUser):
    wait_time=between(1,3)
    
    @task
    def event_name(self):
        response=self.client.get("/event_name")
        
    @task
    def movie_slot(self):
        
        event_name = "Coldplay Music of the Spheres Mumbai"
        response2=self.client.get(f"/movieslot/{event_name}")
        
    @task
    def reserve(self):
        event_name = "Coldplay Music of the Spheres Mumbai"
        quantity=5
        
        response3=self.client.post("/reserve",json={"event_name":event_name,"quantity":quantity})
        print(response3.headers)
        
        