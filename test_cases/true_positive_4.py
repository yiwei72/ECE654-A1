def linear_search_algo(values, search_for):
   search_at = 0
   search_res = False
   while search_at < len(values) and search_res is False:
      if values[search_at] == search_for:
         search_res = True
      else:
         search_at = search_at + 1
   return search_res

if __name__ == '__main__':
    l = [64, 34, 25, 12, 22, 11, 90]
    linear_search_algo(l, 12)