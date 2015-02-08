using Graphs

#the whole graph is local, which is quite annoying
#but is interesting enough.
#a next step is to turn this parallel.

function gossip_minimum(graph)
  #each node has a value and its own guess for minimum
  #at each point, the node takes a random neighbor and
  #compare the guess it has and its neighbor's guess and take min
end

function gossip_minimum_test(graph)
end

function gossip_sum(graph)
  #each node has a value and its own guess for minimum
  #at each point, the node takes a random neighbor and
  #compare the guess it has and its neighbor's guess and take min
  #then generate some random numbers according to exponential distribution
  #then actually say that the mean is the estimator,
  #due to properties of the exponential distribution. hey! you have mean, so you have sum!
end

function gossip_sum_test(graph)
end
