# PolicySchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **List[str]** | List of channel notification | 
**client_source** | **str** | Policy Client source | 
**client_uuid** | **str** | Policy Client UUID | 
**created_at** | **datetime** |  | [optional] 
**deleted** | **bool** | Policy deleted | 
**enabled** | **bool** | Policy enabled | 
**filters** | **object** | Policy filters | 
**frequency** | **bool** | Enable alert frequency for the policy | 
**frequency_minutes** | **int** | Quantity of alert interval time | 
**frequency_occurrences** | **int** | Quantity of alert occurrencies | 
**id** | **str** | Id | 
**labels** | **object** | Policy labels | 
**name** | **str** | Policy name | 
**severity** | **str** | Policy severity | 
**type** | **str** | Policy type | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from labs_alert_manager_client.models.policy_schema import PolicySchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicySchema from a JSON string
policy_schema_instance = PolicySchema.from_json(json)
# print the JSON string representation of the object
print PolicySchema.to_json()

# convert the object into a dict
policy_schema_dict = policy_schema_instance.to_dict()
# create an instance of PolicySchema from a dict
policy_schema_form_dict = policy_schema.from_dict(policy_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


