




def store_task():
	db = []
	return db

def add_task(db,task):
	db.append(task)
	# Task added!


def delete_task(db, del_task):

	if del_task in db: 
		inDex = db.index(del_task)
		del db[inDex]
		print(f'{del_task} has been deleted!')
	else:
		print('Task not found!')


def view_task(db):

	for task in db:
		print(task)
		

def search_task(db, search_task):

	if search_task in db:
		print(f'Searched: {search_task}')
	else:
		print('Task not found!')


def update_task(db, bef_task, aft_task):

	if bef_task in db:
		inDex = db.index(bef_task)
		db[inDex] = aft_task
	else:
		print('Task not found!')


main = store_task()

add_task(main, 'Task 1')
add_task(main, 'Task 2')
add_task(main, 'Task 3')
add_task(main, 'Task 4')
add_task(main, 'Task 5')
update_task(main, 'Task 1', 'New Task 1')
update_task(main, 'Task 2', 'New Task 2')
# view_task(main)
delete_task(main, 'Task 5')
view_task(main)

