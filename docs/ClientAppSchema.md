# ClientAppSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**contract** | **str** |  | [optional] 
**labels** | **object** |  | [optional] 
**id** | **str** |  | 
**token** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**url** | **str** |  | [optional] 
**billing_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.client_app_schema import ClientAppSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAppSchema from a JSON string
client_app_schema_instance = ClientAppSchema.from_json(json)
# print the JSON string representation of the object
print ClientAppSchema.to_json()

# convert the object into a dict
client_app_schema_dict = client_app_schema_instance.to_dict()
# create an instance of ClientAppSchema from a dict
client_app_schema_form_dict = client_app_schema.from_dict(client_app_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


