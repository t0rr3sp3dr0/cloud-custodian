# Copyright 2019 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Azure Functions
"""
# Docker version from https://hub.docker.com/r/microsoft/azure-functions/
FUNCTION_DOCKER_VERSION = 'DOCKER|mcr.microsoft.com/azure-functions/python:3.0-python3.8'
FUNCTION_EXT_VERSION = '~3'
FUNCTION_EVENT_TRIGGER_MODE = 'azure-event-grid'
FUNCTION_TIME_TRIGGER_MODE = 'azure-periodic'
FUNCTION_KEY_URL = 'hostruntime/admin/host/systemkeys/_master?api-version=2018-02-01'
FUNCTION_AUTOSCALE_NAME = 'cloud_custodian_default'
AUTH_TYPE_EMBED = "Embedded"
AUTH_TYPE_MSI = "SystemAssigned"
AUTH_TYPE_UAI = "UserAssigned"

"""
Azure Container Host
"""
CONTAINER_EVENT_TRIGGER_MODE = 'container-event'
CONTAINER_TIME_TRIGGER_MODE = 'container-periodic'
ENV_CONTAINER_STORAGE_RESOURCE_ID = 'AZURE_CONTAINER_STORAGE_RESOURCE_ID'
ENV_CONTAINER_QUEUE_NAME = 'AZURE_CONTAINER_QUEUE_NAME'
ENV_CONTAINER_POLICY_URI = 'AZURE_CONTAINER_POLICY_URI'
ENV_CONTAINER_OPTION_LOG_GROUP = 'AZURE_CONTAINER_LOG_GROUP'
ENV_CONTAINER_OPTION_METRICS = 'AZURE_CONTAINER_METRICS'
ENV_CONTAINER_OPTION_OUTPUT_DIR = 'AZURE_CONTAINER_OUTPUT_DIR'


"""
Event Grid Mode
"""
EVENT_GRID_UPN_CLAIM_JMES_PATH = \
    'data.claims."http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn"'
EVENT_GRID_NAME_CLAIM_JMES_PATH = \
    'data.claims."http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"'
EVENT_GRID_SP_NAME_JMES_PATH = 'data.claims.appid'
EVENT_GRID_SERVICE_ADMIN_JMES_PATH = \
    'data.claims."http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"'
EVENT_GRID_PRINCIPAL_TYPE_JMES_PATH = 'data.authorization.evidence.principalType'
EVENT_GRID_PRINCIPAL_ROLE_JMES_PATH = 'data.authorization.evidence.role'
EVENT_GRID_EVENT_TIME_PATH = 'eventTime'


"""
Environment Variables
"""
ENV_TENANT_ID = 'AZURE_TENANT_ID'
ENV_CLIENT_ID = 'AZURE_CLIENT_ID'
ENV_SUB_ID = 'AZURE_SUBSCRIPTION_ID'
ENV_CLIENT_SECRET = 'AZURE_CLIENT_SECRET'

ENV_KEYVAULT_CLIENT_ID = 'AZURE_KEYVAULT_CLIENT_ID'
ENV_KEYVAULT_SECRET_ID = 'AZURE_KEYVAULT_SECRET'

ENV_ACCESS_TOKEN = 'AZURE_ACCESS_TOKEN'

ENV_USE_MSI = 'AZURE_USE_MSI'

ENV_FUNCTION_TENANT_ID = 'AZURE_FUNCTION_TENANT_ID'
ENV_FUNCTION_CLIENT_ID = 'AZURE_FUNCTION_CLIENT_ID'
ENV_FUNCTION_CLIENT_SECRET = 'AZURE_FUNCTION_CLIENT_SECRET'

ENV_FUNCTION_SUB_ID = 'AZURE_FUNCTION_SUBSCRIPTION_ID'
ENV_FUNCTION_MANAGEMENT_GROUP_NAME = 'AZURE_FUNCTION_MANAGEMENT_GROUP_NAME'

# Allow disabling SSL cert validation (ex: custom domain for ASE functions)
ENV_CUSTODIAN_DISABLE_SSL_CERT_VERIFICATION = 'CUSTODIAN_DISABLE_SSL_CERT_VERIFICATION'

"""
Authentication Resource
"""
RESOURCE_ACTIVE_DIRECTORY = 'https://management.core.windows.net/'
RESOURCE_STORAGE = 'https://storage.azure.com/'
RESOURCE_VAULT = 'https://vault.azure.net'
RESOURCE_GLOBAL_MGMT = 'https://management.azure.com/'

"""
Threading Variable
"""
DEFAULT_MAX_THREAD_WORKERS = 3
DEFAULT_CHUNK_SIZE = 20

"""
Custom Retry Code Variables
"""
DEFAULT_MAX_RETRY_AFTER = 30

"""
KeyVault url templates
"""
TEMPLATE_KEYVAULT_URL = 'https://{0}.vault.azure.net'

"""
Azure Functions Host Configuration
"""
FUNCTION_HOST_CONFIG = {
    "version": "2.0",
    "healthMonitor": {
        "enabled": True,
        "healthCheckInterval": "00:00:10",
        "healthCheckWindow": "00:02:00",
        "healthCheckThreshold": 6,
        "counterThreshold": 0.80
    },
    "functionTimeout": "00:10:00",
    "logging": {
        "fileLoggingMode": "always",
        "console": {
            "isEnabled": "true"
        },
        "logLevel": {
            "default": "Debug",
            "Host.Results": "Trace",
            "Function": "Trace",
            "Host.Aggregator": "Trace"
        }
    },
    "extensions": {
        "http": {
            "routePrefix": "api",
            "maxConcurrentRequests": 5,
            "maxOutstandingRequests": 30
        }
    }
}

FUNCTION_EXTENSION_BUNDLE_CONFIG = {
    "id": "Microsoft.Azure.Functions.ExtensionBundle",
    "version": "[1.*, 2.0.0)"
}

"""
Azure Storage
"""
BLOB_TYPE = 'blob'
QUEUE_TYPE = 'queue'
TABLE_TYPE = 'table'
FILE_TYPE = 'file'

RESOURCE_GROUPS_TYPE = 'resourceGroups'
