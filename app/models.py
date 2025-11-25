from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Pagina(models.Model):
    # O verbose_name não é o dado do site, ele é apenas a "Etiqueta" (Rótulo) do campo que vai aparecer para você lá no Painel Administrativo.

    nome_do_site = models.CharField(max_length=100, verbose_name="Nome do Site")
    logo_do_site = models.ImageField(upload_to='logos/', verbose_name="Logo do Site", validators=[FileExtensionValidator(['pdf', 'svg', 'png', 'jpg', 'jpeg'])])
    texto_chamada = models.TextField(verbose_name="Texto da Chamada (Hero)")
    texto_sobre = models.TextField(verbose_name="Texto Sobre Nós")
    imagem_sobre = models.ImageField(upload_to='sobre/', verbose_name="Imagem da Seção Sobre")

    endereco = models.TextField(verbose_name="Endereço Completo")
    email = models.EmailField(verbose_name="E-mail de Contato")
    whatsapp = models.CharField(max_length=20, verbose_name="Número do WhatsApp")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_do_site

    class Meta:
        verbose_name = "Configuração da Página"
        verbose_name_plural = "Configurações da Página"