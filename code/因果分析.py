import numpy
import pandas as pd

from causality.inference.search import IC
from causality.inference.independence_tests import RobustRegressionTest

from causality.estimation.adjustments import AdjustForDirectCauses
from networkx import DiGraph



SIZE = 2000
x1 = numpy.random.normal(size=SIZE)
x2 = x1 + numpy.random.normal(size=SIZE)
x3 = x1 + numpy.random.normal(size=SIZE)
x4 = x2 + x3 + numpy.random.normal(size=SIZE)
x5 = x4 + numpy.random.normal(size=SIZE)

# load the data into a dataframe:
X = pd.DataFrame({'x1' : x1, 'x2' : x2, 'x3' : x3, 'x4' : x4, 'x5' : x5})

# define the variable types: 'c' is 'continuous'.  The variables defined here
# are the ones the search is performed over  -- NOT all the variables defined
# in the data frame.
variable_types = {'x1' : 'c', 'x2' : 'c', 'x3' : 'c', 'x4' : 'c', 'x5' : 'c'}
g = DiGraph()

g.add_nodes_from(['x1','x2','x3','x4', 'x5'])
g.add_edges_from([('x1','x2'),('x1','x3'),('x2','x4'),('x3','x4')])
adjustment = AdjustForDirectCauses()
print(adjustment.admissable_set(g, ['x2'], ['x3']))
# set(['x1'])
from causality.estimation.nonparametric import CausalEffect
admissable_set = adjustment.admissable_set(g,['x2'], ['x3'])
effect = CausalEffect(X, ['x2'], ['x3'], variable_types=variable_types, admissable_set=list(admissable_set))
x = pd.DataFrame({'x2' : [0.], 'x3' : [0.]})
res = effect.pdf(x)
print(res)

# generate some toy data:
# SIZE = 2000
# x1 = numpy.random.normal(size=SIZE)
# x2 = x1 + numpy.random.normal(size=SIZE)
# x3 = x1 + numpy.random.normal(size=SIZE)
# x4 = x2 + x3 + numpy.random.normal(size=SIZE)
# x5 = x4 + numpy.random.normal(size=SIZE)
#
# # load the data into a dataframe:
# X = pd.DataFrame({'x1' : x1, 'x2' : x2, 'x3' : x3, 'x4' : x4, 'x5' : x5})
#
# # define the variable types: 'c' is 'continuous'.  The variables defined here
# # are the ones the search is performed over  -- NOT all the variables defined
# # in the data frame.
# variable_types = {'x1' : 'c', 'x2' : 'c', 'x3' : 'c', 'x4' : 'c', 'x5' : 'c'}
#
# # run the search
# ic_algorithm = IC(RobustRegressionTest)
# graph = ic_algorithm.search(X, variable_types)
#
# graph.edges(data=True)