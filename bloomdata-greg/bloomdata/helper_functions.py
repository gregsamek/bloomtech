def null_count(df):
    return df.isna().sum().sum()

def randomize(df, seed):
    return df.sample(frac=1.0, random_state=seed)

def greg_test():
    print('GREG')