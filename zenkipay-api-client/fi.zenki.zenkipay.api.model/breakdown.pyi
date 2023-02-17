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


class Breakdown(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Summary of shopping cart amounts.
    """


    class MetaOapg:
        required = {
            "grandTotalAmount",
            "totalItemsAmount",
            "taxesAmount",
            "currencyCodeIso3",
            "shipmentAmount",
            "subtotalAmount",
        }
        
        class properties:
            
            
            class currencyCodeIso3(
                schemas.StrSchema
            ):
                pass
            
            
            class totalItemsAmount(
                schemas.Float64Schema
            ):
                pass
            
            
            class shipmentAmount(
                schemas.Float64Schema
            ):
                pass
            
            
            class subtotalAmount(
                schemas.Float64Schema
            ):
                pass
            
            
            class taxesAmount(
                schemas.Float64Schema
            ):
                pass
            
            
            class grandTotalAmount(
                schemas.Float64Schema
            ):
                pass
            
            
            class localTaxes_amount(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'localTaxes_amount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class importCosts(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'importCosts':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class discountAmount(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'discountAmount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class additionalCharges(
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
            
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'additionalCharges':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "currencyCodeIso3": currencyCodeIso3,
                "totalItemsAmount": totalItemsAmount,
                "shipmentAmount": shipmentAmount,
                "subtotalAmount": subtotalAmount,
                "taxesAmount": taxesAmount,
                "grandTotalAmount": grandTotalAmount,
                "localTaxes_amount": localTaxes_amount,
                "importCosts": importCosts,
                "discountAmount": discountAmount,
                "additionalCharges": additionalCharges,
            }
    
    grandTotalAmount: MetaOapg.properties.grandTotalAmount
    totalItemsAmount: MetaOapg.properties.totalItemsAmount
    taxesAmount: MetaOapg.properties.taxesAmount
    currencyCodeIso3: MetaOapg.properties.currencyCodeIso3
    shipmentAmount: MetaOapg.properties.shipmentAmount
    subtotalAmount: MetaOapg.properties.subtotalAmount
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCodeIso3"]) -> MetaOapg.properties.currencyCodeIso3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalItemsAmount"]) -> MetaOapg.properties.totalItemsAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipmentAmount"]) -> MetaOapg.properties.shipmentAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subtotalAmount"]) -> MetaOapg.properties.subtotalAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxesAmount"]) -> MetaOapg.properties.taxesAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grandTotalAmount"]) -> MetaOapg.properties.grandTotalAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["localTaxes_amount"]) -> MetaOapg.properties.localTaxes_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["importCosts"]) -> MetaOapg.properties.importCosts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discountAmount"]) -> MetaOapg.properties.discountAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalCharges"]) -> MetaOapg.properties.additionalCharges: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currencyCodeIso3", "totalItemsAmount", "shipmentAmount", "subtotalAmount", "taxesAmount", "grandTotalAmount", "localTaxes_amount", "importCosts", "discountAmount", "additionalCharges", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCodeIso3"]) -> MetaOapg.properties.currencyCodeIso3: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalItemsAmount"]) -> MetaOapg.properties.totalItemsAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipmentAmount"]) -> MetaOapg.properties.shipmentAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subtotalAmount"]) -> MetaOapg.properties.subtotalAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxesAmount"]) -> MetaOapg.properties.taxesAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grandTotalAmount"]) -> MetaOapg.properties.grandTotalAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["localTaxes_amount"]) -> typing.Union[MetaOapg.properties.localTaxes_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["importCosts"]) -> typing.Union[MetaOapg.properties.importCosts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discountAmount"]) -> typing.Union[MetaOapg.properties.discountAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalCharges"]) -> typing.Union[MetaOapg.properties.additionalCharges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currencyCodeIso3", "totalItemsAmount", "shipmentAmount", "subtotalAmount", "taxesAmount", "grandTotalAmount", "localTaxes_amount", "importCosts", "discountAmount", "additionalCharges", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        grandTotalAmount: typing.Union[MetaOapg.properties.grandTotalAmount, decimal.Decimal, int, float, ],
        totalItemsAmount: typing.Union[MetaOapg.properties.totalItemsAmount, decimal.Decimal, int, float, ],
        taxesAmount: typing.Union[MetaOapg.properties.taxesAmount, decimal.Decimal, int, float, ],
        currencyCodeIso3: typing.Union[MetaOapg.properties.currencyCodeIso3, str, ],
        shipmentAmount: typing.Union[MetaOapg.properties.shipmentAmount, decimal.Decimal, int, float, ],
        subtotalAmount: typing.Union[MetaOapg.properties.subtotalAmount, decimal.Decimal, int, float, ],
        localTaxes_amount: typing.Union[MetaOapg.properties.localTaxes_amount, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        importCosts: typing.Union[MetaOapg.properties.importCosts, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        discountAmount: typing.Union[MetaOapg.properties.discountAmount, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        additionalCharges: typing.Union[MetaOapg.properties.additionalCharges, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Breakdown':
        return super().__new__(
            cls,
            *args,
            grandTotalAmount=grandTotalAmount,
            totalItemsAmount=totalItemsAmount,
            taxesAmount=taxesAmount,
            currencyCodeIso3=currencyCodeIso3,
            shipmentAmount=shipmentAmount,
            subtotalAmount=subtotalAmount,
            localTaxes_amount=localTaxes_amount,
            importCosts=importCosts,
            discountAmount=discountAmount,
            additionalCharges=additionalCharges,
            _configuration=_configuration,
            **kwargs,
        )
