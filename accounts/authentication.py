import requests
import sys
from accounts.model import ListUser

class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        # Send assertion to Mozilla's verification service
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('Sending to Mozilla', data, file=sys.stderr)
        resp = requests.post('https://verifier.login.persona.org/verify', data=data)
        print('got', resp.content, file=sys.stderr)

        if resp.ok:
            # parse response if received
            verification_data = resp.json()

            # Check assertion valid
            if verification_data['status'] == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.objects.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)