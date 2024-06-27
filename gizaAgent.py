
import streamlit as st

from giza.agents import AgentResult, GizaAgent
from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.models import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.net.full_node_client import FullNodeClient

from starknet_py import contract

# First, make sure to generate private key and salt
address = "0x05fd2cc5fdd0a2b424966ad29632b0f38d72ee910a11f436fbf3e33078dd42f0"
private_key = "0x7b15f1740059aba94cbabf88d91c20c4cbc6874d5854a360d764127b9fa4e8"
class_hash = "0x00816dd0297efc55dc1e7559020a3a825e81ef734b558f03c83325d4da7e6253"
salt = 1234567890

#node_url = "<https://starknet-mainnet.g.alchemy.com/v2/-RKRlVd3tmxZAHYO2QbBNp6E6y7vCXXE"

node_url = "https://starknet-sepolia.g.alchemy.com/v2/FsWY3C1loeRRGwyyBr9wEtVFGk5djhN9"
client = FullNodeClient(node_url=node_url)

starkNetSepoliaChainID = StarknetChainId.SEPOLIA

# we create an instance of our Account
account = Account(
        address=address,
        client=client,
        key_pair=KeyPair.from_private_key(private_key),
        chain=starkNetSepoliaChainID,
    )
#"insuranceEnrollmentContract" = balanceSTRKContractAddress:


st.write("address",address)
st.write("client",client)
st.write("chain",starkNetSepoliaChainID)


insuranceEnrollmentContractAddress = "0x041a78e741e5af2fec34b695679bc6891742439f7afb8484ecd7766661ad02bf"

    # Fill this contracts dictionary with the contract addresses that our agent will interact with
contracts = {
        "insuranceEnrollmentContract": insuranceEnrollmentContractAddress,
        "WETH":  "0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14",
}

agent_id = 78
account_alias ="chainaimlabs3003"
#chain= "https://starknet-mainnet.g.alchemy.com/v2/-RKRlVd3tmxZAHYO2QbBNp6E6y7vCXXE"
chain="https://starknet-sepolia.g.alchemy.com/v2/FsWY3C1loeRRGwyyBr9wEtVFGk5djhN9"


# we create an instance of our Agent given the id
agent = GizaAgent.from_id(
        id=agent_id,
        contracts=contracts,
        chain=chain,
        account=account_alias,
    )
    
# X is the data input you need to define
#prediction = agent.predict(input_feed={"input": X}, verifiable=True)

prediction = agent.predict(
        #input_feed=input,
        input_feed={'input': input},
        verifiable=True,
        dry_run=True,
        job_size="S",
     )  


result = contracts.insuranceEnrollmentContract.get();

print( "result from starknet ", result)

#contract = Contract.from_address(provider=account, address=address)

#sender = "321"
#recipient = "123"

# Using only positional arguments
#nvocation = await contract.functions["transferFrom"].invoke_v1(
#    sender=sender, recipient=recipient, amount=10000, max_fee=int(1e16)
#)