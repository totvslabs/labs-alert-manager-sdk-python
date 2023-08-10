# labs_alert_manager_client.PoliciesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_policies_delete**](PoliciesApi.md#delete_policies_delete) | **DELETE** /policies/{id} | 
[**get_policies_get**](PoliciesApi.md#get_policies_get) | **GET** /policies/{id} | 
[**get_policies_get_all**](PoliciesApi.md#get_policies_get_all) | **GET** /policies | 
[**post_policies_post**](PoliciesApi.md#post_policies_post) | **POST** /policies | 
[**put_policies_put**](PoliciesApi.md#put_policies_put) | **PUT** /policies/{id} | 


# **delete_policies_delete**
> PolicySchema delete_policies_delete(id)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_schema import PolicySchema
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
    api_instance = labs_alert_manager_client.PoliciesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_policies_delete(id)
        print("The response of PoliciesApi->delete_policies_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->delete_policies_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicySchema**](PolicySchema.md)

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

# **get_policies_get**
> PolicySchema get_policies_get(id)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_schema import PolicySchema
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
    api_instance = labs_alert_manager_client.PoliciesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_policies_get(id)
        print("The response of PoliciesApi->get_policies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->get_policies_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PolicySchema**](PolicySchema.md)

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

# **get_policies_get_all**
> PaginationSchema get_policies_get_all()



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
    api_instance = labs_alert_manager_client.PoliciesApi(api_client)

    try:
        api_response = api_instance.get_policies_get_all()
        print("The response of PoliciesApi->get_policies_get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->get_policies_get_all: %s\n" % e)
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

# **post_policies_post**
> PolicySchema post_policies_post(request_body=request_body)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_schema import PolicySchema
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
    api_instance = labs_alert_manager_client.PoliciesApi(api_client)
    request_body = labs_alert_manager_client.PolicySchema() # PolicySchema |  (optional)

    try:
        api_response = api_instance.post_policies_post(request_body=request_body)
        print("The response of PoliciesApi->post_policies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->post_policies_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**PolicySchema**](PolicySchema.md)|  | [optional] 

### Return type

[**PolicySchema**](PolicySchema.md)

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

# **put_policies_put**
> PolicySchema put_policies_put(id, request_body=request_body)



### Example

* Api Key Authentication (auth_token):
```python
import time
import os
import labs_alert_manager_client
from labs_alert_manager_client.models.policy_schema import PolicySchema
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
    api_instance = labs_alert_manager_client.PoliciesApi(api_client)
    id = 'id_example' # str | 
    request_body = labs_alert_manager_client.PolicySchema() # PolicySchema |  (optional)

    try:
        api_response = api_instance.put_policies_put(id, request_body=request_body)
        print("The response of PoliciesApi->put_policies_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->put_policies_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **request_body** | [**PolicySchema**](PolicySchema.md)|  | [optional] 

### Return type

[**PolicySchema**](PolicySchema.md)

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

