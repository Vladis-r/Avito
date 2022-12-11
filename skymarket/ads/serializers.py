from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from ads.models import Ad, Comment
from users.models import User
from users.serializers import CurrentUserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only=True)
    # author = serializers.SerializerMethodField('_user')
    #
    # def _user(self, obj):
    #     request = self.context.get('request', None)
    #     if request:
    #         return request.user

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description", "author"]

    def create(self, request, *args, **kwargs):
        user = self.context['request'].user
        data = request.POST
        data["author"] = user
        return super().create(validated_data=data)


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

    author = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super(AdDetailSerializer, self).create(validated_data)
