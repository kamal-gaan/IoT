import json
from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
    action,
)
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


from .models import Devices, Reads
from django.contrib.auth.models import User
from django.utils.dateparse import parse_datetime
from django.utils.dateparse import parse_date
from datetime import timedelta
from django.db.models import Avg, Max, Min


from .serializers import (
    DevicesSerializer,
    ReadsSerializer,
    UserSerializer,
    ReadsDateRangeSerializer,
    ReadsSummarySerializer,
)
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    CreateAPIView,
)


@api_view(["GET"])
def find_device_by_name(request, device_name):
    snippets = Devices.objects.get(device_name=device_name)
    serializer = DevicesSerializer(snippets)

    return Response(serializer.data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def list_all_devices(request):
    snippets = Devices.objects.all()
    serializer = DevicesSerializer(snippets, many=True)
    return Response(serializer.data)


class DevicesDateRangeViewSet(viewsets.ModelViewSet):
    queryset = Reads.objects.all()
    serializer_class = ReadsDateRangeSerializer

    @action(detail=True, methods=["POST"])
    def date_range(self, request):
        device_name = request.query_params.get("device_name")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        if not device_name or not start_date or not end_date:
            return Response(
                {
                    "error": "Please provide device_name, start_date, and end_date query parameters."
                },
                status=400,
            )

        try:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
        except ValueError:
            return Response({"error": "Invalid date format."}, status=400)

        if not start_date or not end_date:
            return Response(
                {"error": "Invalid date format. Please use YYYY-MM-DD."}, status=400
            )

        # Ensure end_date includes the whole day
        end_date = end_date + timedelta(days=1)

        try:
            device = Devices.objects.get(device_name=device_name)
        except Devices.DoesNotExist:
            return Response({"error": "Device not found."}, status=404)

        reads = Reads.objects.filter(
            sensor_id=device, datetime__gte=start_date, datetime__lt=end_date
        )
        serializer = ReadsSerializer(reads, many=True)
        return Response(serializer.data)


class ReadsSummaryViewSet(viewsets.ViewSet):
    queryset = Reads.objects.all()
    serializer_class = ReadsSummarySerializer

    @action(detail=True, methods=["post"])
    def summary(self, request):
        serializer = ReadsSummarySerializer(data=request.data)
        if serializer.is_valid():
            device_name = serializer.validated_data["device_name"]
            start_date = serializer.validated_data["start_date"]
            end_date = serializer.validated_data["end_date"]

            # Querying and computing min, max, avg temperatures
            reads = Reads.objects.filter(
                sensor_id__device_name=device_name,
                datetime__date__range=(start_date, end_date),
            )

            max_temperature = reads.aggregate(Max("temp"))["temp__max"]
            min_temperature = reads.aggregate(Min("temp"))["temp__min"]
            avg_temperature = reads.aggregate(Avg("temp"))["temp__avg"]

            # Constructing the response
            response_data = {
                "device_name": device_name,
                "start_date": start_date,
                "end_date": end_date,
                "max_temperature": max_temperature,
                "min_temperature": min_temperature,
                "avg_temperature": avg_temperature,
            }
            return Response(response_data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class DevicesViewsSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer

    @action(detail=True, methods=["get"])
    def reads(self, request, pk=None):
        device = self.get_object()
        reads = device.reads_set.all()
        serializer = ReadsSerializer(reads, many=True)
        return Response(serializer.data)


class ReadViewSet(viewsets.ModelViewSet):
    queryset = Reads.objects.all()
    serializer_class = ReadsSerializer
