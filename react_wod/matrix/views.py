from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from .models import Matrix, Document
from .forms import MatrixForm, NodeForm


def editor(request):
    action = request.GET.get('action', 'edit')
    docid = int(request.GET.get('docid', 0))
    matrices = Matrix.objects.all()
    note, documents, context = None, None, {}

 
    if action == 'new_matrix':
        if request.method == 'POST':
            form = MatrixForm(request.POST)
            if form.is_valid():
                new_matrix = form.save()
                return redirect('matrix:document_detail', pk=new_matrix.id)
        else:
            form = MatrixForm()
        return render(request, 'matrix/new_matrix.html', {'form': form})

    elif action == 'new_node':
        if request.method == 'POST':
            form = NodeForm(request.POST)
            if form.is_valid():
                new_node = form.save()
                return redirect('matrix:document_detail', pk=new_node.id)
        else:
            form = NodeForm()
        return render(request, 'matrix/new_node.html', {'form': form})
    else:
        # fetch for specific document first to see if it exists
        if docid > 0:
            note = get_object_or_404(Document, pk=docid)
            documents = Document.objects.filter(matrix=note.matrix).all() if note.matrix else Document.objects.none()
        context = {
            'docid': docid,
            'matrices': matrices,
            'note': note,
            'documents': documents if docid > 0 else None
        }
 
    return render(request, 'matrix/editor.html', context)


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document_detail.html'
    context_object_name = 'document'


document_detail_view = DocumentDetailView.as_view()