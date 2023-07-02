#s = aaaabcca
# a: 5, b: 1, c: 2

# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#                 print(sym, counter)
#
# s = 'aaabc'
# strcounter(set(s))
# это реализация через функцию, простую в написании, но отнимающую много сил у компа




def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1





