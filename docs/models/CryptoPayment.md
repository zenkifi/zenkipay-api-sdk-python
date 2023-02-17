# zenkipay-api-client.fi.zenki.zenkipay.api.model.crypto_payment.CryptoPayment

Summary of the amount paid in crypto currency by the buyer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Summary of the amount paid in crypto currency by the buyer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amount** | str,  | str,  | Payment amount in cryptocurrency. | 
**blockchain** | str,  | str,  | Supported blockchains list.  Posibles valroes: * Bitcoin * Ethereum * Litecoin * Bitcoin Cash * Solana * Algorand * Polygon * Arbitrum * BSC * Avalanche * Ripple * Terra * Cardano * Polkadot * Tron * Stellar * Ethereum Classic * Hedera Hashgraph * Tezos * EOSIO * Fantom Opera * ZCash * Celo * Dash * XDC Network | 
**currency** | str,  | str,  | Code of the cryptocurrency supported by Zenkipay, see: https://developer.zenki.fi/global-v1/docs/zenkipay-recursos-catalogos-criptomonedas-soportadas | 
**transactionHash** | None, str,  | NoneClass, str,  | Unique identifier of the transaction, provided by the blockchain. | [optional] 
**networkScanUrl** | None, str,  | NoneClass, str,  | URL to check the status of the transaction directly on the blockchain. | [optional] 
**transactionStatus** | str,  | str,  | Payment status transaction in the blockchain network.  Possible values: * CONFIRMING                        - Pending confirmation on the blockchain. * PARTIALLY_COMPLETED               - One or more of of the transaction records have completed successfully (Only for Aggregated transactions). * COMPLETED                         - Successfully completed. * CANCELLED                         - The transaction was rejected by the Zenkipay Staff or by the 3rd party service. * REJECTED                          - La transacción fue rechazada por el servicio de terceros. * BLOCKED                           - The transaction was blocked due to a policy rule. * FAILED                            - The transaction has failed. | [optional] must be one of ["CONFIRMING", "PARTIALLY_COMPLETED", "COMPLETED", "CANCELLED", "REJECTED", "BLOCKED", "FAILED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

