import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class Application(App):
    def build(self):
        self.float = False
        layout = GridLayout(cols=2)

        layout.add_widget(Label(text="First Number", ))
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


        self.powerButton = Button(text="Power")
        self.powerButton.bind(on_press=self.power)
        layout.add_widget(self.powerButton)
        self.resultLabel=Label(text="")

        self.rootButton = Button(text="Root")
        self.rootButton.bind(on_press=self.rooted)
        layout.add_widget(self.rootButton)
        self.resultLabel=Label(text="")


        layout.add_widget(self.resultLabel)
        self.ErrorMessage=Label(text="")
        layout.add_widget(self.ErrorMessage)
        return layout


    def handle_click(self, instance):
        if self.valid():
            self.float = True
            result = self.get_first_number() * self.get_second_number()
            self.resultLabel.text = "Result: " + str(result)
    
    def add(self, instance):
        if self.valid():
            self.float = True
            result = self.get_first_number() + self.get_second_number()
            self.resultLabel.text = "Result: " + str(result)
    
    def sub(self, instance):
        if self.valid():
            self.float = True
            result = self.get_first_number() - self.get_second_number()
            self.resultLabel.text = "Result: " + str(result)

    def div(self, instance):
        if self.valid():
            self.float = True
            result = self.get_first_number() / self.get_second_number()
            self.resultLabel.text = "Result: " + str(result)
    
    def power(self, instance):
        if self.valid():
            self.float = False
            result= self.get_first_number() ** self.get_second_number()
            self.resultLabel.text = "Result: " + str(result)
    
    def rooted(self, instance):
        if self.valid():
            self.float = False
            result = self.get_first_number() ** (1/self.get_second_number())
            self.resultLabel.text = "Result: " + str(result)

    def get_first_number(self):
        if self.float == True:
            return float(self.firstNumberInput.text)
        else:
            return int(self.firstNumberInput.text)
    def get_second_number(self):
        if self.float == True:
            return float(self.secondNumberInput.text)
        else:
            return int(self.secondNumberInput.text)

    def valid(self):
        if self.get_first_number() != None and self.get_second_number() != None:
            if self.get_first_number() != 0 and self.get_second_number() != 0:
                return True
            else:
                self.ErrorMessage.text = "Error, Enter a number more than zero"
        else:
            self.ErrorMessage.text = "Error, please enter 2 numbers"
        
        return False

if __name__ == "__main__":
    myApp = Application()
    myApp.run()




