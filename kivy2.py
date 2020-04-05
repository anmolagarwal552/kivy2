from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.inner_grid = GridLayout()
        self.inner_grid.cols = 2

        self.inner_grid.add_widget(Label(text="Username: "))
        self.usr = TextInput(multiline=False)
        self.inner_grid.add_widget(self.usr)

        self.inner_grid.add_widget(Label(text="Password: "))
        self.passw = TextInput(multiline=False)
        self.inner_grid.add_widget(self.passw)

        self.add_widget(self.inner_grid)

        self.button = Button(text="Login")
        self.button.bind(on_press=self.login)
        self.add_widget(self.button)


    def login(self, instance):
        print("Login Successfull")

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()