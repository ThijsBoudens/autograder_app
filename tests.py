import importlib
import traceback
import os
import sys
import copy
from collections import Counter
import math


function_names = ['balanced', 'firstPrime', 'alphabetical', 'dinner', 'standings']

function_inputs = {
	'balanced': {
		'args': [('HellO Anna!'), ('a BALANCED() woooord?'), ('a b c d e f.'), ('a b c d E f e E'), ('ac')]
	},
	'firstPrime': {
		'args': [(6),(100),(233),(888),(89)]
	},
	'alphabetical':{
		'args': [(['a', 'b', 'c']),(['a', 'c', 'b']),(['aeroplane', 'asparagus', 'aspirine']),(['BEER', 'water', 'Wine']),
		(['Beef', 'pasta', 'Ramen', 'STEw', 'Wagyu steak']), (['Beef', 'pasta', 'Ramen', 'STEw', 'Aspirine'])]
	}, 
	'dinner': {
		'args': [({'pasta': 150, 'tomato': 10, 'oil': 50}, {'pasta':500, 'tomato': 11, 'oil': 100, 'salt': 20}),
		 ({'beef': 1000, 'wine': 100, 'onion': 1}, {'pasta':500, 'tomato': 11, 'oil': 100, 'salt': 20}),
		 ({'ramen': 200, 'broth': 500, 'pork': 200, 'egg': 2}, {'ramen':500, 'broth': 500, 'pork': 200, 'salt': 20, 'egg':1}), 
		 ({'flour': 200, 'water': 200}, {'ramen':500, 'broth': 500, 'pork': 200, 'salt': 20, 'egg':1}), 
		 ({'flour': 200, 'water': 200}, {'flour':300, 'water': 500, 'pork': 200, 'salt': 200, 'egg':10})]

	},
	'standings': {
		'args': [('test1.txt'), ('test2.txt'), ('test3.txt')]

	}
}


function_outputs = {
	'balanced': [(False),(True),(False),(True),(True)],
	'firstPrime': [(7),(101),(239),(907),(97)],
	'alphabetical':[(True), (False), (True), (True), (True), (False)],
	'dinner': [(True), (False), (False), (False), (True)],
	'standings': [('Barcelona'), ('Napoli'), ('Livorno')]

}