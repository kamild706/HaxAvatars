from rest_framework import serializers
from avatars.models import Avatar
import re

# class AvatarSerializer(serializers.ModelSerializer):
#
#     def __init__(self, *args, **kwargs):
#         hide_fields = kwargs.pop('hide_fields', None)
#         super(AvatarSerializer, self).__init__(*args, **kwargs)
#
#         defined_fields = {'admin': ('id', 'is_deleted', 'created', 'updated',)}
#         if hide_fields:
#             # noinspection PyTypeChecker
#             for field in defined_fields[hide_fields]:
#                 self.fields.pop(field)
#
#     class Meta:
#         model = Avatar


def is_hex_value(value):
    pattern = re.compile('^([a-f\d]{6}|[a-f\d]{8})$', re.I)
    if not pattern.match(value):
        raise serializers.ValidationError("Must be valid hexadecimal string")


def is_team_name_correct(team_name):
    if team_name.lower() not in ('red', 'blue',):
        raise serializers.ValidationError("Must be either 'red' or 'blue'")


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        exclude = ('id', 'is_deleted', 'modified_at')


class AdminAvatarSerializer(serializers.ModelSerializer):
    color1 = serializers.CharField(validators=[is_hex_value])
    color2 = serializers.CharField(validators=[is_hex_value], required=False)
    color3 = serializers.CharField(validators=[is_hex_value], required=False)
    text_color = serializers.CharField(validators=[is_hex_value])
    desc = serializers.CharField(min_length=10, max_length=80)
    angle = serializers.IntegerField(min_value=0, max_value=360)

    class Meta:
        model = Avatar
