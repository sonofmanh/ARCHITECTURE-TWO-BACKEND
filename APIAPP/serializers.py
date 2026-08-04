from .models import contact,construction,feature, Image
from rest_framework.serializers import ModelSerializer

class contactserialiser(ModelSerializer):
    class Meta:
        model = contact
        fields = '__all__'



class featureserialiser(ModelSerializer):
    class Meta:
        model = feature
        fields = ['keyfeature1']

class Imageserialiser(ModelSerializer): 
    class Meta:
        model = Image
        fields = ['image']

class constructserialiser(ModelSerializer):
    features = featureserialiser(many=True,read_only=True)
    image = Imageserialiser(many=True,read_only=True)
    # names for features and image are exact as name in models as related names
    class Meta:
        model = construction
        fields = ['details','title','location','year','company','size','completed','type','features','image']




