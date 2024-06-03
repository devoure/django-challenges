import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from browser.models import Student
# Create your tests here.


@pytest.fixture
def defaults():
    client = APIClient()
    add_payload = {
            "student_name": "Burey Doe",
            "student_id": "3344",
            "grade": "A"
            }
    update_payload = {
            "student_name": "John Doe",
            "student_id": "3344",
            "grade": "A"
            }

    return client, add_payload, update_payload


@pytest.mark.django_db
def test_create(defaults):
    client, add_payload, _ = defaults
    url = reverse('create')
    res = client.post(url, add_payload)

    assert res.data["student_name"] == add_payload["student_name"]
    assert res.data["student_id"] == add_payload["student_id"]
    assert res.data["grade"] == add_payload["grade"]

    students = Student.objects.all().count()

    assert students == 1


@pytest.mark.django_db
def test_update(defaults):
    client, add_payload, update_payload = defaults
    student = Student.objects.create(**add_payload)
    student.save()
    url = reverse('update', kwargs={"pk": student.id})
    res = client.put(url, update_payload)

    assert res.data["student_name"] == update_payload["student_name"]
    assert res.data["student_id"] == update_payload["student_id"]
    assert res.data["grade"] == update_payload["grade"]


@pytest.mark.django_db
def test_delete(defaults):
    client, add_payload, update_payload = defaults
    student = Student.objects.create(**add_payload)
    student.save()

    url = reverse('delete', kwargs={"pk": student.id})
    client.delete(url)

    students = Student.objects.all()

    assert students.count() == 0
