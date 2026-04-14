import pandas as pd
import importlib
import traceback
import os
import sys
import copy
from collections import Counter
import math


paris_cwd = os.getcwd()
inFolders = True

# os.chdir(cwd+'/'+'ans')
# sys.path.insert(0, '')

paris_outputFile = 'results.csv'


paris_questions = ['balanced', 'firstPrime', 'alphabetical', 'dinner', 'standings']

paris_inputs = {
	'balanced': {
		'nrArgs': 1,
		'args': ['HellO Anna!', 'a BALANCED() woooord?', 'a b c d e f.', 'a b c d E f e E', 'ac']
	},
	'firstPrime': {
		'nrArgs': 1,
		'args': [6,100,233,888, 89]
	},
	'alphabetical':{
		'nrArgs': 1,
		'args': [['a', 'b', 'c'],['a', 'c', 'b'],['aeroplane', 'asparagus', 'aspirine'],['BEER', 'water', 'Wine'],['Beef', 'pasta', 'Ramen', 'STEw', 'Wagyu steak'], ['Beef', 'pasta', 'Ramen', 'STEw', 'Aspirine']]
	}, 
	'dinner': {
		'nrArgs': 2,
		'args': [{'pasta': 150, 'tomato': 10, 'oil': 50}, {'pasta':500, 'tomato': 11, 'oil': 100, 'salt': 20}, {'beef': 1000, 'wine': 100, 'onion': 1}, {'pasta':500, 'tomato': 11, 'oil': 100, 'salt': 20}, {'ramen': 200, 'broth': 500, 'pork': 200, 'egg': 2}, {'ramen':500, 'broth': 500, 'pork': 200, 'salt': 20, 'egg':1}, {'flour': 200, 'water': 200}, {'ramen':500, 'broth': 500, 'pork': 200, 'salt': 20, 'egg':1}, {'flour': 200, 'water': 200}, {'flour':300, 'water': 500, 'pork': 200, 'salt': 200, 'egg':10}]

	},
	'standings': {
		'nrArgs': 1,
		'args': ['test1.txt', 'test2.txt', 'test3.txt']

	}


}
paris_outputs = {
	'balanced': [False,True,False,True, True],
	'firstPrime': [7,101,239,907,97],
	'alphabetical': [True, False, True, True, True, False],
	'dinner': [True, False, False, False, True],
	'standings': ['Barcelona', 'Napoli', 'Livorno']

}

cols = ['surname', 'firstname']
cols.extend(paris_questions)

paris_results = pd.DataFrame(columns=cols)


def getAnswers(mod, q):
	print('running', q, mod, '----------')
	sys.stdout = open(os.devnull, 'w')
	sys.path.append('ans/')
	module = importlib.import_module(mod)
	# print("hi")
	paris_result = []
	try:
		func = getattr(module, q)
		ind = 0
		if paris_inputs[q]['nrArgs'] == 2:
			for ind in range(len(paris_inputs[q]['args'])//2):
				res = func(copy.deepcopy(paris_inputs[q]['args'][2*ind]), copy.deepcopy(paris_inputs[q]['args'][2*ind+1]))
				# print('testing for ', paris_inputs[q]['args'][2*ind], paris_inputs[q]['args'][2*ind+1])
				# print(res)
				# print('----------')
				paris_result.append(res)
		elif paris_inputs[q]['nrArgs'] == 3:
			for ind in range(len(paris_inputs[q]['args'])//3):
				res = func(copy.deepcopy(paris_inputs[q]['args'][3*ind]), copy.deepcopy(paris_inputs[q]['args'][3*ind+1]), copy.deepcopy(paris_inputs[q]['args'][3*ind+2]))
				# print('testing for ', paris_inputs[q]['args'][2*ind], paris_inputs[q]['args'][2*ind+1])
				# print(res)
				# print('----------')
				paris_result.append(res)
		else:
			for ind in range(len(paris_inputs[q]['args'])):
				res = func(copy.deepcopy(paris_inputs[q]['args'][ind]))
				# print('testing for ', paris_inputs[q]['args'][ind])
				# print(res)
				# print('---')
				paris_result.append(res)
		# paris_result.append(res)
	except Exception as e:
		# print("Encountered error: ", traceback.format_exc())
		paris_result.append('crash')
	sys.path.remove('ans/')
	sys.stdout = sys.__stdout__
	# print("----")
	# print(paris_result)
	# print(paris_outputs[q])
	# print(paris_result == paris_outputs[q], ' are they equal')
	# print('----')
	if paris_result == paris_outputs[q]:
		return 20
	return 0
	

for answer in os.listdir(paris_cwd + '/ans'):
	if '.py' in answer:
		# print("old: ", answer)
		newFileName = answer[:-3].replace(".", "") + ".py"
		os.rename(paris_cwd + '/ans/' +answer,  paris_cwd + '/ans/' +newFileName)
		# print('answer:', newFileName)
		studentName = newFileName.split('_')[2]
		# print('studentName: ', studentName)
		res = []
		# module = answer.split('.')[0]
		module = newFileName[:-3]
		nombre = studentName.split(',')
		if len(nombre) == 2:
			res.append(nombre[0])
			res.append(nombre[1])
		else:
			res.append(nombre[0])
			res.append('')
		for q in paris_questions:
			try:
				score = getAnswers(module, q)
			except Exception as x:
				# print("crashed")
				# print(x)
				score = False
			res.append(score)
		# print(res)
		paris_results.loc[len(paris_results)] = res
		
paris_results.sort_values(by=['surname'], inplace=True)
paris_results.to_csv(paris_outputFile, index=False, header=True, mode='a', encoding='utf-8')
				
		
				

					
					