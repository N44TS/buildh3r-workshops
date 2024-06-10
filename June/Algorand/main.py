from algokit_utils.beta.algorand_client import (
    AlgorandClient, 
    AssetCreateParams, 
    AssetOptInParams, 
    AssetTransferParams, 
    PayParams,
    )

algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()

creator = algorand.account.random()

algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=creator.address,
        amount=10_000_000
    )
)

sent_txn = algorand.send.asset_create (
AssetCreateParams (
    sender=creator.address,
    total=1000,
    asset_name="WEB3",
    unit_name="SATS",
    manager=creator.address,
    clawback=creator.address,
    freeze=creator.address
)
)

asset_id = sent_txn["confirmation"]["asset-index"]
print ("asset ID:", asset_id)

receiver_acct = algorand.account.random()
#print("receiver address:", receiver_acct.address)


algorand.send.payment(
    PayParams(
        sender=dispenser.address,
        receiver=receiver_acct.address,
        amount=10_000_000
    )
)

group_tx = algorand.new_group()

group_tx.add_asset_opt_in (
    AssetOptInParams(
        sender=receiver_acct.address,
        asset_id=asset_id
    )
)

group_tx.add_payment (
    PayParams (
        sender=receiver_acct.address,
        receiver=creator.address,
        amount=1_000_000
    )
)

group_tx.add_asset_transfer(
    AssetTransferParams (
    sender=creator.address,
    receiver=receiver_acct.address,
    asset_id=asset_id,
    amount=10
)
)

group_tx.execute()

print("Receiver acct asset balance:", algorand.account.get_information(receiver_acct.address)['assets'][0]['amount'])
print("creator acct asset balance:", algorand.account.get_information(creator.address)['assets'][0]['amount'])


# clawback 5 units from the receiver to the creator for the task
algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=creator.address,
        asset_id=asset_id,
        amount=5,
        clawback_target=receiver_acct.address
    )
)

print("Post clawback:")
print("Receiver acct asset balance:", algorand.account.get_information(receiver_acct.address)['assets'][0]['amount'])
print("creator acct asset balance:", algorand.account.get_information(creator.address)['assets'][0]['amount'])