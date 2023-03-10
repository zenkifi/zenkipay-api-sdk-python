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


class Tracking(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "zenkiTrackingId",
            "courierType",
        }
        
        class properties:
            
            
            class zenkiTrackingId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
            class courierType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "EXTERNAL": "EXTERNAL",
                        "INTERNAL": "INTERNAL",
                    }
                
                @schemas.classproperty
                def EXTERNAL(cls):
                    return cls("EXTERNAL")
                
                @schemas.classproperty
                def INTERNAL(cls):
                    return cls("INTERNAL")
            
            
            class trackingId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'trackingId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class courierName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'courierName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class externalCourier(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "countryCodeIso2",
                        "key",
                    }
                    
                    class properties:
                        
                        
                        class key(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 30
                        
                        
                        class countryCodeIso2(
                            schemas.StrSchema
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 5
                        
                        
                        class url(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 255
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'url':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class name(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 50
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'name':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class nameZhCn(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 50
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'nameZhCn':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        
                        
                        class nameZhHk(
                            schemas.StrBase,
                            schemas.NoneBase,
                            schemas.Schema,
                            schemas.NoneStrMixin
                        ):
                        
                        
                            class MetaOapg:
                                max_length = 50
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[None, str, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'nameZhHk':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                )
                        __annotations__ = {
                            "key": key,
                            "countryCodeIso2": countryCodeIso2,
                            "url": url,
                            "name": name,
                            "nameZhCn": nameZhCn,
                            "nameZhHk": nameZhHk,
                        }
                
                countryCodeIso2: MetaOapg.properties.countryCodeIso2
                key: MetaOapg.properties.key
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["countryCodeIso2"]) -> MetaOapg.properties.countryCodeIso2: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["nameZhCn"]) -> MetaOapg.properties.nameZhCn: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["nameZhHk"]) -> MetaOapg.properties.nameZhHk: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "countryCodeIso2", "url", "name", "nameZhCn", "nameZhHk", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["countryCodeIso2"]) -> MetaOapg.properties.countryCodeIso2: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["nameZhCn"]) -> typing.Union[MetaOapg.properties.nameZhCn, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["nameZhHk"]) -> typing.Union[MetaOapg.properties.nameZhHk, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "countryCodeIso2", "url", "name", "nameZhCn", "nameZhHk", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    countryCodeIso2: typing.Union[MetaOapg.properties.countryCodeIso2, str, ],
                    key: typing.Union[MetaOapg.properties.key, str, ],
                    url: typing.Union[MetaOapg.properties.url, None, str, schemas.Unset] = schemas.unset,
                    name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
                    nameZhCn: typing.Union[MetaOapg.properties.nameZhCn, None, str, schemas.Unset] = schemas.unset,
                    nameZhHk: typing.Union[MetaOapg.properties.nameZhHk, None, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'externalCourier':
                    return super().__new__(
                        cls,
                        *_args,
                        countryCodeIso2=countryCodeIso2,
                        key=key,
                        url=url,
                        name=name,
                        nameZhCn=nameZhCn,
                        nameZhHk=nameZhHk,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "zenkiTrackingId": zenkiTrackingId,
                "courierType": courierType,
                "trackingId": trackingId,
                "courierName": courierName,
                "externalCourier": externalCourier,
            }
    
    zenkiTrackingId: MetaOapg.properties.zenkiTrackingId
    courierType: MetaOapg.properties.courierType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zenkiTrackingId"]) -> MetaOapg.properties.zenkiTrackingId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courierType"]) -> MetaOapg.properties.courierType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackingId"]) -> MetaOapg.properties.trackingId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["courierName"]) -> MetaOapg.properties.courierName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalCourier"]) -> MetaOapg.properties.externalCourier: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["zenkiTrackingId", "courierType", "trackingId", "courierName", "externalCourier", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zenkiTrackingId"]) -> MetaOapg.properties.zenkiTrackingId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courierType"]) -> MetaOapg.properties.courierType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackingId"]) -> typing.Union[MetaOapg.properties.trackingId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["courierName"]) -> typing.Union[MetaOapg.properties.courierName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalCourier"]) -> typing.Union[MetaOapg.properties.externalCourier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["zenkiTrackingId", "courierType", "trackingId", "courierName", "externalCourier", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        zenkiTrackingId: typing.Union[MetaOapg.properties.zenkiTrackingId, str, ],
        courierType: typing.Union[MetaOapg.properties.courierType, str, ],
        trackingId: typing.Union[MetaOapg.properties.trackingId, None, str, schemas.Unset] = schemas.unset,
        courierName: typing.Union[MetaOapg.properties.courierName, None, str, schemas.Unset] = schemas.unset,
        externalCourier: typing.Union[MetaOapg.properties.externalCourier, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Tracking':
        return super().__new__(
            cls,
            *_args,
            zenkiTrackingId=zenkiTrackingId,
            courierType=courierType,
            trackingId=trackingId,
            courierName=courierName,
            externalCourier=externalCourier,
            _configuration=_configuration,
            **kwargs,
        )
