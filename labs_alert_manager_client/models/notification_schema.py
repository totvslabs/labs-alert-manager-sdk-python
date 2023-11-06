# coding: utf-8

"""
    alertmanager

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NotificationSchema(BaseModel):
    """
    NotificationSchema
    """ # noqa: E501
    client_uuid: StrictStr = Field(description="Notification Client UUID")
    created_at: Optional[datetime] = None
    events: Optional[List[StrictStr]] = Field(default=None, description="List of notification events")
    first_event: Optional[datetime] = None
    id: StrictStr = Field(description="Id")
    retries: Optional[StrictInt] = Field(default=None, description="Quantity notification retries")
    status: Annotated[str, Field(strict=True, max_length=10)] = Field(description="Notification status")
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["client_uuid", "created_at", "events", "first_event", "id", "retries", "status", "updated_at"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Queued', 'Processing', 'Failed', 'Success'):
            raise ValueError("must be one of enum values ('Queued', 'Processing', 'Failed', 'Success')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NotificationSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if events (nullable) is None
        # and model_fields_set contains the field
        if self.events is None and "events" in self.model_fields_set:
            _dict['events'] = None

        # set to None if first_event (nullable) is None
        # and model_fields_set contains the field
        if self.first_event is None and "first_event" in self.model_fields_set:
            _dict['first_event'] = None

        # set to None if retries (nullable) is None
        # and model_fields_set contains the field
        if self.retries is None and "retries" in self.model_fields_set:
            _dict['retries'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NotificationSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "client_uuid": obj.get("client_uuid"),
            "created_at": obj.get("created_at"),
            "events": obj.get("events"),
            "first_event": obj.get("first_event"),
            "id": obj.get("id"),
            "retries": obj.get("retries"),
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


