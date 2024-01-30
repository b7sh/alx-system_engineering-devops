#!usr/bin/env ruby
# Your script should output: [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/?\(\d{10}\)?[ -]?\(\d{10}\)[ -]?(\d{10})/).join
