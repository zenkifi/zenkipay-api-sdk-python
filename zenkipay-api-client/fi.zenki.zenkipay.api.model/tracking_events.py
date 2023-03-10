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


class TrackingEvents(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List of events recorded in the process of delivering the package to the buyer.
    """


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "description",
                    "location",
                    "status",
                }
                
                class properties:
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "TRANSIT": "TRANSIT",
                                "DELIVERY": "DELIVERY",
                                "AVAILABLE_FOR_PICKUP": "AVAILABLE_FOR_PICKUP",
                                "CANCELED": "CANCELED",
                                "FAILED": "FAILED",
                            }
                        
                        @schemas.classproperty
                        def TRANSIT(cls):
                            return cls("TRANSIT")
                        
                        @schemas.classproperty
                        def DELIVERY(cls):
                            return cls("DELIVERY")
                        
                        @schemas.classproperty
                        def AVAILABLE_FOR_PICKUP(cls):
                            return cls("AVAILABLE_FOR_PICKUP")
                        
                        @schemas.classproperty
                        def CANCELED(cls):
                            return cls("CANCELED")
                        
                        @schemas.classproperty
                        def FAILED(cls):
                            return cls("FAILED")
                    
                    
                    class location(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 255
                    
                    
                    class description(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 255
                    
                    
                    class createdAt(
                        schemas.Int64Schema
                    ):
                    
                    
                        class MetaOapg:
                            format = 'int64'
                            inclusive_minimum = 0
                    __annotations__ = {
                        "status": status,
                        "location": location,
                        "description": description,
                        "createdAt": createdAt,
                    }
            
            description: MetaOapg.properties.description
            location: MetaOapg.properties.location
            status: MetaOapg.properties.status
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "location", "description", "createdAt", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "location", "description", "createdAt", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                description: typing.Union[MetaOapg.properties.description, str, ],
                location: typing.Union[MetaOapg.properties.location, str, ],
                status: typing.Union[MetaOapg.properties.status, str, ],
                createdAt: typing.Union[MetaOapg.properties.createdAt, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *_args,
                    description=description,
                    location=location,
                    status=status,
                    createdAt=createdAt,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TrackingEvents':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
