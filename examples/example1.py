#!/usr/bin/python
#
# This program does a Google search for "quick and dirty" and returns
# 50 results.
#

from xgoogle.search import GoogleSearch, SearchError
try:
  gs = GoogleSearch("kylinpoet")
  gs.results_per_page = 50
  results = gs.get_results()
  for res in results:
    print res.title.encode('gbk')
    print res.desc.encode('gbk')
    print res.url.encode('gbk')
    print
except SearchError, e:
  print "Search failed: %s" % e

