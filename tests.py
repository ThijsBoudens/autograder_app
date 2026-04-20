test_cases = {
	"Question 1": {
		"function_name": "balanced",
		'inputs': [('HellO Anna!'), ('a BALANCED() woooord?'), ('a b c d e f.'), ('a b c d E f e E'), ('ac')],
		'outputs': [(False),(True),(False),(True),(True)],
		"rubrics":{
			"Rubric 1": {
				"title": "return correct type",
				"points": 5
			}, 
			"Rubric 2": {
				"title": "make appropriate calculation",
				"points": 5
			},
			"Rubric 3": {
				"title": "make appropriate conditionals",
				"points": 5
			},
			"Rubric 4": {
				"title": "make appropriate loop",
				"points": 5
			}
		}

	}, 
	"Question 2": {
		"function_name": "firstPrime",
		'inputs': [(6),(100),(233),(888),(89)],
		'outputs': [(7),(101),(239),(907),(97)],
		"rubrics":{
			"Rubric 1": {
				"title": "return correct type",
				"points": 5
			}, 
			"Rubric 2": {
				"title": "make appropriate calculation",
				"points": 5
			},
			"Rubric 3": {
				"title": "make appropriate conditionals",
				"points": 5
			},
			"Rubric 4": {
				"title": "make appropriate loop",
				"points": 5
			}
		}
	}, 
	"Question 3": {
		"function_name": "alphabetical",
		'inputs': [(['a', 'b', 'c']),(['a', 'c', 'b']),(['aeroplane', 'asparagus', 'aspirine']),
		(['BEER', 'water', 'Wine']),(['Beef', 'pasta', 'Ramen', 'STEw', 'Wagyu steak']), 
		(['Beef', 'pasta', 'Ramen', 'STEw', 'Aspirine'])],
		'outputs':[(True), (False), (True), (True), (True), (False)],
		"rubrics":{
			"Rubric 1": {
				"title": "return correct type",
				"points": 5
			}, 
			"Rubric 2": {
				"title": "make appropriate calculation",
				"points": 5
			},
			"Rubric 3": {
				"title": "make appropriate conditionals",
				"points": 5
			},
			"Rubric 4": {
				"title": "make appropriate loop",
				"points": 5
			}
		}
	}, 
	"Question 4": {
		"function_name": "dinner",
		'inputs': [({'pasta': 150, 'tomato': 10, 'oil': 50}, {'pasta':500, 'tomato': 11, 'oil': 100, 'salt': 20}),
	 ({'beef': 1000, 'wine': 100, 'onion': 1}, {'pasta':500, 'tomato': 11, 'oil': 100, 'salt': 20}),
	 ({'ramen': 200, 'broth': 500, 'pork': 200, 'egg': 2}, {'ramen':500, 'broth': 500, 'pork': 200, 'salt': 20, 'egg':1}), 
	 ({'flour': 200, 'water': 200}, {'ramen':500, 'broth': 500, 'pork': 200, 'salt': 20, 'egg':1}), 
	 ({'flour': 200, 'water': 200}, {'flour':300, 'water': 500, 'pork': 200, 'salt': 200, 'egg':10})],
	 	'outputs': [(True), (False), (False), (False), (True)],
		"rubrics":{
			"Rubric 1": {
				"title": "return correct type",
				"points": 5
			}, 
			"Rubric 2": {
				"title": "make appropriate calculation",
				"points": 5
			},
			"Rubric 3": {
				"title": "make appropriate conditionals",
				"points": 5
			},
			"Rubric 4": {
				"title": "make appropriate loop",
				"points": 5
			}
		}
	}, 
	"Question 5": {
		"function_name": "standings",
		'inputs': [('test1.txt'), ('test2.txt'), ('test3.txt')],
		'outputs': [('Barcelona'), ('Napoli'), ('Livorno')],
		"rubrics":{
			"Rubric 1": {
				"title": "return correct type",
				"points": 5
			}, 
			"Rubric 2": {
				"title": "make appropriate calculation",
				"points": 5
			},
			"Rubric 3": {
				"title": "make appropriate conditionals",
				"points": 5
			},
			"Rubric 4": {
				"title": "make appropriate loop",
				"points": 5
			}
		}
	}
}
