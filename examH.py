import networkx as nx
import sys


def correct_answer(value, m):
	if value == m:
		return "Yes"
	return "No"
		
line = sys.stdin.readline()
tc = int(line)
for i in range(tc):
	values = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	diffs = sys.stdin.readline().strip().split(" ")
	diffs_dict = dict()
	topics = sys.stdin.readline().strip().split(" ")
	topics_dict = dict()
	
	g = nx.DiGraph()
	diff_adjusted = ["%" + i + "%" for i in diffs]
	topics_adjusted = ["@" + i + "@" for i in topics]
	vertices = ["^s^"] + ["^t^"] + list(set(diff_adjusted)) + list(set(topics_adjusted))
	[g.add_node(v) for v in vertices]
	for j in range(values[1]):
		if diff_adjusted[j] in diffs_dict:
			diffs_dict[diff_adjusted[j]] += 1
		else:
			diffs_dict[diff_adjusted[j]] = 1
		if topics_adjusted[j] in topics_dict:
			topics_dict[topics_adjusted[j]] += 1
		else:
			topics_dict[topics_adjusted[j]] = 1
	for topic in topics_dict:
		g.add_edge("^s^", topic, capacity = topics_dict[topic])
	for diffs in diffs_dict:
		g.add_edge(diffs , "^t^", capacity = diffs_dict[diffs])
	
	questions_dict = dict()
	for j in range(values[0]):
		question = sys.stdin.readline().strip()
		question_string = question.split(" ")
		question_adjusted = "@" + question_string[1] + "@ %" + question_string[2] + "%"
		if (("@" + question_string[1] + "@") in topics_dict) and (("%" + question_string[2] + "%") in diffs_dict):
			if question_adjusted in questions_dict:
				questions_dict[question_adjusted] += 1
			else:
				questions_dict[question_adjusted] = 1
				
	for question in questions_dict:
		question_string = question.split(" ")
		g.add_edge(question_string[0], question_string[1], capacity = questions_dict[question])
		
	print(correct_answer(nx.maximum_flow_value(g,"^s^","^t^"), values[1]))
