# PaginationSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**page_size** | **int** |  | 
**rows** | **List[object]** |  | 
**total_rows** | **int** |  | 

## Example

```python
from labs_alert_manager_client.models.pagination_schema import PaginationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationSchema from a JSON string
pagination_schema_instance = PaginationSchema.from_json(json)
# print the JSON string representation of the object
print PaginationSchema.to_json()

# convert the object into a dict
pagination_schema_dict = pagination_schema_instance.to_dict()
# create an instance of PaginationSchema from a dict
pagination_schema_form_dict = pagination_schema.from_dict(pagination_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


