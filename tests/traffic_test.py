import concurrent.futures
import requests
import time

NUM_REQUESTS = 100
API_URL = "https://my-api.com"

def send_request():
    response = requests.get(API_URL)
    return response.status_code

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(send_request, range(NUM_REQUESTS)))

end_time = time.time()

success_rate = results.count(200) / NUM_REQUESTS
avg_response_time = (end_time - start_time) / NUM_REQUESTS

print(f"Success rate: {success_rate:.2%}")
print(f"Average response time: {avg_response_time:.2f} seconds")