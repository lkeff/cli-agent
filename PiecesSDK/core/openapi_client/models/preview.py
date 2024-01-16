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
from pydantic import BaseModel, Field
from openapi_client.models.embedded_model_schema import EmbeddedModelSchema
from openapi_client.models.referenced_format import ReferencedFormat

class Preview(BaseModel):
    """
    This is a preview Model that will hold references to at minimum the base preview. which can be potentiall a base image, or also base text/code and then the oveylay is another format(image/text/code) that is 'overlayed' ontop of the base format.  # noqa: E501
    """
    var_schema: Optional[EmbeddedModelSchema] = Field(None, alias="schema")
    base: ReferencedFormat = Field(...)
    overlay: Optional[ReferencedFormat] = None
    __properties = ["schema", "base", "overlay"]

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
    def from_json(cls, json_str: str) -> Preview:
        """Create an instance of Preview from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of base
        if self.base:
            _dict['base'] = self.base.to_dict()
        # override the default output from pydantic by calling `to_dict()` of overlay
        if self.overlay:
            _dict['overlay'] = self.overlay.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Preview:
        """Create an instance of Preview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Preview.parse_obj(obj)

        _obj = Preview.parse_obj({
            "var_schema": EmbeddedModelSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "base": ReferencedFormat.from_dict(obj.get("base")) if obj.get("base") is not None else None,
            "overlay": ReferencedFormat.from_dict(obj.get("overlay")) if obj.get("overlay") is not None else None
        })
        return _obj


