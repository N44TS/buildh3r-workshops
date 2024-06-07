from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams,
)

algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
#print(dispenser.address)
creator = algorand.account.random()
#print(creator.address)
#print(algorand.account.get_information(creator.address))

algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000
    )
)
#print(algorand.account.get_information(creator.address))

# Create the token
sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=333,
        asset_name="BUILDHER",
        unit_name="HER"
    )
)

asset_id = sent_txn["confirmation"]["asset-index"]
#print(asset_id)

# Create three receiver accounts
receiver_accts = [algorand.account.random() for _ in range(3)]

#send the asset from creator to reciever before opting in causes error
# asset_transfer = algorand.send.asset_transfer (
#     AssetTransferParams (
#         sender=creator.address,
#         receiver=receiver_acct.address,
#         asset_id=asset_id,
#         amount=111
#     )
# ) 

for receiver_acct in receiver_accts:
    algorand.send.payment(
        PayParams(
            sender=dispenser.address,
            receiver=receiver_acct.address,
            amount=10_000_000
        )
    )

#opt in to asset so don't get spammed
    algorand.send.asset_opt_in(
        AssetOptInParams(
            sender=receiver_acct.address,
            asset_id=asset_id
        )
    )

    asset_transfer = algorand.send.asset_transfer(
        AssetTransferParams(
            sender=creator.address,
            receiver=receiver_acct.address,
            asset_id=asset_id,
            amount=111,
            last_valid_round=100 #this is why it kepy erroring! The ending round for which the transaction is valid. After this round, the transaction will be rejected by the network
        )
    )

    print(f"Account {receiver_acct.address} information:")
    print(algorand.account.get_information(receiver_acct.address))
    print()