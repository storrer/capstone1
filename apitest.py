import base64
from secrets import API_APPLICATION_ID, API_SECRET_KEY  # type: ignore
import requests

creds = f"{API_APPLICATION_ID}:{API_SECRET_KEY}"
credsbytes = creds.encode('utf-8')
credsencode = base64.b64encode(credsbytes)
header = {'Authorization': f'Basic {credsencode}'}
endpoint = 'https://api.astronomyapi.com/api/v2/studio/star-chart'
parameters = {
    "observer": {
        "latitude": 33.775867,
        "longitude": -84.39733,
        "date": "2019-12-20"
    },
    "view": {
        "type": "area",
        "parameters": {
            "position": {
                "equatorial": {
                    "rightAscension": 14.83,
                    "declination": -15.23
                }
            },
            "zoom": 3
        }
    }
}
