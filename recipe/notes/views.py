from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from recette.models import Recette
from .forms import NoteForm
from .models import Note

@login_required
def ajouter_note(request, pk):
    # Récupérer la recette spécifique avec l'ID (pk)
    recette = get_object_or_404(Recette, pk=pk)

    if request.method == 'POST':
        # Créer une instance de NoteForm avec les données de la requête POST
        form = NoteForm(request.POST)

        # Vérifier si le formulaire est valide
        if form.is_valid():
            # Créer une instance de Note sans l'enregistrer dans la base de données
            note = form.save(commit=False)

            # Assigner la recette et l'utilisateur à la note
            note.recette = recette
            note.user = request.user

            # Enregistrer la note dans la base de données
            note.save()

            # Rediriger vers la page de détails de la recette
            return redirect('detail_recette', pk=recette.pk)
    else:
        # Créer une instance de NoteForm vide
        form = NoteForm()

    context = {
        'recette': recette,
        'form': form,
    }

    return render(request, 'ajouter_note.html', context)