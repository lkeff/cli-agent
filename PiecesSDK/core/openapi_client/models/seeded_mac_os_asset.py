# coding: utf-8

"""
    Pieces Isomorphic OpenAPI

    Endpoints for Assets, Formats, Users, Asset, Format, User.

    The version of the OpenAPI document: 1.0
    Contact: tsavo@pieces.app
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.application import Application
from openapi_client.models.embedded_model_schema import EmbeddedModelSchema

class SeededMacOSAsset(BaseModel):
    """
    An Seeded Asset specific to MacOS which takes in a Value, and Application  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    application: Optional[Application] = None
    value: StrictStr = Field(..., description="The value of the text that you want to save as an asset.")
    __properties = ["schema", "application", "value"]

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
    def from_json(cls, json_str: str) -> SeededMacOSAsset:
        """Create an instance of SeededMacOSAsset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SeededMacOSAsset:
        """Create an instance of SeededMacOSAsset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SeededMacOSAsset.parse_obj(obj)

        _obj = SeededMacOSAsset.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "application": Application.from_dict(obj.get("application")) if obj.get("application") is not None else None,
            "value": obj.get("value")
        })
        return _obj


