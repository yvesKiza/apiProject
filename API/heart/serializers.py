from rest_framework import serializers
from .models import hospital
from django.core.validators import MinValueValidator,  MaxValueValidator

sex_choices=((0, 'Female'),(1, 'Male'))
cp_choice=((0,'None'),(1, 'Typical Angina'),(2, 'Atypical Angina'),(3, 'Non-Angina'),(4, 'Asymptomatic'))
fasting_blood_sugar_choices=((1,'> 120 mg/dl'),((0,'< 120 mg/dl')))
resting_ecg_choices=((0, 'Normal'),(1, 'Having ST-T wave abnormality'),(2, 'hypertrophy'))
exercise_induced_angina_choices=((0, 'No'),(1, 'Yes'))
st_slope_choices=((1, 'Upsloping'),(2, 'Flat'),(3, 'Down Sloping'))
number_of_vessels_choices=((0, 'None'),(1, 'One'),(2, 'Two'),(3, 'Three'))
thallium_scan_results_choices=((3, 'Normal'),(6, 'Fixed Defect'),(7, 'Reversible Defect'))
 
class hospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=hospital
        fields='__all__'

class PredictionSerializer(serializers.Serializer):
    age = serializers.IntegerField(required=True,validators=[MinValueValidator(0),MaxValueValidator(150)])
    sex =serializers.ChoiceField(required=True,choices=sex_choices)
    cp = serializers.ChoiceField(required=True,choices=cp_choice)
    trestbps = serializers.IntegerField(required=True)
    chol= serializers.IntegerField(required=True)
    fbs = serializers.ChoiceField(required=True,choices=fasting_blood_sugar_choices)
    restecg = serializers.ChoiceField(required=True,choices=resting_ecg_choices)
    thalach = serializers.IntegerField(required=True)
    exang = serializers.ChoiceField(required=True,choices=exercise_induced_angina_choices)
    oldpeak = serializers.DecimalField(required=True,max_digits=4, decimal_places=2)
    slope= serializers.ChoiceField(required=True,choices=st_slope_choices)
    ca= serializers.ChoiceField(required=True,choices=number_of_vessels_choices)
    thal = serializers.ChoiceField(required=True,choices=thallium_scan_results_choices)
