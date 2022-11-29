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


        self.MultiplyButton = Button(text="Convert to F")
        self.MultiplyButton.bind(on_press=self.convertF)
        layout.add_widget(self.MultiplyButton)
        self.resultLabel = Label(text="")
        layout.add_widget(self.resultLabel)


        self.MultiplyButton = Button(text="Convert to C")
        self.MultiplyButton.bind(on_press=self.convertC)
        layout.add_widget(self.MultiplyButton)
        self.resultLabel = Label(text="")
        layout.add_widget(self.resultLabel)

        return layout
    
    def convertF(self, instance):
        result = 1.8 * self.get_number() + 32
        self.resultLabel.text = "Result: " + str(result)

    def convertC(self, instance):
        result = (self.get_number() - 32)/1.8
        self.resultLabel.text = "Result: " + str(result)

    def get_number(self):
        return float(self.firstNumberInput.text)


if __name__ == "__main__":
    myApp = Application()
    myApp.run()