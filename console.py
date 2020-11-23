import pdb 
import repositories.task_repository as task_repository 
from models.task import Task

task_1 = Task("Walk Dog", "Jack Jarvis", 60)

task_2 = Task("Feed Cat", "Victor McDade", 5)

task_repository.save(task_1)


pdb.set_trace()