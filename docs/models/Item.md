# zenkipay-api-client.fi.zenki.zenkipay.api.model.item.Item

Information about a product or service.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about a product or service. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**unitPrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | Unit price of the product or service. | value must be a 64 bit float
**quantity** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of products or services of the order of the same type. | value must be a 64 bit integer
**name** | str,  | str,  | Short name of the product or service. | 
**externalId** | str,  | str,  | Unique identifier of the product or service assigned by the merchant. | [optional] 
**description** | None, str,  | NoneClass, str,  | Description of the product or service. | [optional] 
**type** | str,  | str,  | Indicates the model for the product delivery or service delivery.  Possible values: * WITH_CARRIER    - If a courier is going to be used for the shipment and delivery of the product or service. * WITHOUT_CARRIER - If a courier is not going to be used for the shipment and delivery of the product or service. | [optional] must be one of ["WITH_CARRIER", "WITHOUT_CARRIER", ] 
**thumbnailUrl** | None, str,  | NoneClass, str,  | Product image URL (thumbnail). | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Complementary information of the product or service that is required to be reported or kept in the Zenkipay system. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

Complementary information of the product or service that is required to be reported or kept in the Zenkipay system.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Complementary information of the product or service that is required to be reported or kept in the Zenkipay system. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

