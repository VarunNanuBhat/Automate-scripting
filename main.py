import json

# Load the HAR file
with open('tryingout.har', 'r', encoding='utf-8') as f:
    har_data = json.load(f)

# Iterate through entries and filter based on URL
for entry in har_data['log']['entries']:
    request = entry['request']
    response = entry['response']

    # Check if the request URL contains 'disneycruise.disney.go.com'
    if 'disneycruise.disney.go.com' in request['url']:
        print(f"Request URL: {request['url']}")
        print(f"Response Status: {response['status']}")

        # Extract and print the request payload if available
        if 'postData' in request and 'text' in request['postData']:
            try:
                request_payload = json.loads(request['postData']['text'])
                print("Request Payload (JSON):")
                print(json.dumps(request_payload, indent=4))
            except json.JSONDecodeError:
                print("Request Payload: (Non-JSON or malformed JSON data)")
                print(request['postData']['text'])
        else:
            print("Request Payload: No payload available")

        # Extract and print the response content if it is valid JSON
        if 'content' in response and 'text' in response['content']:
            try:
                response_content = json.loads(response['content']['text'])
                print("Response Content (JSON):")
                print(json.dumps(response_content, indent=4))
            except json.JSONDecodeError:
                print("Response Content: Not a valid JSON")
        else:
            print("Response Content: No content available")
        print()
