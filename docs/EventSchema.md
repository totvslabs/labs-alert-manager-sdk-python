# EventSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_source** | **str** | Event souce | 
**client_uuid** | **str** | Client uuid. This is the id defined by client app | 
**created_at** | **datetime** |  | [optional] 
**data** | **object** | Event data | 
**event_type** | **str** | Event type | 
**id** | **str** | Id | 
**labels** | **object** | Event labels | 
**schema_version** | **str** | Event schema version. Can be used by client app to know how to parse the event | 
**severity** | **str** | Event severity | 
**status** | **str** | Event status, Received, Stored | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from labs_alert_manager_client.models.event_schema import EventSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventSchema from a JSON string
event_schema_instance = EventSchema.from_json(json)
# print the JSON string representation of the object
print EventSchema.to_json()

# convert the object into a dict
event_schema_dict = event_schema_instance.to_dict()
# create an instance of EventSchema from a dict
event_schema_form_dict = event_schema.from_dict(event_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


