# labs_alert_manager_client.DocsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_swagger_json**](DocsApi.md#get_swagger_json) | **GET** /docs/swagger.json | 
[**get_swagger_yml**](DocsApi.md#get_swagger_yml) | **GET** /docs/swagger.yml | 


# **get_swagger_json**
> get_swagger_json()



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = labs_alert_manager_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: auth_token
configuration.api_key['auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with labs_alert_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labs_alert_manager_client.DocsApi(api_client)

    try:
        api_instance.get_swagger_json()
    except Exception as e:
        print("Exception when calling DocsApi->get_swagger_json: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swagger_yml**
> get_swagger_yml()



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = labs_alert_manager_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: auth_token
configuration.api_key['auth_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with labs_alert_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = labs_alert_manager_client.DocsApi(api_client)

    try:
        api_instance.get_swagger_yml()
    except Exception as e:
        print("Exception when calling DocsApi->get_swagger_yml: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

