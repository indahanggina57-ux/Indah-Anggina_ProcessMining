import pm4py
import pandas as pd

df = pd.read_csv('event_log.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
log = pm4py.format_dataframe(df, case_id='case_id', activity_key='activity', timestamp_key='timestamp')

dfg, start_act, end_act = pm4py.discover_dfg(log)
print("DFG berhasil ditemukan")

net, im, fm = pm4py.discover_petri_net_alpha(log)
heu_net = pm4py.discover_heuristics_net(log)

fitness = pm4py.fitness_token_based_replay(log, net, im, fm)
print(fitness)
