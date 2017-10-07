# watson-python-app
MassChallenge 2017 (Oct 6 - Oct8)
Tutorial led by Chyld on Oct 7

#### Prerequisites ####

- Python 2.7.12
- Flask 0.11.1
- IPython 5.5.0
- watson-developer-cloud 0.26.1

#### Base Files####

1. `main.py` with Flask app:

   ```python
   import sys
   import json
   from flask import Flask, render_template, request

   app = Flask(__name__)

   @app.route("/", methods=["GET"])
   ```

2. Tone Analyzer on Bluemix

   ```
   {
     "credentials": {
       "url": "https://gateway.watsonplatform.net/tone-analyzer/api",
       "username": "0f02dd95-69ff-42f9-82f5-5a87c7d8707b",
       "password": "HC2AZdsjGOFC"
     },
     "syslog_drain_url": null,
     "volume_mounts": [],
     "label": "tone_analyzer",
     "provider": null,
     "plan": "lite",
     "name": "Tone Analyzer-tz",
     "tags": [
       "watson",
       "ibm_created",
       "ibm_dedicated_public",
       "lite"
     ]
   }
   ```

3. ​


