import requests

# Your Line Notify access token
line_notify_token = 'O962mosWYaTqYcpyGMYOMaZ0U2ZRuD80nCghTRbGmgU'

# Message you want to send
water_level = 2.01  # From your API response
message = f"Water Level: {water_level}"

# Line Notify API URL
line_notify_url = "https://notify-api.line.me/api/notify"

# Headers and data for the request
headers = {
    'Authorization': f'Bearer {line_notify_token}',
    'Content-Type': 'application/x-www-form-urlencoded'  # Ensure correct content type
}


def callAPI():
    data = {
        'message': message
    }
    
    # Sending the request
    res = requests.get("http://localhost:5000/status",  headers={
        'Content-Type': 'Application/json'
    })
    
    resJson = res.json()
    
    print('resJson', resJson)

    # Sending the request
    response = requests.post(line_notify_url, headers=headers, data={
        'message': f"Water Level: {resJson.water_level}",
        'imageFullsize': resJson.processed_image_url
    })

    # Check response status
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")
        print(f"Error message: {response.text}")
        
    return "Welcome to my Flask API on Heroku!"

if __name__ == '__main__':
    callAPI()