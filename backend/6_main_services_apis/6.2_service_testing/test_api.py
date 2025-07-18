import requests

def test_predict():
    url = "http://127.0.0.1:8000/predict"
    data = {"prices": [10000, 10010, 10020, 10030, 10040, 10050, 10060, 10070, 10080, 10090]}
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response:", response.json())

if __name__ == "__main__":
    test_predict()
