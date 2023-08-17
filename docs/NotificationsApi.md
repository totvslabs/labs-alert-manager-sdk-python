# labs_alert_manager_client.NotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notification_log_get**](NotificationsApi.md#get_notification_log_get) | **GET** /notifications/{id} | 
[**get_notification_log_get_all**](NotificationsApi.md#get_notification_log_get_all) | **GET** /notifications | 
[**post_notification_log_resend**](NotificationsApi.md#post_notification_log_resend) | **POST** /notifications/{id}/resend | 


# **get_notification_log_get**
> NotificationSchema get_notification_log_get(id)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.notification_schema import NotificationSchema
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
    api_instance = labs_alert_manager_client.NotificationsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_notification_log_get(id)
        print("The response of NotificationsApi->get_notification_log_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_log_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NotificationSchema**](NotificationSchema.md)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_log_get_all**
> PaginationSchema get_notification_log_get_all()



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.pagination_schema import PaginationSchema
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
    api_instance = labs_alert_manager_client.NotificationsApi(api_client)

    try:
        api_response = api_instance.get_notification_log_get_all()
        print("The response of NotificationsApi->get_notification_log_get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->get_notification_log_get_all: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PaginationSchema**](PaginationSchema.md)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_notification_log_resend**
> NotificationSchema post_notification_log_resend(id)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.notification_schema import NotificationSchema
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
    api_instance = labs_alert_manager_client.NotificationsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.post_notification_log_resend(id)
        print("The response of NotificationsApi->post_notification_log_resend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->post_notification_log_resend: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**NotificationSchema**](NotificationSchema.md)

### Authorization

[auth_token](../README.md#auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

