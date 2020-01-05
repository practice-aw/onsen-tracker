from django.urls import reverse, resolve

class TestUrls:
    def test_newtaco_url(self):
        path = reverse('new_taco')
        assert resolve(path).view_name == 'new_taco'
