import flet as ft

def main(page: ft.Page):
    page.title = "Glassy Tasks"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 700
    page.padding = 0
    
    # تنسيق الخطوط والألوان
    BG_COLOR = "#1a1a2e"
    GLASS_COLOR = "#22ffffff" # لون أبيض شفاف جداً
    
    # قائمة المهام
    tasks_view = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    def delete_task(task_container):
        tasks_view.controls.remove(task_container)
        page.update()

    def add_task(e):
        if not task_input.value:
            return
        
        # إنشاء بطاقة المهمة بتأثير زجاجي
        task_container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Checkbox(check_color=ft.colors.PINK, fill_color=ft.colors.WHITE70),
                    ft.Text(task_input.value, expand=True, size=16, color=ft.colors.WHITE),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
                        icon_color=ft.colors.PINK_200,
                        on_click=lambda _: delete_task(task_container)
                    ),
                ],
            ),
            padding=10,
            border_radius=15,
            bgcolor=GLASS_COLOR,
            blur=ft.Blur(10, 10, ft.BlurStyle.INNER), # تأثير التغبيش الزجاجي
            border=ft.border.all(1, ft.colors.WHITE24),
            margin=ft.margin.only(bottom=10)
        )
        
        tasks_view.controls.append(task_container)
        task_input.value = ""
        page.update()

    # حقل إدخال المهام بتصميم زجاجي
    task_input = ft.TextField(
        hint_text="ما هي مهمتك التالية؟",
        border=ft.InputBorder.NONE,
        filled=False,
        expand=True,
        color=ft.colors.WHITE,
        cursor_color=ft.colors.PINK,
    )

    # الواجهة الرئيسية
    main_container = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#0f0c29", "#302b63", "#24243e"], # خلفية متدرجة عميقة
        ),
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("مهامي اليومية", size=32, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                
                # صندوق الإدخال الزجاجي
                ft.Container(
                    content=ft.Row([task_input, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task, bgcolor=ft.colors.PINK_600)]),
                    padding=10,
                    border_radius=20,
                    bgcolor="#11ffffff",
                    blur=ft.Blur(15, 15, ft.BlurStyle.OUTER),
                    border=ft.border.all(1, ft.colors.WHITE10),
                ),
                
                ft.Divider(height=30, color=ft.colors.WHITE12),
                
                # عرض المهام
                tasks_view
            ]
        )
    )

    page.add(main_container)

ft.app(target=main)
  
