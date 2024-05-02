from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Matrix, Document

def editor(request):
    docid = int(request.GET.get('docid', 0))
    notes = Matrix.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        documents = request.POST.get('content', '')

        if docid > 0:
            note = Matrix.objects.get(pk=docid)
            note.title = title
            note.documents = documents
            note.save()

            return redirect('/?docid=%i' % docid)
        else:
            note = Matrix.objects.create(documents=documents)

            return redirect('/?docid=%i' % note.id)

    if docid > 0:
        note = Matrix.objects.get(pk=docid)
    else:
        note = ''

    context = {
        'docid': docid,
        'notes': notes,
        'note': note
    }

    return render(request, 'matrix/editor.html', context)

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document_detail.html'
    context_object_name = 'document'

document_detail_view = DocumentDetailView.as_view()