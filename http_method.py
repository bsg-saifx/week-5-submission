import requests

def get_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def post_request():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "Hello world!",
        "body": "New to this world",
        "userId": 1
    }
    response = requests.post(url, json=payload)

    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    get_request()
    post_request()
