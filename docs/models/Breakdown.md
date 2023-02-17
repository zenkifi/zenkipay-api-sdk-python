# zenkipay-api-client.fi.zenki.zenkipay.api.model.breakdown.Breakdown

Summary of shopping cart amounts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Summary of shopping cart amounts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**grandTotalAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of subtotalAmount, taxesAmount, localTaxesAmount, importCosts, and each value of additionalCharges minus discountAmount. | value must be a 64 bit float
**totalItemsAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of the total cost of the items (quantity * unitPrice). | value must be a 64 bit float
**taxesAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Taxes, if not applied, its value must be 0. | value must be a 64 bit float
**currencyCodeIso3** | str,  | str,  | Unique code of the currency of the country, the definition of the ISO 4217 standard is used with 3 characters, see: https://es.wikipedia.org/wiki/ISO_4217 or https://www.iso.org/iso-4217-currency-codes.html. | 
**shipmentAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Shipping cost, in case of not applying its value must be 0. | value must be a 64 bit float
**subtotalAmount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of total_items_amount plus shipment_amount. | value must be a 64 bit float
**localTaxes_amount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Local taxes, if not applied, its value must be 0. | [optional] value must be a 64 bit float
**importCosts** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Import costs, if not applied, its value must be 0. | [optional] value must be a 64 bit float
**discountAmount** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Discount of your merchant, in case of not applying its value must be 0. | [optional] value must be a 64 bit float
**[additionalCharges](#additionalCharges)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Additional charges, consists of a key/value object that comprises the description of the charge/amount respectively. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# additionalCharges

Additional charges, consists of a key/value object that comprises the description of the charge/amount respectively.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Additional charges, consists of a key/value object that comprises the description of the charge/amount respectively. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

