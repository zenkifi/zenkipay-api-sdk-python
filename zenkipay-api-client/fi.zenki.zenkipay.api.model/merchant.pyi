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


class Merchant(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Merchant information.
    """


    class MetaOapg:
        required = {
            "cryptoLovePercentage",
            "escrowConfig",
            "integrationConfig",
            "merchantInfo",
            "cryptoCurrencies",
        }
        
        class properties:
            
            
            class merchantInfo(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "kycStatus",
                        "accountType",
                        "integrationStatus",
                        "commercialName",
                    }
                    
                    class properties:
                        
                        
                        class commercialName(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class legalName(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class accountType(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def PERSONAL(cls):
                                return cls("PERSONAL")
                            
                            @schemas.classproperty
                            def ENTITY(cls):
                                return cls("ENTITY")
                        
                        
                        class kycStatus(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def PENDING(cls):
                                return cls("PENDING")
                            
                            @schemas.classproperty
                            def APPROVED(cls):
                                return cls("APPROVED")
                            
                            @schemas.classproperty
                            def REQUEST_INFO(cls):
                                return cls("REQUEST_INFO")
                            
                            @schemas.classproperty
                            def REJECTED(cls):
                                return cls("REJECTED")
                        
                        
                        class integrationStatus(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def PENDING(cls):
                                return cls("PENDING")
                            
                            @schemas.classproperty
                            def COMPLETED(cls):
                                return cls("COMPLETED")
                        __annotations__ = {
                            "commercialName": commercialName,
                            "legalName": legalName,
                            "accountType": accountType,
                            "kycStatus": kycStatus,
                            "integrationStatus": integrationStatus,
                        }
                
                kycStatus: MetaOapg.properties.kycStatus
                accountType: MetaOapg.properties.accountType
                integrationStatus: MetaOapg.properties.integrationStatus
                commercialName: MetaOapg.properties.commercialName
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["commercialName"]) -> MetaOapg.properties.commercialName: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["legalName"]) -> MetaOapg.properties.legalName: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["kycStatus"]) -> MetaOapg.properties.kycStatus: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["integrationStatus"]) -> MetaOapg.properties.integrationStatus: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["commercialName", "legalName", "accountType", "kycStatus", "integrationStatus", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["commercialName"]) -> MetaOapg.properties.commercialName: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["legalName"]) -> typing.Union[MetaOapg.properties.legalName, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["kycStatus"]) -> MetaOapg.properties.kycStatus: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["integrationStatus"]) -> MetaOapg.properties.integrationStatus: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["commercialName", "legalName", "accountType", "kycStatus", "integrationStatus", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    kycStatus: typing.Union[MetaOapg.properties.kycStatus, str, ],
                    accountType: typing.Union[MetaOapg.properties.accountType, str, ],
                    integrationStatus: typing.Union[MetaOapg.properties.integrationStatus, str, ],
                    commercialName: typing.Union[MetaOapg.properties.commercialName, str, ],
                    legalName: typing.Union[MetaOapg.properties.legalName, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'merchantInfo':
                    return super().__new__(
                        cls,
                        *_args,
                        kycStatus=kycStatus,
                        accountType=accountType,
                        integrationStatus=integrationStatus,
                        commercialName=commercialName,
                        legalName=legalName,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class integrationConfig(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "plugins",
                    }
                    
                    class properties:
                        
                        
                        class plugins(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                
                                class items(
                                    schemas.DictSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        required = {
                                            "clientId",
                                            "name",
                                        }
                                        
                                        class properties:
                                            
                                            
                                            class name(
                                                schemas.EnumBase,
                                                schemas.StrSchema
                                            ):
                                                
                                                @schemas.classproperty
                                                def SCRIPT(cls):
                                                    return cls("SCRIPT")
                                                
                                                @schemas.classproperty
                                                def WOOCOMMERCE(cls):
                                                    return cls("WOOCOMMERCE")
                                                
                                                @schemas.classproperty
                                                def BIGCOMMERCE(cls):
                                                    return cls("BIGCOMMERCE")
                                                
                                                @schemas.classproperty
                                                def MAGENTO(cls):
                                                    return cls("MAGENTO")
                                                
                                                @schemas.classproperty
                                                def ECWID(cls):
                                                    return cls("ECWID")
                                                
                                                @schemas.classproperty
                                                def SHOPIFY(cls):
                                                    return cls("SHOPIFY")
                                                
                                                @schemas.classproperty
                                                def VTEX(cls):
                                                    return cls("VTEX")
                                                
                                                @schemas.classproperty
                                                def ANGULAR(cls):
                                                    return cls("ANGULAR")
                                                
                                                @schemas.classproperty
                                                def REACT(cls):
                                                    return cls("REACT")
                                                
                                                @schemas.classproperty
                                                def VUEJS(cls):
                                                    return cls("VUEJS")
                                                
                                                @schemas.classproperty
                                                def PRESTASHOP(cls):
                                                    return cls("PRESTASHOP")
                                            
                                            
                                            class clientId(
                                                schemas.StrSchema
                                            ):
                                                pass
                                            __annotations__ = {
                                                "name": name,
                                                "clientId": clientId,
                                            }
                                    
                                    clientId: MetaOapg.properties.clientId
                                    name: MetaOapg.properties.name
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
                                    
                                    @typing.overload
                                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                    
                                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "clientId", ], str]):
                                        # dict_instance[name] accessor
                                        return super().__getitem__(name)
                                    
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
                                    
                                    @typing.overload
                                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                    
                                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "clientId", ], str]):
                                        return super().get_item_oapg(name)
                                    
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, ],
                                        clientId: typing.Union[MetaOapg.properties.clientId, str, ],
                                        name: typing.Union[MetaOapg.properties.name, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'items':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            clientId=clientId,
                                            name=name,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'plugins':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "plugins": plugins,
                        }
                
                plugins: MetaOapg.properties.plugins
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["plugins"]) -> MetaOapg.properties.plugins: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["plugins", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["plugins"]) -> MetaOapg.properties.plugins: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["plugins", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    plugins: typing.Union[MetaOapg.properties.plugins, list, tuple, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'integrationConfig':
                    return super().__new__(
                        cls,
                        *_args,
                        plugins=plugins,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class cryptoLovePercentage(
                schemas.Float64Schema
            ):
                pass
            
            
            class escrowConfig(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "amount",
                        "blockchain",
                        "currency",
                    }
                    
                    class properties:
                        
                        
                        class orderType(
                            schemas.EnumBase,
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def WITH_CARRIER(cls):
                                return cls("WITH_CARRIER")
                            
                            @schemas.classproperty
                            def WITHOUT_CARRIER(cls):
                                return cls("WITHOUT_CARRIER")
                            
                            @schemas.classproperty
                            def MIXED(cls):
                                return cls("MIXED")
                        
                        
                        class shopperNotification(
                            schemas.Int64Schema
                        ):
                            pass
                        
                        
                        class timeWaitToApproval(
                            schemas.Int64Schema
                        ):
                            pass
                        __annotations__ = {
                            "orderType": orderType,
                            "shopperNotification": shopperNotification,
                            "timeWaitToApproval": timeWaitToApproval,
                        }
                
                amount: schemas.AnyTypeSchema
                blockchain: schemas.AnyTypeSchema
                currency: schemas.AnyTypeSchema
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["orderType"]) -> MetaOapg.properties.orderType: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["shopperNotification"]) -> MetaOapg.properties.shopperNotification: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["timeWaitToApproval"]) -> MetaOapg.properties.timeWaitToApproval: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["orderType", "shopperNotification", "timeWaitToApproval", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["orderType"]) -> typing.Union[MetaOapg.properties.orderType, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["shopperNotification"]) -> typing.Union[MetaOapg.properties.shopperNotification, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["timeWaitToApproval"]) -> typing.Union[MetaOapg.properties.timeWaitToApproval, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["orderType", "shopperNotification", "timeWaitToApproval", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    amount: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    blockchain: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    currency: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    orderType: typing.Union[MetaOapg.properties.orderType, str, schemas.Unset] = schemas.unset,
                    shopperNotification: typing.Union[MetaOapg.properties.shopperNotification, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    timeWaitToApproval: typing.Union[MetaOapg.properties.timeWaitToApproval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'escrowConfig':
                    return super().__new__(
                        cls,
                        *_args,
                        amount=amount,
                        blockchain=blockchain,
                        currency=currency,
                        orderType=orderType,
                        shopperNotification=shopperNotification,
                        timeWaitToApproval=timeWaitToApproval,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class cryptoAssets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "active",
                                "currency",
                            }
                            
                            class properties:
                                
                                
                                class currency(
                                    schemas.StrSchema
                                ):
                                    pass
                                active = schemas.BoolSchema
                                __annotations__ = {
                                    "currency": currency,
                                    "active": active,
                                }
                        
                        active: MetaOapg.properties.active
                        currency: MetaOapg.properties.currency
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency", "active", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency", "active", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            active: typing.Union[MetaOapg.properties.active, bool, ],
                            currency: typing.Union[MetaOapg.properties.currency, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                active=active,
                                currency=currency,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cryptoAssets':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "merchantInfo": merchantInfo,
                "integrationConfig": integrationConfig,
                "cryptoLovePercentage": cryptoLovePercentage,
                "escrowConfig": escrowConfig,
                "cryptoAssets": cryptoAssets,
            }
    
    cryptoLovePercentage: MetaOapg.properties.cryptoLovePercentage
    escrowConfig: MetaOapg.properties.escrowConfig
    integrationConfig: MetaOapg.properties.integrationConfig
    merchantInfo: MetaOapg.properties.merchantInfo
    cryptoCurrencies: schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantInfo"]) -> MetaOapg.properties.merchantInfo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integrationConfig"]) -> MetaOapg.properties.integrationConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cryptoLovePercentage"]) -> MetaOapg.properties.cryptoLovePercentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["escrowConfig"]) -> MetaOapg.properties.escrowConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cryptoAssets"]) -> MetaOapg.properties.cryptoAssets: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["merchantInfo", "integrationConfig", "cryptoLovePercentage", "escrowConfig", "cryptoAssets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantInfo"]) -> MetaOapg.properties.merchantInfo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["integrationConfig"]) -> MetaOapg.properties.integrationConfig: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cryptoLovePercentage"]) -> MetaOapg.properties.cryptoLovePercentage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["escrowConfig"]) -> MetaOapg.properties.escrowConfig: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cryptoAssets"]) -> typing.Union[MetaOapg.properties.cryptoAssets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["merchantInfo", "integrationConfig", "cryptoLovePercentage", "escrowConfig", "cryptoAssets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cryptoLovePercentage: typing.Union[MetaOapg.properties.cryptoLovePercentage, decimal.Decimal, int, float, ],
        escrowConfig: typing.Union[MetaOapg.properties.escrowConfig, dict, frozendict.frozendict, ],
        integrationConfig: typing.Union[MetaOapg.properties.integrationConfig, dict, frozendict.frozendict, ],
        merchantInfo: typing.Union[MetaOapg.properties.merchantInfo, dict, frozendict.frozendict, ],
        cryptoCurrencies: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        cryptoAssets: typing.Union[MetaOapg.properties.cryptoAssets, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Merchant':
        return super().__new__(
            cls,
            *_args,
            cryptoLovePercentage=cryptoLovePercentage,
            escrowConfig=escrowConfig,
            integrationConfig=integrationConfig,
            merchantInfo=merchantInfo,
            cryptoCurrencies=cryptoCurrencies,
            cryptoAssets=cryptoAssets,
            _configuration=_configuration,
            **kwargs,
        )
