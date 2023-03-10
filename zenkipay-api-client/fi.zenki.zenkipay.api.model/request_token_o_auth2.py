# coding: utf-8

"""
    Zenkipay API

    Definition of technical specification of the product; Zenkipay is a gateway cryptocurrency payment system that allows merchant's to receive payments on their e-commerce portals. Unlike other platforms, Zenkipay ensures customer satisfaction through its payment process. guarantee deposit (delivered product and expected quality) to settle payment to the merchant, thus avoiding the loss of client assets due to online scams.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@zenki.fi
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zenkipay-api-client import schemas  # noqa: F401


class RequestTokenOAuth2(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "clientId",
            "clientSecret",
            "grantType",
        }
        
        class properties:
            
            
            class clientId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
            class clientSecret(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
            class grantType(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 30
            __annotations__ = {
                "clientId": clientId,
                "clientSecret": clientSecret,
                "grantType": grantType,
            }
    
    clientId: MetaOapg.properties.clientId
    clientSecret: MetaOapg.properties.clientSecret
    grantType: MetaOapg.properties.grantType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientSecret"]) -> MetaOapg.properties.clientSecret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grantType"]) -> MetaOapg.properties.grantType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clientId", "clientSecret", "grantType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientSecret"]) -> MetaOapg.properties.clientSecret: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grantType"]) -> MetaOapg.properties.grantType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clientId", "clientSecret", "grantType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        clientId: typing.Union[MetaOapg.properties.clientId, str, ],
        clientSecret: typing.Union[MetaOapg.properties.clientSecret, str, ],
        grantType: typing.Union[MetaOapg.properties.grantType, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequestTokenOAuth2':
        return super().__new__(
            cls,
            *_args,
            clientId=clientId,
            clientSecret=clientSecret,
            grantType=grantType,
            _configuration=_configuration,
            **kwargs,
        )
