import requests
import json

def get_form_submissions(api_key, submission_id):
    url = f"https://api.jotform.com/submission/{submission_id}"
    params = {'apiKey': api_key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
       
        return None

def get_submission_data(submission_ID):
    # Replace '48cec1b525331730de6371554c2613a4' with your actual JotForm API key
    api_key = "980ea3de9e275ece5334aab9a87a1246"

   
   

    submission = get_form_submissions(api_key, submission_ID)

    if submission:
       
        return(submission)
        # print(submissions['content'][0]['answers']['6']['answer'])
        # print(submissions['content'][1]['ip'])
    else:
        print("Failed to fetch form submissions.")


