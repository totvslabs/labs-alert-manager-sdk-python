# NotificationSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_uuid** | **str** | Notification Client UUID | 
**created_at** | **datetime** |  | [optional] 
**events** | **List[str]** | List of notification events | [optional] 
**first_event** | **datetime** |  | [optional] 
**id** | **str** | Id | 
**retries** | **int** | Quantity notification retries | [optional] 
**status** | **str** | Notification status | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from labs_alert_manager_client.models.notification_schema import NotificationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSchema from a JSON string
notification_schema_instance = NotificationSchema.from_json(json)
# print the JSON string representation of the object
print NotificationSchema.to_json()

# convert the object into a dict
notification_schema_dict = notification_schema_instance.to_dict()
# create an instance of NotificationSchema from a dict
notification_schema_form_dict = notification_schema.from_dict(notification_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


