from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(max_length=50, source="author.first_name", required=False)
    author_last_name = serializers.CharField(max_length=50, source="author.last_name", required=False)
    author_image = serializers.ImageField(source="author.image", required=False)

    class Meta:
        model = Comment
        fields = ["pk", "text", "author_id", "created_at", "author_first_name", "author_last_name", "ad_id",
                  "author_image"]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    phone = serializers.CharField(source="author.phone", required=False)
    author_first_name = serializers.CharField(max_length=50, source="author.first_name", required=False)
    author_last_name = serializers.CharField(max_length=50, source="author.last_name", required=False)

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description", "author_id", "phone", "author_first_name",
                  "author_last_name"]
