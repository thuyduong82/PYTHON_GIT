from nicegui import ui 

def example():
    ui.notify("button works!")

def example2():
    ui.notify("button2")

buttons = {
    "button1": example,
    "button2": example2,

}

with ui.element("div").classes("flex items-center justify-center flex-col h-screen w-full"):
    ui.label("Hi!").classes("text-teal-500 text-4xl")
    ui.label("Bye!").style("color:red")

    with ui.grid(columns=3):#vytvori grid s 3 sloupci
        for name,func in buttons.items():
            ui.button(name, on_click=func)

    ui.button("click me", on_click=example)

ui.run(native=True)