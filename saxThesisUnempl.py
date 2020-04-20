# # from fuzzywuzzy import fuzz
# import itertools
# import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict
from saxpy.strfunc import idx2letter
from saxpy.znorm import znorm
from saxpy.paa import paa
from saxpy.alphabet import cuts_for_asize
from tkinter.filedialog import askopenfilename
import numpy as np
from saxpy.visit_registry import VisitRegistry
from saxpy.distance import early_abandoned_dist
from saxpy.znorm import znorm
import matplotlib.pyplot as plt

#
#
url = "C:/Users/Βασίλης/IdeaProjects/MyThesisApp/Data sets/Unemployment_Rate.csv" #dialog box and return the path to the selected file
print(url)
df = pd.read_csv(url)
series = np.array(df.Value)
# #
# def ts_to_string(series, cuts):
#     """A straightforward num-to-string conversion."""
#     a_size = len(cuts)
#     sax = list()
#
#     for i in range(0, len(series)):
#         num = series[i]
#
#         # if teh number below 0, start from the bottom, or else from the top
#         if(num >= 0):
#             j = a_size - 1
#             while ((j > 0) and (cuts[j] >= num)):
#                 j = j - 1
#             sax.append(idx2letter(j))
#         else:
#             j = 1
#             while (j < a_size and cuts[j] <= num):
#                 j = j + 1
#             sax.append(idx2letter(j-1))
#
#     return ''.join(sax)
#
#
# def is_mindist_zero(a, b):
#     """Check mindist."""
#     if len(a) != len(b):
#         return 0
#     else:
#         for i in range(0, len(b)):
#             if abs(ord(a[i]) - ord(b[i])) > 1:
#                 return 0
#     return 1
#
#
# # def sax_by_chunking(series, paa_size, alphabet_size=4, z_threshold=0.01):
# #     """Simple chunking conversion implementation."""
# #     paa_rep = paa(znorm(series, z_threshold), paa_size)
# #     cuts = cuts_for_asize(alphabet_size)
# #     return ts_to_string(paa_rep, cuts)
#
#
# def sax_via_window(series, win_size=30, paa_size=4, alphabet_size=3,
#                    nr_strategy='none', z_threshold=0.01):
#     """Simple via window conversion implementation."""
#     cuts = cuts_for_asize(alphabet_size)
#     sax = defaultdict(list)
#
#     prev_word = ''
#
#     for i in range(0, len(series) - win_size):
#
#         sub_section = series[i:(i+win_size)]
#
#         zn = znorm(sub_section, z_threshold)
#
#         paa_rep = paa(zn, paa_size)
#
#         curr_word = ts_to_string(paa_rep, cuts)
#
#         if '' != prev_word:
#             if 'exact' == nr_strategy and prev_word == curr_word:
#                 print("aaaa")
#                 continue
#
#             elif 'mindist' == nr_strategy and \
#                     is_mindist_zero(prev_word, curr_word):
#                 print("bbbb")
#                 continue
#
#         prev_word = curr_word
#
#         sax[curr_word].append(i)
#
#
#     return sax
#
# saxres=sax_via_window(series)
# print("-----------------------------------------------------------------------------")
# print(saxres.keys())
# print("-----------------------------------------------------------------------------")
# print(saxres.values())
#
# print("-----------------------------------------------------------------------------")
# print(saxres)

# print(*saxres, sep = "\n")
#ousiastikadhmiourgw ena dictionary
# keys= list(saxres.keys())



# print('----------------------------------------------------------------------------------------------------------------------------------')
# # df['anomaly'] = pd.Series(len(keys))
# ratio = []
# anomaly = []
# for a, b in itertools.combinations(keys, 2):
#     ex = fuzz.ratio(a, b)#elegxw an uparxei omoiothta metaksu twn elements sthn
#
#     ratio.append(ex)
#     if ex <=40 :
#         anomaly.append(-1)#me omoiothta miktoterh h ish tou 40% thewreitai anomalia kai tou anathetw to-1
#
#     elif ex >40:
#         anomaly.append(1)
#
#
# # kenourio dataframe
# anomlist = pd.DataFrame(
#     {'ratio': ratio,
#      'anomaly': anomaly,
#      })

# print(anomlist)
# plt.plot(series)
# plt.show()
# plt.plot(anomlist)
# plt.show()



"""Discord discovery routines."""



def find_best_discord_brute_force(series, win_size , global_registry,
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

    return best_so_far_index
# print(len(series))

def find_discords_brute_force(series, win_size = 1, num_discords=12,
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
print(df.new)
colors = ['r' if anomaly==1 else 'b' for anomaly in df.anomaly]

plt.plot(df['Date'], df['Value'], color='blue', linewidth=1)

plt.scatter(df['Date'], df['Value'], color=colors, linewidths=0)
plt.show()