from django.shortcuts import redirect, render
from .models import Etudiant, Matiere, Note
from .forms import AjoutForm, AjoutEtudiantForm


# Create your views here.

def index(request):
    etudiants = Etudiant.objects.all()
    matieres = Matiere.objects.all()
    notes = Note.objects.order_by('id')
    moyennes = {}
    coef = 0

# Calcule des moyenne de chaque étudiant

    for values in etudiants.values():
        somme = 0
        for note in notes.values():
            if note['etudiant_id'] == values['id']:
                coefficient = matieres.get(pk=note['matiere_id']).coef
                somme += note['note'] * coefficient
                coef += coefficient

        moyennes[values['id']] = round(somme / coef, 2)

    # Création du formalaire de note
    form = AjoutForm()
    # Ajout de l'étudiant
    formEtudiant = AjoutEtudiantForm()

    return render(request, 'students/index.html',
                  {'etudiants': etudiants, 'matieres': matieres, 'notes': notes, 'moyennes': moyennes, 'form': form,
                   'formEtudiant': formEtudiant})


def ajout_note(request):
    if request.method == 'POST':
        form = AjoutForm(request.POST)

        # Si formulaire validé

        if form.is_valid():
            # Recuperation des données
            etudiant = form.cleaned_data['etudiant']
            matiere = form.cleaned_data['matiere']
            noteE = form.cleaned_data['note']
            # Verification si la note existe
            note = Note.objects.filter(etudiant=etudiant).filter(matiere=matiere)
            if not note.exists():
                # Ajout d'une note
                note = Note.objects.create(
                    etudiant=etudiant,
                    matiere=matiere,
                    note=noteE
                )
                note.save()
            else:
                # Modification d'un note existante
                note.update(note=noteE)

    return redirect('index')


def ajout_etudiant(request):
    matieres = Matiere.objects.all()

    if request.method == 'POST':
        form = AjoutEtudiantForm(request.POST)

    # Si formulaire validé
        if form.is_valid():
            #Recuperation des données
            name = form.cleaned_data['name']
            etudiant = Etudiant.objects.create(
                name=name
            )
            etudiant.save()
            # Création des notes
            for matiere in matieres.values():
                note = Note.objects.create(
                    etudiant=Etudiant.objects.get(name=name),
                    matiere=Matiere.objects.get(name=matiere['name']),
                    note=0.0
                )
                note.save()
    return redirect('index')
