from fastapi import FastAPI
from fastapi.responses import FileResponse
import google.auth.transport.requests
from google.oauth2 import service_account

app = FastAPI()

SCOPES = ['https://www.googleapis.com/auth/firebase.messaging']


@app.get("/")
async def root():
    return {"details": "no details"}

@app.get("/get-access-token")
async def get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.

    :return: Access token.
    """
    credentials = service_account.Credentials.from_service_account_file(
        'service-account.json', scopes=SCOPES)
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    # make it an array to be able to use it in the header
    return {"status": 200, "credentials": credentials.token}
