from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Matrix, Document
from .forms import NodeForm

from django.contrib.auth.decorators import login_required


@login_required
def editor(request):
    docid = int(request.GET.get('docid', 0))
    notes = Matrix.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        titles = request.POST.get('title', '')

        if docid > 0:
            note = Matrix.objects.get(pk=docid)
            note.title = titles
            # note.owner = owners
            # note.documents = documents
            note.save()

            return redirect(f'/editor/{docid}/markdown/')
        else:
            note = Matrix.objects.create(title=titles)

            #return redirect('/?docid=%i' % note.id)
            return redirect(f'/editor/{docid}/markdown/')

    if docid > 0:
        note = Matrix.objects.get(pk=docid)
    else:
        note = ''

    context = {
        'docid': docid,
        'notes': notes,
        'note': note
    }

    return render(request, "matrix/editor.html", context)


def editor2(request):
    # docid = int(request.GET.get('docid', 0))
    # notes = Matrix.objects.all()
    docs = Document.objects.all()
    

    if request.method == 'POST':
        # docid = int(request.POST.get('docid', 0))
        # file_names = request.POST.get('file_name', '')
        # file_content = request.POST.get('file_contents', '')
        # matriix = request.POST.get('matrix')
        form = NodeForm(request.POST)

        # if docid > 0:
        if form.is_valid():
            save_data = form.cleaned_data
            return render(request, "matrix/new_node.html", {'form': form, 'saved_data': save_data})
            
            # note = Document.objects.get(pk=docid)
            # note.file_name = file_names
            # note.file_contents = file_content
            # note.matrix = matriix
            # note.save()

        else:
            # doc = Document.objects.create(file_name=file_names, file_contents=file_content, matrix=matriix)
            # note = Matrix.objects.create(documents=documents)
            form = NodeForm()
            # return redirect('blank_text_field')

    # if docid > 0:
    #     note = Matrix.objects.get(pk=docid)
    # else:
    #     note = ''

    # context = {
    #     'document': docs,
    #     # 'notes:': notes,
    # }

    return render(request, "matrix/new_node.html")


    #         return redirect('/?docid=%i' % docid)
    #     else:
    #         note = Matrix.objects.create(documents=documents)

    #         return redirect('/?docid=%i' % note.id)

    # if docid > 0:
    #     note = Matrix.objects.get(pk=docid)
    # else:
    #     note = ''

    # context = {
    #     'docid': docid,
    #     'notes': notes,
    #     'note': note
    # }

    # return render(request, 'matrix/editor.html', context)

@login_required
def markdown_editor(request, docid):
    try:
        matrix = Matrix.objects.get(pk=docid, owner=request.user)
    except:
        return redirect('/')

    if request.method == 'POST':
        file_name = request.POST.get('file_name', '')
        file_contents = request.POST.get('file_contents', '')

        document = Document.objects.create(
            file_name=file_name,
            file_contents=file_contents,
            owner=request.user
        )

        matrix.documents.add(document)
        return redirect(f'editor/{docid}/markdown/')
    
    context = {
        'matrix': matrix
    }

    return render(request, "matrix/markdown_editor.html", context)



class DocumentDetailView(DetailView):
    model = Document
    template_name = "document_detail.html"
    context_object_name = "document"

document_detail_view = DocumentDetailView.as_view()