from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from .models import Matrix, Document

def editor(request):
    docid = int(request.GET.get('docid', 0))
    matrices = Matrix.objects.all()
    note, documents = None, None
 
    # Moved to top so we fetch for specific document first to see if it exists
    if docid > 0:
        note = get_object_or_404(Document, pk=docid)
        documents = Document.objects.filter(matrix=note.matrix).all() if note.matrix else Document.objects.none()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        matrix_id = int(request.POST.get('matrix', 0))
 
        if docid > 0:
            note = get_object_or_404(Document, pk=docid)
            note.file_name = title
            note.file_contents = content
            note.save()
        else:
            # select the matrix
            matrix = get_object_or_404(Matrix, pk=matrix_id) if matrix_id else None
            note = Document.objects.create(
                file_name=title,
                file_contents=content,
                matrix=matrix
            )
        
        return redirect('matrix:document_detail', pk=note.id)

    context = {
        'docid': docid,
        'matrices': matrices,
        'note': note,
        'documents': documents if docid > 0 else None
    }
 
    return render(request, 'node.html', context)

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document_detail.html'
    context_object_name = 'document'

document_detail_view = DocumentDetailView.as_view()