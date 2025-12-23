import flet as ft

class TaskApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.task_input = ft.TextField(
            hint_text="أدخل مهمة جديدة...",
            expand=True,
            border_radius=15,
            bgcolor="#15ffffff",
            color="white",
            border_color="white24"
        )
        self.tasks_list = ft.Column()

    def add_task(self, e):
        if self.task_input.value:
            task = ft.Container(
                content=ft.Row([
                    ft.Checkbox(check_color="pink"),
                    ft.Text(self.task_input.value, expand=True, color="white"),
                    ft.IconButton(ft.icons.DELETE_OUTLINE, icon_color="red400", on_click=lambda _: self.delete_task(task))
                ]),
                padding=10,
                border_radius=15,
                bgcolor="#22ffffff",
                blur=ft.Blur(10, 10, ft.BlurStyle.INNER),
                border=ft.border.all(1, "white10")
            )
            self.tasks_list.controls.append(task)
            self.task_input.value = ""
            self.update()

    def delete_task(self, task):
        self.tasks_list.controls.remove(task)
        self.update()

    def build(self):
        return ft.Column(
            controls=[
                ft.Row([self.task_input, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_task, bgcolor="pink600")]),
                self.tasks_list
            ]
        )

def main(page: ft.Page):
    page.title = "Glassy Todo"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    
    # خلفية متدرجة ثابتة للجوال
    page.bgcolor = "#0f0c29"
    
    app = TaskApp()
    page.add(
        ft.Text("مهامي", size=40, weight="bold", color="white"),
        ft.Divider(height=10, color="transparent"),
        app.build()
    )

if __name__ == "__main__":
    ft.app(target=main)
