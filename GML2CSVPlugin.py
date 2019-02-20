import pandas as pd
import sys
import networkx as nx

class GML2CSVPlugin:
	def input(self, filename):
		self.myfile = filename


	def run(self):
		graph_gml = nx.read_gml(self.myfile)
		self.panda_df = nx.to_pandas_adjacency(graph_gml)


	def output(self, filename):
		self.panda_df.to_csv(filename, index=False)