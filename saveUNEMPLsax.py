import numpy as np
import pandas as pd

from saxpy.visit_registry import VisitRegistry
from saxpy.distance import early_abandoned_dist
from saxpy.znorm import znorm

#
#
url = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Unemployment_Rate.csv" #dialog box and return the path to the selected file
print(url)
df = pd.read_csv(url)
print(df.head())
series = np.array(df.Value)


"""Discord discovery routines."""


def find_best_discord_brute_force(series, win_size, global_registry,
                                  z_threshold=0.01):
    """Early-abandoned distance-based discord discovery."""
    best_so_far_distance = -1.0
    best_so_far_index = -1

    outerRegistry = global_registry.clone()

    outer_idx = outerRegistry.get_next_unvisited()

    while ~np.isnan(outer_idx):

        outerRegistry.mark_visited(outer_idx)

        candidate_seq = znorm(series[outer_idx:(outer_idx+win_size)],
                              z_threshold)

        nnDistance = np.inf
        innerRegistry = VisitRegistry(len(series) - win_size)

        inner_idx = innerRegistry.get_next_unvisited()

        while ~np.isnan(inner_idx):
            innerRegistry.mark_visited(inner_idx)

            if abs(inner_idx - outer_idx) > win_size:

                curr_seq = znorm(series[inner_idx:(inner_idx+win_size)],
                                 z_threshold)
                dist = early_abandoned_dist(candidate_seq,
                                            curr_seq, nnDistance)

                if (~np.isnan(dist)) and (dist < nnDistance):
                    nnDistance = dist

            inner_idx = innerRegistry.get_next_unvisited()

        if ~(np.inf == nnDistance) and (nnDistance > best_so_far_distance):
            best_so_far_distance = nnDistance
            best_so_far_index = outer_idx

        outer_idx = outerRegistry.get_next_unvisited()

    return (best_so_far_index)
# print(len(series))

def find_discords_brute_force(series, win_size = 50, num_discords=0.15*len(series),
                              z_threshold=0.01):
    """Early-abandoned distance-based discord discovery."""
    discords = list()

    globalRegistry = VisitRegistry(len(series))
    globalRegistry.mark_visited_range(len(series) - win_size, len(series))

    while (len(discords) < num_discords):

        bestDiscord = find_best_discord_brute_force(series, win_size,
                                                    globalRegistry,
                                                    z_threshold)

        if -1 == bestDiscord:
            break

        discords.append(bestDiscord)

        mark_start = bestDiscord - win_size
        if 0 > mark_start:
            mark_start = 0

        mark_end = bestDiscord + win_size
        '''if len(series) < mark_end:
            mark_end = len(series)'''

        globalRegistry.mark_visited_range(mark_start, mark_end)

    return discords

# print(find_discords_brute_force(series))
# print(series)

p = df.index.values
df.insert( 0, column="new",value = p)
y=len(df['Value'])
# print(df.index)
xaa=find_discords_brute_force(series)

df2  =pd.DataFrame(xaa, columns= ['Value'])

x=len(find_discords_brute_force(series))
z=abs(y-x)
for i in range(z):
    df2 = df2.append(pd.Series([0], index=df2.columns ), ignore_index=True)

df = df.assign(anomaly=df['new'].isin(df2['Value']).astype(int))
a = df.loc[df['anomaly'] == 1, ['Date', 'Value']] #anomaly

a.to_csv('UnemplsaxAnom.csv')