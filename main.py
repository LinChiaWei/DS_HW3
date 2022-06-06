def config():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--consumption", default="./sample_data/consumption.csv", help="input the consumption data path")
    parser.add_argument("--generation", default="./sample_data/generation.csv", help="input the generation data path")
    parser.add_argument("--bidresult", default="./sample_data/bidresult.csv", help="input the bids result path")
    parser.add_argument("--output", default="output.csv", help="output the bids path")

    return parser.parse_args()


def output(path, data):
    import pandas as pd

    df = pd.DataFrame(data, columns=["time", "action", "target_price", "target_volume"])
    df.to_csv(path, index=False)

    return


if __name__ == "__main__":
    args = config()

    import numpy as np
    import pandas as pd
    # import tensorflow as tf
    # from sklearn.preprocessing import MinMaxScaler
    

    ### read data
    generation = pd.read_csv(args.generation,index_col='time', parse_dates=['time'])
    consumption = pd.read_csv(args.consumption,index_col='time', parse_dates=['time'])
    bidresult = pd.read_csv(args.bidresult,index_col='time', parse_dates=['time'])

    gen_data = generation.values
    cons_data = consumption.values
    ###

    ###prepare data
    # gen_set = gen_data.reshape(-1, 1)
    # cons_set = cons_data.reshape(-1, 1)

    # sc = MinMaxScaler(feature_range = (0, 1))
    # gen_set_scaled = sc.fit_transform(gen_set)
    # cons_set_scaled = sc.fit_transform(cons_set)

    # X_gen = []
    # X_cons = []
    
    # for i in range(144, 168): 
    #     X_gen.append(gen_set_scaled[i-144:i, 0])
    # X_gen = np.array(X_gen)
    # X_gen = np.reshape(X_gen, (X_gen.shape[0], X_gen.shape[1], 1))

    # for i in range(144, 168): 
    #     X_cons.append(cons_set_scaled[i-144:i, 0])
    # X_cons = np.array(X_cons)
    # X_cons = np.reshape(X_cons, (X_cons.shape[0], X_cons.shape[1], 1))
    ###

    ###predict gen
    # model_gen = tf.keras.models.load_model('./gen.h5')
    # results_gen = model_gen.predict(X_gen)
    # ori_results_gen = sc.inverse_transform(results_gen)
    # # print(np.sum(ori_results_gen))

    # model_cons = tf.keras.models.load_model('./cons.h5')
    # results_cons = model_gen.predict(X_cons)
    # ori_results_cons = sc.inverse_transform(results_cons)
    # print(np.sum(ori_results_cons))

    # print(np.sum(gen_data[-24:]))
    # print(np.sum(cons_data[-24:]))
    ###




    ### stragedy
    data = pd.DataFrame(columns=["time", "action", "target_price", "target_volume"])
    time = pd.date_range(start='09/01/2018', periods = 24,freq='H')

    gen_all = np.sum(gen_data)
    cons_all = np.sum(cons_data)


    
    if cons_all > gen_all:
        need = cons_all-gen_all
        average = need / gen_data.shape[0]
        average = average / 4
        for i in range(24):
            hour = time[i] 
            data = data.append({"time":hour,"action":"sell","target_price":2,"target_volume":average},ignore_index=True)
            data = data.append({"time":hour,"action":"sell","target_price":1.9,"target_volume":average},ignore_index=True)

    else:
        need = gen_all-cons_all
        average = need / gen_data.shape[0]
        average = average / 4
        for i in range(24):
            hour = time[i] 
            data = data.append({"time":hour,"action":"sell","target_price":2,"target_volume":average},ignore_index=True)
            data = data.append({"time":hour,"action":"sell","target_price":1.9,"target_volume":average},ignore_index=True)


    ###

    ###output
    ### time(%Y-%m-%d %H:%M:%S), action, price, volume  
    data.to_csv(args.output,index=False)
    ###
