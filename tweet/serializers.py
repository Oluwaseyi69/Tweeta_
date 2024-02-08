from rest_framework import serializers

from tweet.models import Tweet, Comment


class TweetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Tweet
        fields = ['id', 'text', 'last_updated', 'comments']
        # fields = '__all__'
    # id = serializers.IntegerField()
    # text = serializers.CharField(max_length=500)
    # last_updated = serializers.DateTimeField()


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    # tweet = serializers.HyperlinkedRelatedField(
    #     'tweet-detail', queryset=Tweet.objects.all())
    # comment_id = serializers.IntegerField(read_only=True)
    # id = serializers.IntegerField(read_only=True)
    # created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['id', 'text', 'last_updated', 'comments']
