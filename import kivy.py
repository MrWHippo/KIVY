import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class Application(App):
    def build(self):
        layout = GridLayout(cols=2)

        layout.add_widget(Label(text="First Number"))
        self.firstNumberInput = TextInput(multiline=False)
        layout.add_widget(self.firstNumberInput)

        layout.add_widget(Label(text="Second Number"))
        self.secondNumberInput = TextInput(multiline=False)
        layout.add_widget(self.secondNumberInput)

        self.MultiplyButton = Button(text="Multiply")
        self.MultiplyButton.bind(on_press=self.handle_click)
        layout.add_widget(self.MultiplyButton)
        self.resultLabel = Label(text="")

        self.AddButton = Button(text="Add")
        self.AddButton.bind(on_press=self.add)
        layout.add_widget(self.AddButton)
        self.resultLabel = Label(text="")

        self.SubButton = Button(text="Subtract")
        self.SubButton.bind(on_press=self.sub)
        layout.add_widget(self.SubButton)
        self.resultLabel = Label(text="")

        self.DivButton = Button(text ="Divide")
        self.DivButton.bind(on_press=self.div)
        layout.add_widget(self.DivButton)
        self.resultLabel = Label(text="")
        layout.add_widget(self.resultLabel)


        return layout


    def handle_click(self, instance):
        result = self.get_first_number() * self.get_second_number()
        self.resultLabel.text = "Result: " + str(result)
    
    def add(self, instance):
        result = self.get_first_number() + self.get_second_number()
        self.resultLabel.text = "Result: " + str(result)
    
    def sub(self, instance):
        result = self.get_first_number() - self.get_second_number()
        self.resultLabel.text = "Result: " + str(result)

    def div(self, instance):
        result = self.get_first_number() / self.get_second_number()
        self.resultLabel.text = "Result: " + str(result)

    def get_first_number(self):
        return float(self.firstNumberInput.text)

    def get_second_number(self):
        return float(self.secondNumberInput.text)
    
    

if __name__ == "__main__":
    myApp = Application()
    myApp.run()




