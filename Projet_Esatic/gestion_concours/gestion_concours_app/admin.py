
from django.contrib import admin
from .models import Candidat

class CandidatAdmin(admin.ModelAdmin):
    list_display = (
        'nom', 'prenoms', 'email', 'telephone',
        'concours_choisi', 'specialite', 'niveau_etudes', 'date_inscription'
    )
    search_fields = ('nom', 'prenoms', 'email', 'telephone')
    list_filter = ('concours_choisi', 'specialite', 'niveau_etudes', 'date_inscription')
    readonly_fields = ('date_inscription',)

    # Pour afficher les fichiers dans le détail
    def extrait_naissance_link(self, obj):
        if obj.extrait_naissance:
            return f"<a href='{obj.extrait_naissance.url}' target='_blank'>Voir</a>"
        return "Aucun fichier"
    extrait_naissance_link.allow_tags = True
    extrait_naissance_link.short_description = "Extrait de naissance"

admin.site.register(Candidat,CandidatAdmin)
