import base64
from secrets import API_APPLICATION_ID, API_SECRET_KEY  # type: ignore
import requests

creds = f"{API_APPLICATION_ID}:{API_SECRET_KEY}"
credsbytes = creds.encode('utf-8')
credsencode = base64.b64encode(credsbytes)
header = f'Authorization: Basic {credsencode}'