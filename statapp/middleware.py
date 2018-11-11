from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


class ValidLogin(object):

    def process_request(self):
        if not self.user.is_authenticated():
            return HttpResponseRedirect(reverse('login'))
        return None
