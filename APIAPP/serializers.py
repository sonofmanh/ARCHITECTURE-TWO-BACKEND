from .models import contact,construction,feature, Image
from rest_framework.serializers import ModelSerializer


class contactserialiser(ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'


class featureserialiser(ModelSerializer):
    class Meta:
        model = feature
        fields = '__all__'

class Imageserialiser(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class constructserialiser(ModelSerializer):
    features = featureserialiser()
    image = Imageserialiser()
    class Meta:
        model = construction
        fields = '__all__'




