from locust import HttpUser, task, between
import random
import sys

class website(HttpUser):
    wait_time=between(1,3)
    
    @task
    def event_name(self):
        response=self.client.get("/event_name")
        
        if response.status_code==200:
            data=response.json()
            print(data)
        
            event_name =random.choice(data["event_name"])["event_name"]
            
            response2=self.client.get(f"/movieslot/{event_name}")
            
            data=response2.json()
           
            if response2.status_code==404:
                print(
                    data["detail"]
                )
                    
        
            if response2.status_code==200:
                quantity=random.choice(range(1,10))
        
                response3=self.client.post("/reserve",json={"event_name":event_name,"quantity":quantity}) 
                
                data=response3.json()   
                
                if response3.status_code == 200:
                    print(
                        data["message"]
                    )
                else:
                    print(
                        f"Reservation failed {quantity} {event_name}",
                        response3.text
                    )