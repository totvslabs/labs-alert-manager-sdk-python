# coding: utf-8

"""
    alertmanager

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class ClientAppSchema(BaseModel):
    """
    ClientAppSchema
    """
    updated_at: Optional[datetime] = None
    name: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    contract: Optional[StrictStr] = None
    labels: Optional[Dict[str, Any]] = None
    id: StrictStr = Field(...)
    token: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    billing_id: Optional[StrictStr] = None
    __properties = ["updated_at", "name", "deleted", "contract", "labels", "id", "token", "created_at", "url", "billing_id"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ClientAppSchema:
        """Create an instance of ClientAppSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if labels (nullable) is None
        # and __fields_set__ contains the field
        if self.labels is None and "labels" in self.__fields_set__:
            _dict['labels'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientAppSchema:
        """Create an instance of ClientAppSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientAppSchema.parse_obj(obj)

        _obj = ClientAppSchema.parse_obj({
            "updated_at": obj.get("updated_at"),
            "name": obj.get("name"),
            "deleted": obj.get("deleted"),
            "contract": obj.get("contract"),
            "labels": obj.get("labels"),
            "id": obj.get("id"),
            "token": obj.get("token"),
            "created_at": obj.get("created_at"),
            "url": obj.get("url"),
            "billing_id": obj.get("billing_id")
        })
        return _obj

