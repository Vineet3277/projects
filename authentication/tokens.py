from django.contrib.auth.tokens import PasswordResetTokenGenerator 
# generally used to reset the password, but we will use to activate the account.
from six import text_type


class TokenGenrator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp)
        )
    
genrate_token = TokenGenrator()