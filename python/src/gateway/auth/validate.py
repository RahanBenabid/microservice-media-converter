#!/usr/bin/env python3

import os, requests

def token(request):
	if not "Authorization" in request.headers:
		return None, ("Missing credentials", 401)
	
	token = request.headers.get("Authorization")
	
	if not token:
		return None, ("Missing credentials", 401)
	
	reponse = requests.post(
		f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
		headers={"Authorization": token},
	)
	
	if reponse.status_code == 200:
		return response.text, None
	else:
		return None, (reponse.txt, reponse.status_code)