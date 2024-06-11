from django.shortcuts import render
from django.http import JsonResponse
from google.cloud import storage
import os

def list_blobs(request):
    creds_path = os.path.join(os.path.dirname(__file__), 'taller-integracion-310700-41f361102b8b.json')
    storage_client = storage.Client.from_service_account_json('/etc/secrets/taller-integracion-310700-41f361102b8b.json')
    blobs = storage_client.list_blobs('2024-1-tarea-3')
    blobs_dict = {}
    for blob in blobs:
        blobs_dict[blob.name] = blob.download_as_string().decode('utf-8')


    return JsonResponse(blobs_dict)