import pyserum
import asyncio
from pyserum.async_connection import async_conn
from pyserum.market import AsyncMarket
from pyserum.connection import get_live_markets, get_token_mints
from pyserum.connection import conn
from pyserum.market import Market
from solana.account import Account
from solana.account import PublicKey
from solana.rpc.types import TxOpts
from spl.token.client import Token
from spl.token.constants import TOKEN_PROGRAM_ID
from pyserum.connection import get_live_markets, get_token_mints
from pyserum.enums import OrderType, Side



#Prints all live markets on Mainnet
#print("tokens: ")
#print(get_token_mints())
#print("markets: ")



#print(get_live_markets())


#Orderbook for X


async def main():


    market_address = "A8YFbxQYFVqKZaoYJLLUVcQiWP7G2MeEgW5wsAQgMvFw" # For BTCUSDC on serum
    async with async_conn("http://api.mainnet-beta.solana.com/") as cc:


        payer = Account() # Your account to pay fees
        quote_token = Token(
        cc,
        pubkey=PublicKey("EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1vE"), # mint address of token
        program_id=TOKEN_PROGRAM_ID,
        payer=payer,
        )

        quote_wallet = quote_token.create_account(
        payer.public_key(),
        skip_confirmation=True)

        #Load Market
        market = await AsyncMarket.load(cc, market_address)


        #Show Asks
        asks = await market.load_asks()
        print("Ask Orders: ")
        for ask in asks:
            print(f"Order id: {ask.order_id}, price: {ask.info.price}, size: {ask.info.size}.")


        print("\n")




        #Show Bids
        print("Bid orders:")
        bids = await market.load_bids()
        for bid in bids:
            print(f"Order id: {bid.order_id}, price: {bid.info.price}, size: {bid.info.size}.")

        print("\n")


        
    tx_sig2 = market.place_order(
        payer=quote_wallet,
        owner=payer,
        side=Side.Sell,
        order_type=OrderType.limit,
        limit_price=35000,
        max_quantity=0.01,
        opts = TxOpts(skip_preflight=True)
    )

    print(tx_sig2)


    tx_sig = market.place_order(
            payer=quote_wallet,
            owner=payer,
            side=Side.Buy,
            order_type=OrderType.limit,
            limit_price=30000,
            max_quantity=0.01,
            opts = TxOpts(skip_preflight=True)
            )
    print(tx_sig)


    asyncio.run(main())















