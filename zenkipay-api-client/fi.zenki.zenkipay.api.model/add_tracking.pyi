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


class AddTracking(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "courierType",
        }
        
        class properties:
            
            
            class courierType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("EXTERNAL")
                
                @schemas.classproperty
                def INTERNAL(cls):
                    return cls("INTERNAL")
            
            
            class trackingId(
                schemas.StrSchema
            ):
                pass
            
            
            class courierName(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "courierType": courierType,
                "trackingId": trackingId,
                "courierName": courierName,
            }
    
    courierType: MetaOapg.properties.courierType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courierType"]) -> MetaOapg.properties.courierType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackingId"]) -> MetaOapg.properties.trackingId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courierName"]) -> MetaOapg.properties.courierName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["courierType", "trackingId", "courierName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courierType"]) -> MetaOapg.properties.courierType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackingId"]) -> typing.Union[MetaOapg.properties.trackingId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courierName"]) -> typing.Union[MetaOapg.properties.courierName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["courierType", "trackingId", "courierName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        courierType: typing.Union[MetaOapg.properties.courierType, str, ],
        trackingId: typing.Union[MetaOapg.properties.trackingId, str, schemas.Unset] = schemas.unset,
        courierName: typing.Union[MetaOapg.properties.courierName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddTracking':
        return super().__new__(
            cls,
            *_args,
            courierType=courierType,
            trackingId=trackingId,
            courierName=courierName,
            _configuration=_configuration,
            **kwargs,
        )
