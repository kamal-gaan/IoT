from rest_framework import serializers
from devices.models import Devices, Reads
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = "__all__"


class ReadsSerializer(serializers.ModelSerializer):
    device_name = serializers.RelatedField(read_only=True)

    class Meta:
        model = Reads
        fields = "__all__"


class ReadsSummarySerializer(serializers.Serializer):
    device_name = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    max_temperature = serializers.FloatField(required=False)
    min_temperature = serializers.FloatField(required=False)
    avg_temperature = serializers.FloatField(required=False)
    def validate(self, data):
        """
        Validate that start_date is before end_date.
        """
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        if start_date and end_date:
            if start_date > end_date:
                raise serializers.ValidationError("start_date must be before end_date.")

        return data

    def create(self, validated_data):
        """
        Process summary logic and return summary data.
        """
        device_name = validated_data.get("device_name")
        start_date = validated_data.get("start_date")
        end_date = validated_data.get("end_date")

        device = Devices.objects.get(device_name=device_name)

        # Calculate summary metrics for temperature readings
        summary = Reads.objects.filter(
            sensor_id=device,
            datetime__date__gte=start_date,
            datetime__date__lte=end_date,
        ).aggregate(avg_temp=Avg("temp"), max_temp=Max("temp"), min_temp=Min("temp"))

        return {
            "device_name": device_name,
            "start_date": start_date,
            "end_date": end_date,
            "avg_temp": summary["avg_temp"],
            "max_temp": summary["max_temp"],
            "min_temp": summary["min_temp"],
        }

    def update(self, instance, validated_data):
        """
        Not needed for this serializer as it's read-only.
        """
        pass


class ReadsDateRangeSerializer(serializers.ModelSerializer):
    sensor_id = serializers.PrimaryKeyRelatedField(queryset=Devices.objects.all())
    device = serializers.RelatedField(source="device_name", read_only=True)

    class Meta:
        model = Reads
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()

        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = (
            "id",
            "username",
            "password",
        )
