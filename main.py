import typer
import rich
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos,delete_todo,insert_todo,complete_todo,update_todo


console = Console()
app = typer.Typer()


@app.command()
def add(task:str,category:str):
    typer.echo(f'adding{task},{category}')
    todo = Todo(task,category)
    insert_todo(todo)
    show()

@app.command()
def delete(position : int):
    typer.echo(f'deleting{position}')
    #Indices in database begins at 0
    delete_todo(position-1)
    show()

@app.command()
def update(position: int, task:str= None,category:str = None):
    typer.echo(f'updating{position}')
    update_todo(position-1,task,category)
    show()

@app.command()
def complete(position : int):
    typer.echo(f'complete {position}')   
    complete_todo(position-1) 
    show()

@app.command()
def show():
    tasks = get_all_todos()
    console.print('[bold magenta]TASK-TRACKER[/bold magenta]!','💻',justify='center')

    table = Table(show_header=True,header_style="bold violet")
    table.add_column("Sno.",style='cyan',justify='center',width=5)
    table.add_column("Tasks",style='yellow',min_width=20,justify='center')
    table.add_column('Category',min_width=15,justify='center')
    table.add_column('Status',min_width=15,justify='center')
    
    for id,tsk in enumerate(tasks,start=1):
        is_done_str = '✅' if tsk.status == 2 else '❌'
        table.add_row(str(id),tsk.task[0],f'{tsk.category}',is_done_str)
    console.print(table)

if __name__ =='__main__':
    app()