import requests, os

# Authentication

host = os.environ.get('host') if os.environ.get('host') else 'http://localhost'
port = os.environ.get('port') if os.environ.get('port') else '3000'
healthCheckEndpoint = f'{host}:{port}/api/health'
properties = f'{host}:{port}/api/session/properties'
setup = f'{host}:{port}/api/setup'
database = f'{host}:{port}/api/database'
login = f'{host}:{port}/api/session'

sqlite = {"is_on_demand":False,"is_full_sync":True,"is_sample":False,"cache_ttl":None,"refingerprint":False,"auto_run_queries":True,"schedules":{},"details":{"db":"/home/metabase/datastacksurvey2025.db","advanced-options":False,"destination-database":False},"name":"Data Stack Survey 2025","engine":"sqlite"}

def health():
    response = requests.get(healthCheckEndpoint, verify=False)
    if response.json()['status'] == 'ok':
        return 'healthy'
    else:
        health()

if health() == 'healthy' and os.environ.get('retry') == 'yes':
    loginPayload = { 'username': 'a@b.com', 'password': 'metabot1' }
    session = requests.Session()
    sessionToken = session.post(login, verify=False, json=loginPayload)
    session.post(database, verify=False, json=sqlite)

if health() == 'healthy' and os.environ.get('retry') is None:
    session = requests.Session()
    token = session.get(properties, verify=False).json()['setup-token']
    setupPayload = {
        'token':f'{token}',
        'user':{
            'first_name':'a',
            'last_name':'b',
            'email':'a@b.com',
            'password':'metabot1',
        },
        'prefs':{
            'site_name':'metabot1',
            'site_locale':'en',
            'allow_tracking':False
        }
    }
    try:
        print(f'sending a call with token: {setupPayload}')
        sessionToken = session.post(setup, verify=False, json=setupPayload)
        print(sessionToken.json())
        try:
            session.post(database, verify=False, json=sqlite)
        except:
            session.post(database, verify=False, json=sqlite)

    except:
        exit()