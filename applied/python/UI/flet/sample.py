import flet as ft
from flet import Checkbox, FloatingActionButton, Icons, Page, TextField


## this is the basic startup program
def hello_world_main(page: ft.Page):
    page.add(ft.Text(value="Hello World!"))

def main(page: ft.Page):
    def add_clicked(e):
        # page.add(Checkbox(label=new_task.value))
        tasks_view.controls.append(Checkbox(label=new_task.value))
        new_task.value = ""
        view.update()
        # page.update()

    new_task = TextField(hint_text="Whats needs to be done?", expand=True)
    tasks_view = ft.Column()
    view = ft.Column(
        width=600,
        controls=[
            new_task,
            ft.FloatingActionButton(icon=Icons.ADD, on_click=add_clicked),
            tasks_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)
    # page.add(new_task, FloatingActionButton(icon=Icons.ADD, on_click=add_clicked))

ft.run(main)