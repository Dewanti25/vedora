import urllib.request, json
def post(path, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request('http://127.0.0.1:8000' + path, data=data, headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode())

if __name__ == '__main__':
    print('registering...')
    try:
        post('/register', {'email':'test@local','password':'pass123'})
    except Exception as e:
        print('register error', e)
    print('logging in...')
    try:
        post('/login', {'email':'test@local','password':'pass123'})
    except Exception as e:
        print('login error', e)
