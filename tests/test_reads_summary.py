import pytest
from unittest.mock import patch
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import date
from devices.models import Devices, Reads
from devices.serializers import ReadsSummarySerializer

@pytest.mark.django_db
def test_reads_summary_view_set():
    # Create test data
    device = Devices.objects.create(device_name="TestDevice")
    Reads.objects.create(sensor_id=device, temp=25.5)

    # Mock the request data
    request_data = {
        "device_name": "TestDevice",
        "start_date": date.today(),
        "end_date": date.today(),
    }

    # Mocking the serializer's behavior
    with patch.object(ReadsSummarySerializer, "is_valid", return_value=True):
        with patch.object(ReadsSummarySerializer, "create", return_value=request_data):
            client = APIClient()
            url = reverse("reads-summary")
            response = client.post(url, request_data, format="json")

    assert response.status_code == 200
    assert "device_name" in response.data
    assert "start_date" in response.data
    assert "end_date" in response.data
    assert "avg_temp" in response.data
    assert "max_temp" in response.data
    assert "min_temp" in response.data
    