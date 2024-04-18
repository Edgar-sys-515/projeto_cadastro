from django.db import models
from datetime import datetime



#documentacao
#https://docs.djangoproject.com/en/4.2/topics/db/models/?_gl=1*vy3v6f*_ga*MjcyMzg4MDQuMTcxMDU1MDE2MA..*_ga_37GXT4VGQK*MTcxMzMxMjQxMC4yMzkuMS4xNzEzMzEyNDEwLjAuMC4w




class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField(null=True)
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)# sem parenteses

    def __str__(self):
        
        if self.pago == True:
            nomme =  'Sim'
        elif self.pago == False:
            nomme = 'Não'
        return str(f'{self.investimento} | Pago: {nomme}')
    

