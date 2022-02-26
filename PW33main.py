from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):

        def build(self):
                fl=FloatLayout(size=(200, 200))
                fl.add_widget(Button(
                        text="Кнопка 1",
                        font_size=20,
                        on_press=self.btn_press,
                        background_color=[0,1,0,1],
                        background_normal='',
                        size_hint=(1, .25),
                        pos_hint={'center_x': .5, 'center_y': .65}));

                fl.add_widget(Button(
                        text="Кнопка 2",
                        font_size=20,
                        on_press=self.btn_press,
                        background_color=[1,0,0,1],
                        background_normal='',
                        size_hint=(1, .25),
                        pos_hint={'center_x': .5, 'center_y': .35}));
                return fl
        def btn_press(self, instance):        
                instance.text='Я нажата'

if __name__=="__main__":
        myApp().run()
