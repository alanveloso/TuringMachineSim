#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import optparse
from collections import defaultdict
from copy import deepcopy
	
def trace(tapesAmount, currentDescriptions):
	word = ''
	for state, tapes, index in currentDescriptions: 
		word += state+' - '
		for i in range(tapesAmount):
			tr = tapes[i][:]
			tr.insert(index[i]+1,']')
			tr.insert(index[i],'[')
			word += ''.join(tr) + '\t\t'
		word += '\n'
	return word

def run(fileName, word, printTrace, clearBlanks, printResult):
	tm, delta = open(fileName), defaultdict(list)
	tm.readline()
	tm.readline()
	tapesAmount = len(tm.readline().split('-')[0].split())-1 # tko sm mislu
	tm.seek(0)
	state, final= tm.readline().split()[1],tm.readline().split()[1:]
	[delta[tuple(i.split()[:tapesAmount+1])].append(i.split()[tapesAmount+2:]) for i in tm]
	tapes = [list(word)] #tapes 1
	for i in range(tapesAmount-1):
		tapes.append(['_']) #tapes i
	index = [0 for i in range(tapesAmount)]
	shift = ['S' for i in range(tapesAmount)]
	currentDescriptions = [(state, tapes, index)]
	while(currentDescriptions!=[]):
		if printTrace:
			print trace(tapesAmount, currentDescriptions)
		newDescriptions = []
		for state, tapes, index in currentDescriptions:
			t = [state]
			for i in range(tapesAmount):
				t.append(tapes[i][index[i]])
			for deltaOption in delta[tuple(t)]:
				newState = deltaOption[0]
				newTapes = deepcopy(tapes)
				newIndex = deepcopy(index)
				for i in range(tapesAmount):
					newTapes[i][newIndex[i]] = deltaOption[i+1]
					shift[i] = deltaOption[i+1+tapesAmount]
					
				for i in range(tapesAmount):
					if clearBlanks:
						j = len(newTapes[i])-1
						while j > 3 and newTapes[i][j] == '_' and j > newIndex[i]: 
							j -= 1
						j = 0 if j<2 else j-1
						k = 0
						while k < newIndex[i]-2 and newTapes[i][k] == '_':
							k += 1
						newTapes[i] = newTapes[i][k:j+3]
						newIndex[i] -= k

					if newIndex[i] == 0:
						newTapes[i].insert(0, '_')
						newIndex[i] += 1
					if newIndex[i] == len(newTapes[i])-1:
						newTapes[i].append('_')

					if shift[i] == 'L':
						newIndex[i] -= 1
					if shift[i] == 'R':
						newIndex[i] += 1
				newDescriptions.append((newState, newTapes, newIndex))
				if any(i in newState for i in final):
					if printTrace:
						print trace(tapesAmount, newDescriptions)
					if printResult:
						print '\n\nResult: '+''.join(newTapes[0])+'\n'
					return True
		currentDescriptions = newDescriptions
	return False

parser = optparse.OptionParser("usage: %prog [options] word1 word2")
parser.add_option("-t", "--trace", dest="t", action="store_true", default=False, help="Set for trace turing machine")
parser.add_option("-r", "--result", dest="r", action="store_true", default=False, help="Print the output from the first track")
parser.add_option("-b", "--clearBlanks", dest="b", action="store_true", default=False, help="Clear unused blanks from tracks")
parser.add_option("-f", "--file", dest="f", type="string", help="File name for turing machine")
(options, args) = parser.parse_args()
if len(args) < 1:
	parser.print_help()
for word in args:
	if run(options.f, word, options.t, options.b, options.r):
		print "In the language" 
		print
	else:
		print "Not in the language"
		print
