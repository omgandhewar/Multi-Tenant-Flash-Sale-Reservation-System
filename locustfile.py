from locust import HttpUser, task, between

class website(HttpUser):
    wait_time=between(1,3)
    
    @task
    def event_name(self):
        response=self.client.get("/event_name")
        
        if response.status_code==200:
            data=response.json()
            print(data)
        
            event_name=data[0]["event_name"]
        
            response2=self.client.get(f"/movieslot/{event_name}")
        
            quantity=5
        
            response3=self.client.post("/reserve",json={"event_name":event_name,"quantity":quantity})
        
        