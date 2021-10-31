from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.config import Config


#Config.set('graphics','resizable',0)
#Config.set('graphics','width',600)
#Config.set('graphics','height',400)

class MyApplication(App):

    def click(self, instance):
        self.my_label.text='1'
  

    def click_2(self, instance):
        self.my_label.text='2'
  

    def build(self):
        but_together = BoxLayout()
        my_grid = GridLayout(cols=1)

        my_but = Button(text='Кнопка 1', 
                        font_size=20, 
                        background_color='cyan', 
                        on_press=self.click)
        
        think_of_name = Button(text='Кнопка 2',
                               font_size=20, 
                               background_color='cyan',
                               on_press=self.click_2)
        
        self.my_label = Label(text='Метка',font_size=30)

        but_together.add_widget(my_but)
        but_together.add_widget(think_of_name)

        my_grid.add_widget(but_together)
        my_grid.add_widget(self.my_label)

        return my_grid

if __name__ == "__main__":
    MyApplication().run()