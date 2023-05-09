from rest_framework import serializers
from .models import MyUser, UserProfile


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = MyUser
        fields = ["email", "first_name", "last_name", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = MyUser(
            email=self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
        )
        
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        style={"input_type": "password"}, required=True
    )
    new_password = serializers.CharField(
        style={"input_type": "password"}, required=True
    )

    def validate_current_password(self, value):
        if not self.context["request"].user.check_password(value):
            raise serializers.ValidationError({"current_password": "Does not match"})
        return value


class UserProfileSerializer(serializers.ModelSerializer):
    #technology_name = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = UserProfile
        fields = ['user_id', 'profile_pic', 'phone', 'designation', 'experiance', 'interest', 'technology_name']
        #fields = ['user_id', 'profile_pic', 'phone', 'designation', 'experiance', 'interest']
        #exclude = ('is_active', 'is_delete', 'created_at', 'updated_at')


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name']


