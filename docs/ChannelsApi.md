# labs_alert_manager_client.ChannelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_policy_channels_delete**](ChannelsApi.md#delete_policy_channels_delete) | **DELETE** /channels/{id} | 
[**get_policy_channels_get**](ChannelsApi.md#get_policy_channels_get) | **GET** /channels/{id} | 
[**get_policy_channels_get_all**](ChannelsApi.md#get_policy_channels_get_all) | **GET** /channels | 
[**post_policy_channels_post**](ChannelsApi.md#post_policy_channels_post) | **POST** /channels | 
[**post_policy_channels_test**](ChannelsApi.md#post_policy_channels_test) | **POST** /channels/test | 
[**put_policy_channels_put**](ChannelsApi.md#put_policy_channels_put) | **PUT** /channels/{id} | 


# **delete_policy_channels_delete**
> PolicyChannelSchema delete_policy_channels_delete(id)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_channel_schema import PolicyChannelSchema
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
    api_instance = labs_alert_manager_client.ChannelsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_policy_channels_delete(id)
        print("The response of ChannelsApi->delete_policy_channels_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->delete_policy_channels_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicyChannelSchema**](PolicyChannelSchema.md)

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

# **get_policy_channels_get**
> PolicyChannelSchema get_policy_channels_get(id)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_channel_schema import PolicyChannelSchema
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
    api_instance = labs_alert_manager_client.ChannelsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_policy_channels_get(id)
        print("The response of ChannelsApi->get_policy_channels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_policy_channels_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicyChannelSchema**](PolicyChannelSchema.md)

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

# **get_policy_channels_get_all**
> PaginationSchema get_policy_channels_get_all()



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
    api_instance = labs_alert_manager_client.ChannelsApi(api_client)

    try:
        api_response = api_instance.get_policy_channels_get_all()
        print("The response of ChannelsApi->get_policy_channels_get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->get_policy_channels_get_all: %s\n" % e)
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

# **post_policy_channels_post**
> PolicyChannelSchema post_policy_channels_post(request_body=request_body)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_channel_schema import PolicyChannelSchema
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
    api_instance = labs_alert_manager_client.ChannelsApi(api_client)
    request_body = labs_alert_manager_client.PolicyChannelSchema() # PolicyChannelSchema |  (optional)

    try:
        api_response = api_instance.post_policy_channels_post(request_body=request_body)
        print("The response of ChannelsApi->post_policy_channels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->post_policy_channels_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**PolicyChannelSchema**](PolicyChannelSchema.md)|  | [optional] 

### Return type

[**PolicyChannelSchema**](PolicyChannelSchema.md)

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

# **post_policy_channels_test**
> PolicyChannelSchema post_policy_channels_test(request_body=request_body)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_channel_schema import PolicyChannelSchema
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
    api_instance = labs_alert_manager_client.ChannelsApi(api_client)
    request_body = labs_alert_manager_client.PolicyChannelSchema() # PolicyChannelSchema |  (optional)

    try:
        api_response = api_instance.post_policy_channels_test(request_body=request_body)
        print("The response of ChannelsApi->post_policy_channels_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->post_policy_channels_test: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**PolicyChannelSchema**](PolicyChannelSchema.md)|  | [optional] 

### Return type

[**PolicyChannelSchema**](PolicyChannelSchema.md)

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

# **put_policy_channels_put**
> PolicyChannelSchema put_policy_channels_put(id, request_body=request_body)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_channel_schema import PolicyChannelSchema
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
    api_instance = labs_alert_manager_client.ChannelsApi(api_client)
    id = 'id_example' # str | 
    request_body = labs_alert_manager_client.PolicyChannelSchema() # PolicyChannelSchema |  (optional)

    try:
        api_response = api_instance.put_policy_channels_put(id, request_body=request_body)
        print("The response of ChannelsApi->put_policy_channels_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChannelsApi->put_policy_channels_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**PolicyChannelSchema**](PolicyChannelSchema.md)|  | [optional] 

### Return type

[**PolicyChannelSchema**](PolicyChannelSchema.md)

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

