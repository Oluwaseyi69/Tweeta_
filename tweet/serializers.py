from rest_framework import serializers

from tweet.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Tweet
        fields = '__all__'
    # id = serializers.IntegerField()
    # text = serializers.CharField(max_length=500)
    # last_updated = serializers.DateTimeField()


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Tweet
        fields = '__all__'
