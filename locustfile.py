import pandas as pd
import os
from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    headers = None

    def on_start(self):
        headers = {
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    @task
    def test_seeker_groups(self):
        self.client.get("/predict")
