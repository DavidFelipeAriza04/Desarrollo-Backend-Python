from rest_framework import serializers
from .models import Project, Task

class ProjectSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskDetailSerializer(serializers.ModelSerializer):
    
    project = ProjectSerializerModel()
    class Meta:
        model = Task
        fields = '__all__'
        
class ProjectSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=60)
    init_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField()
    
    def validate(self, attrs):
        #Validacion end_date > init_date
        # if attrs['end_date'] < attrs['init_date']:
        #     raise serializers.ValidationError("End date must be greater than init date")
        return super().validate(attrs)
    
    def validate_name(self, value):
        if('david' in value):
            raise serializers.ValidationError("Name cannot contain david")
        return value
    
    def create(self, validated_data):
        Project(**validated_data).save()
        return self.data