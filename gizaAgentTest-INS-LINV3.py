import streamlit as st
import argparse
import logging
import os
import pprint
from logging import getLogger

# %%
import numpy as np
# %%
from dotenv import find_dotenv, load_dotenv

# %%
from giza.agents import AgentResult, GizaAgent


# %%
from addresses import ADDRESSES

# %%
# from lp_tools import get_tick_range
# from uni_helpers import (approve_token, check_allowance, close_position,
#                          get_all_user_positions, get_mint_params)

# %%
load_dotenv(find_dotenv())

# %%
dev_passphrase = os.environ.get("DEV_PASSPHRASE")
sepolia_rpc_url = os.environ.get("SEPOLIA_RPC_URL")

print(dev_passphrase)
print(sepolia_rpc_url)

dev_passphrase = "catestHack2024"
sepolia_rpc_url = os.environ.get("SEPOLIA_RPC_URL")

# %%
logging.basicConfig(level=logging.INFO)

# %%
def create_agent(
    model_id: int, version_id: int, chain: str, contracts: dict, account: str
):
    """
    Create a Giza agent for the regression model
    """
    agent = GizaAgent(
        contracts=contracts,
        id=model_id,
        version_id=version_id,
        chain=chain,
        account=account,
    )
    return agent

# %%
def predict(agent: GizaAgent, X: np.ndarray):
    """
    Predict for the results of the model

    Args:
        X (np.ndarray): Input to the model.

    Returns:
        int: Predicted value.
    """
    prediction = agent.predict(input_feed={"val": X}, verifiable=True, job_size="XL")
    return prediction

# %%
def get_pred_val(prediction: AgentResult):
    """
    Get the value from the prediction.

    Args:
        prediction (dict): Prediction from the model.

    Returns:
        int: Predicted value.
    """
    # This will block the executon until the prediction has generated the proof
    # and the proof has been verified
    return prediction.value[0][0]

# %%
def eval_quote(
    #agent_id: int,
    pred_model_id:int,
    pred_version_id:int,
    policyId:int,
    quote: float,
    bmi:float,
    #chainURL:str,
    #chain=f"ethereum:sepolia:{SEPOLIA_RPC_URL}",
    account="chainaimlabs3003",
    chain=f"ethereum:sepolia:{sepolia_rpc_url}",
):
    
    ## Change the INS-ENROLLMENT-AGENT_PASSPHRASE to be {AGENT-NAME}_PASSPHRASE
    # os.environ["INS_ENROLLMENT-AGENT_PASSPHRASE"] = os.environ.get("DEV_PASSPHRASE")

    # Create logger

    logger = getLogger("agent_logger");

   

    #chain=f"ethereum:sepolia:{SEPOLIA_RPC_URL}",
    #networks.parse_network_choice(f"ethereum:sepolia:{SEPOLIA_RPC_URL}").__enter__()

    st.write(chain)

    chain_id = 11155111;
    #chain_id = chain.chain_id;
    #print (chain_id);

    # Load the addresses

    #insuranceEnrollmentContractAddress = ADDRESSES["INSE"][chain_id]
    insuranceEnrollmentContractAddress = "0x96d3441592F87CE5d89C8220DCbef3cFd06a9976";

    # The IEPVContract 
    #insuranceEnrollmentContractAddress = "0x6D15540f38295566455Ba36747EE9d951a0d1dAf";

    #insuranceEnrollmentContractAddress = "0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14";

    chainZkSyncURL=""
    chainIdZkSync=300
    insuranceEnrollmentContractAddressZkSync = "0x17ba8fc541A9747059fD6e4C617C40e8A9B25951";
    ZKSYNC_SEPOLIA_RPC_URL="https://zksync-sepolia.g.alchemy.com/v2/alcht_qTqyinch9eBi0vF09MR064gABbQbLI"

    
    # Load the data, this can be changed to retrieve live data
    #file_path = "data/data_array.npy"
    #X = np.load(file_path)
     
  
    # Fill this contracts dictionary with the contract addresses that our agent will interact with
    contracts = {
        "insuranceEnrollmentContract": insuranceEnrollmentContractAddress,
        "WETH":  "0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14",
    }


    contractsZkSync = {
        "insuranceEnrollmentContract": insuranceEnrollmentContractAddressZkSync,
        "WETH":  "0xfFf9976782d46CC05630D1f6eBAb18b2324d6B14",
    }

    # Create the agent
    
    agent = create_agent(
        model_id=pred_model_id,
        version_id=pred_version_id,
        chain=chain,
        contracts=contracts,
        account=account,
    )

  
    #st.write("agent" , agent.contracts.insuranceEnrollmentContract)

    #agent = create_agent(
    #    model_id=pred_model_id,
    #    version_id=pred_version_id,
    #    chain=ZKSYNC_SEPOLIA_RPC_URL,
    #    contracts=contractsZkSync,
    #    account=account,
    #)


    st.header("User Inputs")

                # Age input
    age = st.number_input("Age", value=29 )

                # Gender input
    gender_options = ["Male", "Female"]
    gender = st.selectbox("Gender", options=gender_options)

                # Children input
    children = st.number_input("Number of Children", min_value=0, step=1)

                # Smoker input
    smoker_options = ["Yes", "No"]
    smoker = st.selectbox("Smoker", options=smoker_options)

     # Age input
    bmi = st.number_input("BMI", value=30.1 )

                # Region input
    region_options = ["north-east", "south-east", "south-west"]
    region = st.selectbox("Region", options=region_options)


        # Run button
    if st.button("Run"):
            # Results
            st.markdown("---")
            st.header("Results")
           
            input = np.array([[bmi]]).astype(np.float32)

            #result = eval_quote(MODEL_ID,VERSION_ID,policyId,quote,bmi)

           
            st.write("");
            #st.write(f"{age}")
            #st.write(f"{gender}")
            #st.write(f"{children}")
            #st.write(f"{smoker}")
            #st.write(f"{region}")

            # Line
            st.markdown("---")


         #file_path = "data/data_array.npy"
         #input = np.load(file_path)

            input = np.array([[bmi]]).astype(np.float32)
            #st.write("input dim " ,input.ndim)
  
            #input2 = np.array([bmi,1])
            #st.write("input2 dim ",input2.ndim)
            #st.write(" shape ",input.shape)
            #st.write(" input is ",input)
    
       
            print(input)

            # THIS WORKED >>
            #result = predict(agent, input)

            # result = predict(agent, input, job_size="S", dry_run=True)
            ###  IMP input = np.array([[bmi]]).astype(np.float32)

            input = np.array([[bmi]]).astype(np.float32)

            # THIS WORKED................
            result = agent.predict(
            #input_feed=input,
            input_feed={'input': input},
            verifiable=True,
            dry_run=True,
            job_size="S",
            )  

# From giza doc...
 #   result = agent.predict(
 #       input_feed=<input-data>,
 #       verifiable=True,
 #       dry_run=True,
 #   )  

# From Gonzalo
#prediction = agent.predict(
#        input_feed={"image": image}, verifiable=True, job_size="S", dry_run=True
#    )
#    return prediction


  # This errored..
    #prediction = agent.predict(
    #    input_feed = input, verifiable=True, job_size="S", dry_run=False
    #)
    #return prediction

 # This errored..
   # prediction = agent.predict(
   #     input_feed = {"image":bmi}, verifiable=True, job_size="S", dry_run=False
   # )
   # return prediction

    #st.write( "prediction back", prediction)

    #resultVal = result.value

    # For User Inputs of , the predicted premium is ...

    #print(resultVal)

    #st.write("Model prediction Result ", result)
    #st.write("Model prediction ResultVal ", resultVal)

# Eventually we need to do the logic ..  
# If Quote < ( 1 + tolerance * 1 / 100) ) - THen .. 

# st.write ( Agent  Execution to Buy Policy ordered in  Chain + chain ID )

#else

            st.write("Predicted Value (Insurance Premium Price : "  , result)

    if st.button("Buy Policy"):
    #        commission = 0.001
    #        initialInvestment = 1000000
    #        interval='1d'

        try:
            with agent.execute() as contracts:
                logger.info("Executing INSE contract with policyId  "  )
                #contracts.WETH.deposit(value = 1000);
                contracts.insuranceEnrollmentContract.buyPolicy(policyId,value =13500);
                
                #res = contracts.insuranceEnrollmentContract.insurerWallet();
                #print(res);

                logger.info("Executing INSE contract");

        except Exception as e:    
            #st.write(f"Caught an exception of type: {type(e).__name__}")
            #readbackPolicy = contracts.insuranceEnrollmentContract.policies(policyId)
            #st.write(" Updated Policy Details  ", readbackPolicy )

            #explorerLink="https://sepolia.etherscan.io/address/0x96d3441592F87CE5d89C8220DCbef3cFd06a9976"
            st.write(" [Policy Enrolled. Please see the Blockchain Explorer] (https://sepolia.etherscan.io/address/0x96d3441592F87CE5d89C8220DCbef3cFd06a9976)")
            #st.write(" [Policy Enrolled. Please see the Blockchain Explorer] (https://sepolia.etherscan.io/address/0x6D15540f38295566455Ba36747EE9d951a0d1dAf)")
            #st.write("[Click here to visit Streamlit's website](https://www.streamlit.io/)")

    # This will block the executon until the prediction has generated the proof
    # and the proof has been verified

            #print(result)
    
    #return result
    return

# %%
if __name__ == "__main__":
   
    #st.title(" ZK  ML GIZA DvP Engine ")
    #st.write(" ZKML for Verifiable Trust Collaboration For Real world Applications")
    #st.write("   Scenario 1 -  Insurance Price Transparency - US Healthcare ..")
    #st.write("   Scenario 2 -  Insurance Claims Adjudicaion - US Healthcare  Alternate Payments Settlement..")
    #st.write("   Scenario 3 -  SupplyChain Charges -  Settlement ..")
    #st.write("   Scenario 4 -  Dynamic Portfolio Allocations ..")

    #st.write(" User Scenario ") # pick list...

    st.title(" ZK ML Veri Price  ")
    st.write(" ZKML - Verify ML : For Real World Price Verification Models ")
    st.write(" First Usecase: Insurance Price Transparency - US Healthcare ..")
    st.write(" Extensions : to other usecases ..")

    #st.write("   Scenario 2 -  Insurance Claims Adjudicaion - US Healthcare  Alternate Payments Settlement..")
    #st.write("   Scenario 3 -  SupplyChain Charges -  Settlement ..")
    #st.write("   Scenario 4 -  Dynamic Portfolio Allocations ..")

# In the UI I need 
#  A dropdown to pick the Scenario., as soon as they change the UI has to show the Model , Version ID differently.
#  For scenario 1 - Show Public Reference Model ID :  739 ,  Version ID : 1 
#  Upward Tolerance for Insurance Quote : 5 %

    MODEL_ID = 719
    VERSION_ID = 3

    print(MODEL_ID)
    print(VERSION_ID)

    # Display in the sidebar
    st.sidebar.header("Model Information")
    st.sidebar.write("Model Info: Verifiable ML")
    st.sidebar.write("Price Transparency US Healthcare.")

    st.sidebar.write("Model ID:", MODEL_ID)
    st.sidebar.write("Version ID:", VERSION_ID)    

    # Fetch and display the current Ethereum price
    #current_eth_price = get_eth_price()
    #st.sidebar.markdown("---")
    #st.sidebar.write("Current Ethereum Price:", current_eth_price)    

    # Slider for Risk Level
    st.sidebar.markdown("---")

  
    st.sidebar.header("Insurance Policy ACME ")
    st.sidebar.header("Quote : 13500" )


    # Slider for Risk Level
    st.sidebar.markdown("---")
    st.sidebar.header("Agent Parameters")
    st.sidebar.header("User Defined")

    upward_tolerance_level = st.sidebar.slider("Select Upward Price Tolerance Level", min_value=0, max_value=100, value=10)

    #tokenWETH_amount = 2500000
    #tokenUSDC_amount = 1000000
    #st.subheader("your current portfolio holdings")

    # rebalance_lp(tokenWETH_amount, tokenUSDC_amount, MODEL_ID, VERSION_ID)
    #weth, usdc = rebalance_lp_NOMODEL(tokenWETH_amount, tokenUSDC_amount, MODEL_ID, VERSION_ID)

    #wethUSD = weth * current_eth_price
    # Display the tokenWETH_amount
    #st.metric("WETH", weth)
    #st.write(f"WETH USD Value: {wethUSD:.2f}")
    #st.metric("USDC Amount", usdc)

    # Add an extra line before the submit button
    st.text("")
    st.text("")

    #if st.button("Call Agent"):
    #        commission = 0.001
    #        initialInvestment = 1000000
    #        interval='1d'

# For Scenario 1 :  We need to       #  ALSO fix  chain, chain id and address...
    pred_model_id = 719
    pred_version_id = 3


# For Scenario #1 - Insurance offer
    #policyId = 1
    #quote = 100

    policyId = 7
    quote = 13500

# User Public verification user inputs... 
    bmi = 31.1

# For Scenario 2 :
    #pred_model_id =XXX
    #pred_version_id = X
# %%


    eval_quote(pred_model_id,pred_version_id,policyId,quote,bmi)