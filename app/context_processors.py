from .models import Pagina

def dados_globais(request):
    """
    Disponibiliza as informações da Pagina (Logo, Telefone, etc)
    em todos os templates do site, inclusive no base.html.
    """
    try:
        # Pega a primeira configuração ou retorna vazio se não tiver nada cadastrado
        info = Pagina.objects.first()
    except:
        info = None
        
    return {
        'pagina': info
    }