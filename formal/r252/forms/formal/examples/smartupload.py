import formal
from formal.examples import main

class SmartUploadFormPage(main.FormExamplePage):

    title = 'Smart File Upload'
    description = 'Smart uploading of files where the file is "carried across" when the validation fails'
    
    def form_example(self, ctx):
        form = formal.Form()
        form.addField('required', formal.String(required=True))
        form.addField('file', formal.File(), formal.FileUploadWidget)
        form.addAction(self.submitted)
        return form
    
    def submitted(self, ctx, form, data):
        print form, data
