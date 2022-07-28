data.to_pickle("C:/Users/Aayus/Downloads/ANZ/data.pkl")

data[['txn_description','amount']].groupby("txn_description", as_index=False).mean().sort_values(by="amount",
                                                                                                ascending=False)
