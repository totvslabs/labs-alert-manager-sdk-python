# PolicyChannelSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_uuid** | **str** | Client uuid. This is the id defined by client app | 
**config** | **object** | Policy Channel config | 
**created_at** | **datetime** |  | [optional] 
**deleted** | **bool** | Policy Channel deleted flag | 
**enabled** | **bool** | Policy Channel enabled flag | 
**id** | **str** | Id | 
**last_notification** | **datetime** |  | [optional] 
**name** | **str** | Policy Channel name | 
**type** | **str** | Policy Channel type | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from labs_alert_manager_client.models.policy_channel_schema import PolicyChannelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyChannelSchema from a JSON string
policy_channel_schema_instance = PolicyChannelSchema.from_json(json)
# print the JSON string representation of the object
print PolicyChannelSchema.to_json()

# convert the object into a dict
policy_channel_schema_dict = policy_channel_schema_instance.to_dict()
# create an instance of PolicyChannelSchema from a dict
policy_channel_schema_form_dict = policy_channel_schema.from_dict(policy_channel_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


