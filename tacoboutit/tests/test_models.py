from mixer.backend.django import mixer
import pytest
@pytest.mark.django_db
class TestModels:

    def test_restaurant_has_tacos(self):
        #create the taco
        rest = mixer.blend('myapi.Restaurant', name='scotts tacos')
        assert rest.tacos
        
    # def test_str_method(self):
    #     rest = mixer.blend('myapi.Restaurant', name='scotts tacos')
    #     assert rest.__str_()
