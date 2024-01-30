#!/usr/bin/env ruby
# Find the regular expression that will match some cases
puts ARGV[0].scan(/h(t|b|tb|bt)n/).join
