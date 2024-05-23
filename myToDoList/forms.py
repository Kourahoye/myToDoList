from django import forms

from myToDoList.models import Task

class TaskCreate(forms.ModelForm):
    title = forms.CharField(label="Title", widget = forms.TextInput,max_length = 30, min_length = 3,required = True)
    content = forms.CharField(label="Content", widget = forms.Textarea,min_length = 5)   
    done = forms.CharField(label="State", widget = forms.CheckboxInput,required=False)   
    class Meta:
        model = Task
        fields = ("title","content","done")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-input w-full rounded-md h-[25px] shadow-md ring ring-blue-200 rounded-md'
                                                           'hover:ring hover:ring-blue-400 border-transparent placeholder:text-slate-600 font-medium ',
                                                  'id': 'Title','placeholder':'Titre'})
        self.fields['content'].widget.attrs.update({'class': 'form-textarea w-full rounded-md h-fit shadow-md ring ring-blue-200 rounded-md'
                                                           'hover:ring hover:ring-blue-400 border-transparent placeholder:text-slate-600 font-medium',
                                                  'id': 'Content','placeholder':'Description'})
        self.fields['done'].widget.attrs.update({'class':'form-checkbox shadow-md rounded-full ring ring-blue-200 rounded-md'
                                                           'hover:ring hover:ring-blue-400 border-transparent','id':'State'})
