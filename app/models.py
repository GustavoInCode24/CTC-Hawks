from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import MaxValueValidator, MinValueValidator

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

class Produto(models.Model):

    #Produto
    nome_produto = models.CharField(max_length=100 , verbose_name= "Nome do Produto")
    estoque_produto = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)],verbose_name="Estoque do Produto")
    preco_produto =  models.DecimalField(max_digits=5,decimal_places=2,verbose_name= "Preço do Produto")
    descricao_produto =  models.CharField(max_length=120,verbose_name="Descrição do Produto")
    imagem_produto = models.ImageField(upload_to='produtos/', verbose_name="Imagem dos Produtos ")
    
    criado_em_produto = models.DateTimeField(auto_now_add=True)
    atualizado_em_produto = models.DateTimeField(auto_now=True)          

    def __str__(self):
        return self.nome_produto  