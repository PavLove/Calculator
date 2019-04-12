# импортируем саму структуру приложения из библиотеки Киви
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 500)
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)
#    Создаем класс
class CalculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if( self.formula == '0' ):
            self.formula = ''

        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if( str(instance.text) == 'x'):
            self.formula +='*'
        else:
            self.formula += str( instance.text )
        self.update_label()

    def calc_result(self,instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = '0'

    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical', padding=3)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))
 #       Добавляем метод Label в класс через self, чтобы вызывать его из других методов
        self.lbl = Label(text='0', font_size=50, size_hint=(1, .4),
                         halign='right', valign='center',
                         color=[.32, .85, .94, 1],
                         text_size=(400 - 50, 500 * .4 - 50))
        bl.add_widget(self.lbl)
        gl.add_widget(Button(text='7', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='8', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='9', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='x', background_color=[.32, .85, .94, 1],
                             on_press=self.add_operation))
        gl.add_widget(Button(text='4', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='5', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='6', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='-', background_color=[.32, .85, .94, 1],
                             on_press=self.add_operation))
        gl.add_widget(Button(text='1', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='2', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='3', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='+', background_color=[.32, .85, .94, 1],
                             on_press=self.add_operation))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='0', background_color=[.32, .85, .94, 1],
                             on_press=self.add_number))
        gl.add_widget(Button(text='.', background_color=[.32, .85, .94, 1],
                             on_press=self.add_operation))
        gl.add_widget(Button(text='=', background_color=[.32, .85, .94, 1],
                             on_press=self.calc_result))
        bl.add_widget(gl)
        return bl
if __name__ == '__main__':
    CalculatorApp().run()
