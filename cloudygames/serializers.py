from rest_framework import serializers
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from cloudygames.models import Game, PlayerSaveData, GameSession

class GameSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        many=True,
        queryset=User.objects.all(),
        slug_field='username'
    )
    
    class Meta:
        model = Game
        fields = ('id', 'name', 'publisher', 'max_limit', 'address', 'users')

class PlayerSaveDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayerSaveData
        fields = ('id', 'saved_file', 'is_autosaved', 'player', 'game')

    def create(self, data):
        data.player = self.request.user
        return PlayerSaveData.objects.create(data)

class GameSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameSession
        fields = ('game',)