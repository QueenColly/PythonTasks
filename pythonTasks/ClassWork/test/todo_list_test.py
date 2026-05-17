from unittest import TestCase
import list_intro

class ToDOListTest(TestCase):

    def test_that_no_task_in_todo_list(self):

        all_task = list_intro.count_task()
#        self.assertNull(all_task)
        self.assertEqual(all_task, 0)

    def test_that_task_is_created(self):

        title = "Write code"

        content = "Write EOB's assignment snacks"

        confirmation_code = create_task(title, content, 1)

        available_task = count_task(0)

        task = create_task(title,content)

        self.assertEqual(confirmation_code , 0)
 #       self.assertEquals(task[1], content)


