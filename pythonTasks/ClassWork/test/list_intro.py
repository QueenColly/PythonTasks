task_list = []

id_count = 1

def count_task():

    return len(task_list)

def create_task(title,content,id_count):

    new_list = (id_count, title, content)

    task_list_append(new_list)

    id_count += 1

    return 0
