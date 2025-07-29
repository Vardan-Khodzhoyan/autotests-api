import httpx

login_payload = {
  "email": "xva333@gmail.com",
  "password": "qazWSX123"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

