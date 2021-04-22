# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms import ModelForm



class NFCe(models.Model):
    nfce_versao = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    nfce_id = models.CharField(db_column='nfce_Id', max_length=47, blank=True, null=True)  # Field name made lowercase.
    nfce_ide_cuf = models.IntegerField(db_column='nfce_ide_cUF', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_cnf = models.IntegerField(db_column='nfce_ide_cNF', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_natop = models.CharField(db_column='nfce_ide_natOp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nfce_ide_mod = models.IntegerField(blank=True, null=True)
    nfce_ide_serie = models.IntegerField(blank=True, null=True)
    nfce_ide_nnf = models.IntegerField(db_column='nfce_ide_nNF', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_dhemi = models.CharField(db_column='nfce_ide_dhEmi', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nfce_ide_tpnf = models.IntegerField(db_column='nfce_ide_tpNF', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_iddest = models.IntegerField(db_column='nfce_ide_idDest', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_cmunfg = models.IntegerField(db_column='nfce_ide_cMunFG', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_tpimp = models.IntegerField(db_column='nfce_ide_tpImp', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_tpemis = models.IntegerField(db_column='nfce_ide_tpEmis', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_cdv = models.IntegerField(db_column='nfce_ide_cDV', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_tpamb = models.IntegerField(db_column='nfce_ide_tpAmb', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_finnfe = models.IntegerField(db_column='nfce_ide_finNFe', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_indfinal = models.IntegerField(db_column='nfce_ide_indFinal', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_indpres = models.IntegerField(db_column='nfce_ide_indPres', blank=True, null=True)  # Field name made lowercase.
    nfce_ide_procemi = models.IntegerField(db_column='nfce_ide_procEmi', blank=True, null=True)  # Field name made lowercase.
    nfce_emit_cnpj = models.CharField(db_column='nfce_emit_CNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nfce_emit_xnome = models.CharField(db_column='nfce_emit_xNome', max_length=33, blank=True, null=True)  # Field name made lowercase.
    nfce_emit_xfant = models.CharField(db_column='nfce_emit_xFant', max_length=29, blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit = models.IntegerField(db_column='nfce_emit_enderEmit', blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_xlgr = models.CharField(db_column='nfce_emit_enderEmit_xLgr', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_nro = models.IntegerField(db_column='nfce_emit_enderEmit_nro', blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_xbairro = models.CharField(db_column='nfce_emit_enderEmit_xBairro', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_cmun = models.IntegerField(db_column='nfce_emit_enderEmit_cMun', blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_xmun = models.CharField(db_column='nfce_emit_enderEmit_xMun', max_length=7, blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_uf = models.CharField(db_column='nfce_emit_enderEmit_UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_cep = models.IntegerField(db_column='nfce_emit_enderEmit_CEP', blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_cpais = models.IntegerField(db_column='nfce_emit_enderEmit_cPais', blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_xpais = models.CharField(db_column='nfce_emit_enderEmit_xPais', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nfce_emit_enderemit_fone = models.IntegerField(db_column='nfce_emit_enderEmit_fone', blank=True, null=True)  # Field name made lowercase.
    nfce_emit_ie = models.IntegerField(db_column='nfce_emit_IE', blank=True, null=True)  # Field name made lowercase.
    nfce_emit_crt = models.IntegerField(db_column='nfce_emit_CRT', blank=True, null=True)  # Field name made lowercase.
    nfce_det_nitem = models.IntegerField(db_column='nfce_det_nItem', blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_cprod = models.IntegerField(db_column='nfce_det_prod_cProd', blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_cean = models.CharField(db_column='nfce_det_prod_cEAN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_xprod = models.CharField(db_column='nfce_det_prod_xProd', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_ncm = models.IntegerField(db_column='nfce_det_prod_NCM', blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_cfop = models.IntegerField(db_column='nfce_det_prod_CFOP', blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_ucom = models.CharField(db_column='nfce_det_prod_uCom', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_qcom = models.DecimalField(db_column='nfce_det_prod_qCom', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_vuncom = models.DecimalField(db_column='nfce_det_prod_vUnCom', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_vprod = models.DecimalField(db_column='nfce_det_prod_vProd', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_ceantrib = models.CharField(db_column='nfce_det_prod_cEANTrib', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_utrib = models.CharField(db_column='nfce_det_prod_uTrib', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_qtrib = models.DecimalField(db_column='nfce_det_prod_qTrib', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_vuntrib = models.DecimalField(db_column='nfce_det_prod_vUnTrib', max_digits=12, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_indtot = models.IntegerField(db_column='nfce_det_prod_indTot', blank=True, null=True)  # Field name made lowercase.
    nfce_det_prod_cest = models.IntegerField(db_column='nfce_det_prod_CEST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'nfce'


class ModelFormWithFileField(ModelForm):
    class Meta:
        model = NFCe
        fields = ['nfce_id', 'nfce_ide_serie', 'nfce_emit_cnpj']


class NFe(models.Model):
    nfeproc = models.IntegerField(db_column='nfeProc', blank=True, null=True)  # Field name made lowercase.
    nfeproc_versao = models.DecimalField(db_column='nfeProc_versao', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_xmlns = models.CharField(db_column='nfeProc_xmlns', max_length=34, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe = models.IntegerField(db_column='nfeProc_NFe', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe = models.IntegerField(db_column='nfeProc_NFe_infNFe', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_versao = models.DecimalField(db_column='nfeProc_NFe_infNFe_versao', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_id = models.CharField(db_column='nfeProc_NFe_infNFe_Id', max_length=47, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_cuf = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_cUF', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_cnf = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_cNF', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_natop = models.CharField(db_column='nfeProc_NFe_infNFe_ide_natOp', max_length=39, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_mod = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_mod', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_serie = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_serie', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_nnf = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_nNF', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_dhemi = models.CharField(db_column='nfeProc_NFe_infNFe_ide_dhEmi', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_dhsaient = models.CharField(db_column='nfeProc_NFe_infNFe_ide_dhSaiEnt', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_tpnf = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_tpNF', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_iddest = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_idDest', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_cmunfg = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_cMunFG', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_tpimp = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_tpImp', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_tpemis = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_tpEmis', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_cdv = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_cDV', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_tpamb = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_tpAmb', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_finnfe = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_finNFe', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_indfinal = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_indFinal', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_indpres = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_indPres', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_procemi = models.IntegerField(db_column='nfeProc_NFe_infNFe_ide_procEmi', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_ide_verproc = models.CharField(db_column='nfeProc_NFe_infNFe_ide_verProc', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit = models.IntegerField(db_column='nfeProc_NFe_infNFe_emit', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_cnpj = models.CharField(db_column='nfeProc_NFe_infNFe_emit_CNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_xnome = models.CharField(db_column='nfeProc_NFe_infNFe_emit_xNome', max_length=33, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit = models.IntegerField(db_column='nfeProc_NFe_infNFe_emit_enderEmit', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_xlgr = models.CharField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_xLgr', max_length=33, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_nro = models.IntegerField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_nro', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_xbairro = models.CharField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_xBairro', max_length=17, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_cmun = models.IntegerField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_cMun', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_xmun = models.CharField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_xMun', max_length=7, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_uf = models.CharField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_cep = models.IntegerField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_CEP', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_cpais = models.IntegerField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_cPais', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_xpais = models.CharField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_xPais', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_enderemit_fone = models.CharField(db_column='nfeProc_NFe_infNFe_emit_enderEmit_fone', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_ie = models.IntegerField(db_column='nfeProc_NFe_infNFe_emit_IE', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_emit_crt = models.IntegerField(db_column='nfeProc_NFe_infNFe_emit_CRT', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest = models.IntegerField(db_column='nfeProc_NFe_infNFe_dest', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_cnpj = models.CharField(db_column='nfeProc_NFe_infNFe_dest_CNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_xnome = models.CharField(db_column='nfeProc_NFe_infNFe_dest_xNome', max_length=33, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest = models.IntegerField(db_column='nfeProc_NFe_infNFe_dest_enderDest', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_xlgr = models.CharField(db_column='nfeProc_NFe_infNFe_dest_enderDest_xLgr', max_length=39, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_nro = models.IntegerField(db_column='nfeProc_NFe_infNFe_dest_enderDest_nro', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_xbairro = models.CharField(db_column='nfeProc_NFe_infNFe_dest_enderDest_xBairro', max_length=18, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_cmun = models.IntegerField(db_column='nfeProc_NFe_infNFe_dest_enderDest_cMun', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_xmun = models.CharField(db_column='nfeProc_NFe_infNFe_dest_enderDest_xMun', max_length=19, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_uf = models.CharField(db_column='nfeProc_NFe_infNFe_dest_enderDest_UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_cep = models.IntegerField(db_column='nfeProc_NFe_infNFe_dest_enderDest_CEP', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_cpais = models.IntegerField(db_column='nfeProc_NFe_infNFe_dest_enderDest_cPais', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_xpais = models.CharField(db_column='nfeProc_NFe_infNFe_dest_enderDest_xPais', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_enderdest_fone = models.CharField(db_column='nfeProc_NFe_infNFe_dest_enderDest_fone', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_indiedest = models.IntegerField(db_column='nfeProc_NFe_infNFe_dest_indIEDest', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_dest_ie = models.IntegerField(db_column='nfeProc_NFe_infNFe_dest_IE', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det = models.IntegerField(db_column='nfeProc_NFe_infNFe_det', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_nitem = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_nItem', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_prod', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_cprod = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_prod_cProd', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_cean = models.CharField(db_column='nfeProc_NFe_infNFe_det_prod_cEAN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_xprod = models.CharField(db_column='nfeProc_NFe_infNFe_det_prod_xProd', max_length=83, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_ncm = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_prod_NCM', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_cfop = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_prod_CFOP', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_ucom = models.CharField(db_column='nfeProc_NFe_infNFe_det_prod_uCom', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_qcom = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_prod_qCom', max_digits=15, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_vuncom = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_prod_vUnCom', max_digits=15, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_vprod = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_prod_vProd', max_digits=15, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_ceantrib = models.CharField(db_column='nfeProc_NFe_infNFe_det_prod_cEANTrib', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_utrib = models.CharField(db_column='nfeProc_NFe_infNFe_det_prod_uTrib', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_qtrib = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_prod_qTrib', max_digits=15, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_vuntrib = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_prod_vUnTrib', max_digits=15, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_indtot = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_prod_indTot', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms20 = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms20_orig = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_orig', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms20_cst = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_CST', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms20_modbc = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_modBC', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms20_predbc = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_pRedBC', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms20_vbc = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_vBC', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms20_picms = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_pICMS', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms20_vicms = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS20_vICMS', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_pis = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_PIS', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_pis_pisoutr = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_pis_pisoutr_cst = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr_CST', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_pis_pisoutr_vbc = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr_vBC', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_pis_pisoutr_ppis = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr_pPIS', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_pis_pisoutr_vpis = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_PIS_PISOutr_vPIS', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_cofins = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_COFINS', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_cofins_cofinsoutr = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_cofins_cofinsoutr_cst = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr_CST', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_cofins_cofinsoutr_vbc = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr_vBC', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_cofins_cofinsoutr_pcofins = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr_pCOFINS', max_digits=5, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_cofins_cofinsoutr_vcofins = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_COFINS_COFINSOutr_vCOFINS', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms00 = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms00_orig = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_orig', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms00_cst = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_CST', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms00_modbc = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_modBC', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms00_vbc = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_vBC', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms00_picms = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_pICMS', max_digits=6, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_imposto_icms_icms00_vicms = models.DecimalField(db_column='nfeProc_NFe_infNFe_det_imposto_ICMS_ICMS00_vICMS', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_det_prod_cest = models.IntegerField(db_column='nfeProc_NFe_infNFe_det_prod_CEST', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total = models.IntegerField(db_column='nfeProc_NFe_infNFe_total', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot = models.IntegerField(db_column='nfeProc_NFe_infNFe_total_ICMSTot', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vbc = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vBC', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vicms = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vICMS', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vicmsdeson = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vICMSDeson', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vfcp = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vFCP', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vbcst = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vBCST', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vst = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vST', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vfcpst = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vFCPST', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vfcpstret = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vFCPSTRet', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vprod = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vProd', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vfrete = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vFrete', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vseg = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vSeg', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vdesc = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vDesc', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vii = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vII', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vipi = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vIPI', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vipidevol = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vIPIDevol', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vpis = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vPIS', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vcofins = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vCOFINS', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_voutro = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vOutro', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_total_icmstot_vnf = models.DecimalField(db_column='nfeProc_NFe_infNFe_total_ICMSTot_vNF', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_transp = models.IntegerField(db_column='nfeProc_NFe_infNFe_transp', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_transp_modfrete = models.IntegerField(db_column='nfeProc_NFe_infNFe_transp_modFrete', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_transp_vol = models.IntegerField(db_column='nfeProc_NFe_infNFe_transp_vol', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_transp_vol_qvol = models.IntegerField(db_column='nfeProc_NFe_infNFe_transp_vol_qVol', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_transp_vol_pesol = models.DecimalField(db_column='nfeProc_NFe_infNFe_transp_vol_pesoL', max_digits=5, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_transp_vol_pesob = models.DecimalField(db_column='nfeProc_NFe_infNFe_transp_vol_pesoB', max_digits=6, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_pag = models.IntegerField(db_column='nfeProc_NFe_infNFe_pag', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_pag_detpag = models.IntegerField(db_column='nfeProc_NFe_infNFe_pag_detPag', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_pag_detpag_tpag = models.IntegerField(db_column='nfeProc_NFe_infNFe_pag_detPag_tPag', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_pag_detpag_vpag = models.DecimalField(db_column='nfeProc_NFe_infNFe_pag_detPag_vPag', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_compra = models.IntegerField(db_column='nfeProc_NFe_infNFe_compra', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_infnfe_compra_xped = models.IntegerField(db_column='nfeProc_NFe_infNFe_compra_xPed', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature = models.IntegerField(db_column='nfeProc_NFe_Signature', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_xmlns = models.CharField(db_column='nfeProc_NFe_Signature_xmlns', max_length=34, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo = models.IntegerField(db_column='nfeProc_NFe_Signature_SignedInfo', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_canonicalizationmethod = models.IntegerField(db_column='nfeProc_NFe_Signature_SignedInfo_CanonicalizationMethod', blank=True, null=True)  # Field name made lowercase.
    nfe_signature_signedinfo_canonicalizationmethod_algorithm = models.CharField(db_column='NFe_Signature_SignedInfo_CanonicalizationMethod_Algorithm', max_length=47, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_signaturemethod = models.IntegerField(db_column='nfeProc_NFe_Signature_SignedInfo_SignatureMethod', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_signaturemethod_algorithm = models.CharField(db_column='nfeProc_NFe_Signature_SignedInfo_SignatureMethod_Algorithm', max_length=42, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_reference = models.IntegerField(db_column='nfeProc_NFe_Signature_SignedInfo_Reference', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_reference_uri = models.CharField(db_column='nfeProc_NFe_Signature_SignedInfo_Reference_URI', max_length=48, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_reference_transforms = models.IntegerField(db_column='nfeProc_NFe_Signature_SignedInfo_Reference_Transforms', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_reference_transforms_transform = models.IntegerField(db_column='nfeProc_NFe_Signature_SignedInfo_Reference_Transforms_Transform', blank=True, null=True)  # Field name made lowercase.
    signature_signedinfo_reference_transforms_transform_algorithm = models.CharField(db_column='Signature_SignedInfo_Reference_Transforms_Transform_Algorithm', max_length=53, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_reference_digestmethod = models.IntegerField(db_column='nfeProc_NFe_Signature_SignedInfo_Reference_DigestMethod', blank=True, null=True)  # Field name made lowercase.
    nfe_signature_signedinfo_reference_digestmethod_algorithm = models.CharField(db_column='NFe_Signature_SignedInfo_Reference_DigestMethod_Algorithm', max_length=38, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signedinfo_reference_digestvalue = models.CharField(db_column='nfeProc_NFe_Signature_SignedInfo_Reference_DigestValue', max_length=28, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_signaturevalue = models.CharField(db_column='nfeProc_NFe_Signature_SignatureValue', max_length=344, blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_keyinfo = models.IntegerField(db_column='nfeProc_NFe_Signature_KeyInfo', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_keyinfo_x509data = models.IntegerField(db_column='nfeProc_NFe_Signature_KeyInfo_X509Data', blank=True, null=True)  # Field name made lowercase.
    nfeproc_nfe_signature_keyinfo_x509data_x509certificate = models.CharField(db_column='nfeProc_NFe_Signature_KeyInfo_X509Data_X509Certificate', max_length=2648, blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe = models.IntegerField(db_column='nfeProc_protNFe', blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_versao = models.DecimalField(db_column='nfeProc_protNFe_versao', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot = models.IntegerField(db_column='nfeProc_protNFe_infProt', blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_id = models.CharField(db_column='nfeProc_protNFe_infProt_Id', max_length=17, blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_tpamb = models.IntegerField(db_column='nfeProc_protNFe_infProt_tpAmb', blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_veraplic = models.CharField(db_column='nfeProc_protNFe_infProt_verAplic', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_chnfe = models.IntegerField(db_column='nfeProc_protNFe_infProt_chNFe', blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_dhrecbto = models.CharField(db_column='nfeProc_protNFe_infProt_dhRecbto', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_nprot = models.IntegerField(db_column='nfeProc_protNFe_infProt_nProt', blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_digval = models.CharField(db_column='nfeProc_protNFe_infProt_digVal', max_length=28, blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_cstat = models.IntegerField(db_column='nfeProc_protNFe_infProt_cStat', blank=True, null=True)  # Field name made lowercase.
    nfeproc_protnfe_infprot_xmotivo = models.CharField(db_column='nfeProc_protNFe_infProt_xMotivo', max_length=24, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'nfe'


class Reg0000(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_ver = models.CharField(db_column='COD_VER', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_fin = models.CharField(db_column='COD_FIN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ie = models.CharField(db_column='IE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cod_mun = models.CharField(db_column='COD_MUN', max_length=7, blank=True, null=True)  # Field name made lowercase.
    im = models.CharField(db_column='IM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suframa = models.CharField(db_column='SUFRAMA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ind_perfil = models.CharField(db_column='IND_PERFIL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_ativ = models.CharField(db_column='IND_ATIV', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0000'
# Unable to inspect table 'reg_0001'
# The error was: (1932, "Table 'bd20190207165244.reg_0001' doesn't exist in engine")


class Reg0005(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fantasia = models.CharField(db_column='FANTASIA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    num = models.CharField(db_column='NUM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='FONE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=11, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0005'


class Reg0015(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    uf_st = models.CharField(db_column='UF_ST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ie_st = models.CharField(db_column='IE_ST', max_length=14, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0015'


class Reg0100(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11, blank=True, null=True)  # Field name made lowercase.
    crc = models.CharField(db_column='CRC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    num = models.CharField(db_column='NUM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fone = models.CharField(db_column='FONE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=11, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mun = models.CharField(db_column='COD_MUN', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0100'


class Reg0150(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_pais = models.CharField(db_column='COD_PAIS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11, blank=True, null=True)  # Field name made lowercase.
    ie = models.CharField(db_column='IE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cod_mun = models.CharField(db_column='COD_MUN', max_length=7, blank=True, null=True)  # Field name made lowercase.
    suframa = models.CharField(db_column='SUFRAMA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    num = models.CharField(db_column='NUM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=60, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0150'


class Reg0175(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_alt = models.DateField(db_column='DT_ALT', blank=True, null=True)  # Field name made lowercase.
    nr_campo = models.CharField(db_column='NR_CAMPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cont_ant = models.CharField(db_column='CONT_ANT', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0175'


class Reg0190(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0190'


class Reg0200(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    descr_item = models.CharField(db_column='DESCR_ITEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_barra = models.CharField(db_column='COD_BARRA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cod_ant_item = models.CharField(db_column='COD_ANT_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    unid_inv = models.CharField(db_column='UNID_INV', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tipo_item = models.CharField(db_column='TIPO_ITEM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_ncm = models.CharField(db_column='COD_NCM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_ipi = models.CharField(db_column='EX_IPI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_gen = models.CharField(db_column='COD_GEN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_lst = models.CharField(db_column='COD_LST', max_length=5, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cest = models.CharField(db_column='CEST', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0200'


class Reg0205(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    descr_ant_item = models.CharField(db_column='DESCR_ANT_ITEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fim = models.DateField(db_column='DT_FIM', blank=True, null=True)  # Field name made lowercase.
    cod_ant_item = models.CharField(db_column='COD_ANT_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0205'


class Reg0206(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_comb = models.CharField(db_column='COD_COMB', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0206'


class Reg0210(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item_comp = models.CharField(db_column='COD_ITEM_COMP', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_comp = models.DecimalField(db_column='QTD_COMP', max_digits=23, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    perda = models.DecimalField(db_column='PERDA', max_digits=11, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0210'


class Reg0220(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    unid_conv = models.CharField(db_column='UNID_CONV', max_length=6, blank=True, null=True)  # Field name made lowercase.
    fat_conv = models.DecimalField(db_column='FAT_CONV', max_digits=25, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0220'


class Reg0300(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_ind_bem = models.CharField(db_column='COD_IND_BEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ident_merc = models.CharField(db_column='IDENT_MERC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    descr_item = models.CharField(db_column='DESCR_ITEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_prnc = models.CharField(db_column='COD_PRNC', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nr_parc = models.CharField(db_column='NR_PARC', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0300'


class Reg0305(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_ccus = models.CharField(db_column='COD_CCUS', max_length=60, blank=True, null=True)  # Field name made lowercase.
    func = models.CharField(db_column='FUNC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vida_util = models.CharField(db_column='VIDA_UTIL', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0305'


class Reg0400(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.CharField(db_column='COD_NAT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descr_nat = models.CharField(db_column='DESCR_NAT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0400'


class Reg0450(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_inf = models.CharField(db_column='COD_INF', max_length=6, blank=True, null=True)  # Field name made lowercase.
    txt = models.CharField(db_column='TXT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0450'


class Reg0460(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.
    txt = models.CharField(db_column='TXT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0460'


class Reg0500(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_alt = models.DateField(db_column='DT_ALT', blank=True, null=True)  # Field name made lowercase.
    cod_nat_cc = models.CharField(db_column='COD_NAT_CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ind_cta = models.CharField(db_column='IND_CTA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=60, blank=True, null=True)  # Field name made lowercase.
    nome_cta = models.CharField(db_column='NOME_CTA', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0500'


class Reg0600(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_alt = models.DateField(db_column='DT_ALT', blank=True, null=True)  # Field name made lowercase.
    cod_ccus = models.CharField(db_column='COD_CCUS', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ccus = models.CharField(db_column='CCUS', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_0600'
# Unable to inspect table 'reg_0990'
# The error was: (1932, "Table 'bd20190207165244.reg_0990' doesn't exist in engine")
# Unable to inspect table 'reg_1001'
# The error was: (1932, "Table 'bd20190207165244.reg_1001' doesn't exist in engine")


class Reg1010(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_exp = models.CharField(db_column='IND_EXP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_ccrf = models.CharField(db_column='IND_CCRF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_comb = models.CharField(db_column='IND_COMB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_usina = models.CharField(db_column='IND_USINA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_va = models.CharField(db_column='IND_VA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_ee = models.CharField(db_column='IND_EE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_cart = models.CharField(db_column='IND_CART', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_form = models.CharField(db_column='IND_FORM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_aer = models.CharField(db_column='IND_AER', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1010'


class Reg1100(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_doc = models.CharField(db_column='IND_DOC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nro_de = models.CharField(db_column='NRO_DE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    dt_de = models.DateField(db_column='DT_DE', blank=True, null=True)  # Field name made lowercase.
    nat_exp = models.CharField(db_column='NAT_EXP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nro_re = models.CharField(db_column='NRO_RE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    dt_re = models.DateField(db_column='DT_RE', blank=True, null=True)  # Field name made lowercase.
    chc_emb = models.CharField(db_column='CHC_EMB', max_length=18, blank=True, null=True)  # Field name made lowercase.
    dt_chc = models.DateField(db_column='DT_CHC', blank=True, null=True)  # Field name made lowercase.
    dt_avb = models.DateField(db_column='DT_AVB', blank=True, null=True)  # Field name made lowercase.
    tp_chc = models.CharField(db_column='TP_CHC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='PAIS', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1100'


class Reg1105(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    chv_nfe = models.CharField(db_column='CHV_NFE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1105'


class Reg1110(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    chv_nfe = models.CharField(db_column='CHV_NFE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    nr_memo = models.CharField(db_column='NR_MEMO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1110'


class Reg1200(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_aj_apur = models.CharField(db_column='COD_AJ_APUR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    sld_cred = models.DecimalField(db_column='SLD_CRED', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cred_apr = models.DecimalField(db_column='CRED_APR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cred_receb = models.DecimalField(db_column='CRED_RECEB', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cred_util = models.DecimalField(db_column='CRED_UTIL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sld_cred_fim = models.DecimalField(db_column='SLD_CRED_FIM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1200'


class Reg1210(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tipo_util = models.CharField(db_column='TIPO_UTIL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nr_doc = models.CharField(db_column='NR_DOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_cred_util = models.DecimalField(db_column='VL_CRED_UTIL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chv_doce = models.CharField(db_column='CHV_DOCE', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1210'


class Reg1300(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dt_fech = models.DateField(db_column='DT_FECH', blank=True, null=True)  # Field name made lowercase.
    estq_abert = models.DecimalField(db_column='ESTQ_ABERT', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_entr = models.DecimalField(db_column='VOL_ENTR', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_disp = models.DecimalField(db_column='VOL_DISP', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_saidas = models.DecimalField(db_column='VOL_SAIDAS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    estq_escr = models.DecimalField(db_column='ESTQ_ESCR', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    val_aj_perda = models.DecimalField(db_column='VAL_AJ_PERDA', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    val_aj_ganho = models.DecimalField(db_column='VAL_AJ_GANHO', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    fech_fisico = models.DecimalField(db_column='FECH_FISICO', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1300'


class Reg1310(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_tanque = models.CharField(db_column='NUM_TANQUE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    estq_abert = models.DecimalField(db_column='ESTQ_ABERT', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_entr = models.DecimalField(db_column='VOL_ENTR', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_disp = models.DecimalField(db_column='VOL_DISP', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_saidas = models.DecimalField(db_column='VOL_SAIDAS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    estq_escr = models.DecimalField(db_column='ESTQ_ESCR', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    val_aj_perda = models.DecimalField(db_column='VAL_AJ_PERDA', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    val_aj_ganho = models.DecimalField(db_column='VAL_AJ_GANHO', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    fech_fisico = models.DecimalField(db_column='FECH_FISICO', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1310'


class Reg1320(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_bico = models.CharField(db_column='NUM_BICO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nr_interv = models.CharField(db_column='NR_INTERV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mot_interv = models.CharField(db_column='MOT_INTERV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nom_interv = models.CharField(db_column='NOM_INTERV', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cnpj_interv = models.CharField(db_column='CNPJ_INTERV', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cpf_interv = models.CharField(db_column='CPF_INTERV', max_length=11, blank=True, null=True)  # Field name made lowercase.
    val_fecha = models.DecimalField(db_column='VAL_FECHA', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    val_abert = models.DecimalField(db_column='VAL_ABERT', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_aferi = models.DecimalField(db_column='VOL_AFERI', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vol_vendas = models.DecimalField(db_column='VOL_VENDAS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1320'


class Reg1350(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fabricante = models.CharField(db_column='FABRICANTE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='MODELO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo_medicao = models.CharField(db_column='TIPO_MEDICAO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1350'


class Reg1360(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_lacre = models.CharField(db_column='NUM_LACRE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dat_aplicacao = models.DateField(db_column='DAT_APLICACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1360'


class Reg1370(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_bico = models.CharField(db_column='NUM_BICO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    num_tanque = models.CharField(db_column='NUM_TANQUE', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1370'


class Reg1390(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.CharField(db_column='COD_PROD', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1390'


class Reg1391(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_registro = models.DateField(db_column='DT_REGISTRO', blank=True, null=True)  # Field name made lowercase.
    qtd_moid = models.DecimalField(db_column='QTD_MOID', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estq_ini = models.DecimalField(db_column='ESTQ_INI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtd_produz = models.DecimalField(db_column='QTD_PRODUZ', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ent_anid_hid = models.DecimalField(db_column='ENT_ANID_HID', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    outr_entr = models.DecimalField(db_column='OUTR_ENTR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perda = models.DecimalField(db_column='PERDA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cons = models.DecimalField(db_column='CONS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sai_ani_hid = models.DecimalField(db_column='SAI_ANI_HID', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    saidas = models.DecimalField(db_column='SAIDAS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estq_fin = models.DecimalField(db_column='ESTQ_FIN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    estq_ini_mel = models.DecimalField(db_column='ESTQ_INI_MEL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prod_dia_mel = models.DecimalField(db_column='PROD_DIA_MEL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    util_mel = models.DecimalField(db_column='UTIL_MEL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prod_alc_mel = models.DecimalField(db_column='PROD_ALC_MEL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1391'


class Reg1400(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item_ipm = models.CharField(db_column='COD_ITEM_IPM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    mun = models.CharField(db_column='MUN', max_length=7, blank=True, null=True)  # Field name made lowercase.
    valor = models.DecimalField(db_column='VALOR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1400'


class Reg1500(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_oper = models.CharField(db_column='IND_OPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_cons = models.CharField(db_column='COD_CONS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    dt_e_s = models.DateField(db_column='DT_E_S', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_forn = models.DecimalField(db_column='VL_FORN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv_nt = models.DecimalField(db_column='VL_SERV_NT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_terc = models.DecimalField(db_column='VL_TERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_da = models.DecimalField(db_column='VL_DA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_inf = models.CharField(db_column='COD_INF', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofis = models.DecimalField(db_column='VL_COFIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tp_ligacao = models.CharField(db_column='TP_LIGACAO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_grupo_tensao = models.CharField(db_column='COD_GRUPO_TENSAO', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1500'


class Reg1510(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_item = models.CharField(db_column='NUM_ITEM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_class = models.CharField(db_column='COD_CLASS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_st = models.DecimalField(db_column='ALIQ_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_rec = models.CharField(db_column='IND_REC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofis = models.DecimalField(db_column='VL_COFIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1510'


class Reg1600(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    tot_credito = models.DecimalField(db_column='TOT_CREDITO', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tot_debito = models.DecimalField(db_column='TOT_DEBITO', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1600'


class Reg1700(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_disp = models.CharField(db_column='COD_DISP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc_ini = models.CharField(db_column='NUM_DOC_INI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    num_doc_fin = models.CharField(db_column='NUM_DOC_FIN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    num_aut = models.CharField(db_column='NUM_AUT', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1700'


class Reg1710(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_doc_ini = models.CharField(db_column='NUM_DOC_INI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    num_doc_fin = models.CharField(db_column='NUM_DOC_FIN', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1710'


class Reg1800(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_carga = models.DecimalField(db_column='VL_CARGA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pass = models.DecimalField(db_column='VL_PASS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_fat = models.DecimalField(db_column='VL_FAT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_rat = models.DecimalField(db_column='IND_RAT', max_digits=14, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    vl_icms_ant = models.DecimalField(db_column='VL_ICMS_ANT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_apur = models.DecimalField(db_column='VL_ICMS_APUR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_apur = models.DecimalField(db_column='VL_BC_ICMS_APUR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_dif = models.DecimalField(db_column='VL_DIF', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1800'


class Reg1900(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_apur_icms = models.CharField(db_column='IND_APUR_ICMS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    descr_compl_out_apur = models.CharField(db_column='DESCR_COMPL_OUT_APUR', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1900'


class Reg1910(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1910'


class Reg1920(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_tot_transf_debitos_oa = models.DecimalField(db_column='VL_TOT_TRANSF_DEBITOS_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_aj_debitos_oa = models.DecimalField(db_column='VL_TOT_AJ_DEBITOS_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_estornos_cred_oa = models.DecimalField(db_column='VL_ESTORNOS_CRED_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_transf_creditos_oa = models.DecimalField(db_column='VL_TOT_TRANSF_CREDITOS_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_aj_creditos_oa = models.DecimalField(db_column='VL_TOT_AJ_CREDITOS_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_estornos_deb_oa = models.DecimalField(db_column='VL_ESTORNOS_DEB_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_credor_ant_oa = models.DecimalField(db_column='VL_SLD_CREDOR_ANT_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_apurado_oa = models.DecimalField(db_column='VL_SLD_APURADO_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_ded = models.DecimalField(db_column='VL_TOT_DED', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_recolher_oa = models.DecimalField(db_column='VL_ICMS_RECOLHER_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_credor_transp_oa = models.DecimalField(db_column='VL_SLD_CREDOR_TRANSP_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deb_esp_oa = models.DecimalField(db_column='DEB_ESP_OA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1920'


class Reg1921(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_aj_apur = models.CharField(db_column='COD_AJ_APUR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    descr_compl_aj = models.CharField(db_column='DESCR_COMPL_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_aj_apur = models.DecimalField(db_column='VL_AJ_APUR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1921'


class Reg1922(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_da = models.CharField(db_column='NUM_DA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc = models.CharField(db_column='PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1922'


class Reg1923(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_aj_item = models.DecimalField(db_column='VL_AJ_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chv_doce = models.CharField(db_column='CHV_DOCE', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1923'


class Reg1925(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_inf_adic = models.CharField(db_column='COD_INF_ADIC', max_length=8, blank=True, null=True)  # Field name made lowercase.
    vl_inf_adic = models.DecimalField(db_column='VL_INF_ADIC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    desc_compl_aj = models.CharField(db_column='DESC_COMPL_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1925'


class Reg1926(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_or = models.CharField(db_column='COD_OR', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vl_or = models.DecimalField(db_column='VL_OR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dt_vcto = models.DateField(db_column='DT_VCTO', blank=True, null=True)  # Field name made lowercase.
    cod_rec = models.CharField(db_column='COD_REC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc = models.CharField(db_column='PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mes_ref = models.CharField(db_column='MES_REF', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_1926'
# Unable to inspect table 'reg_1990'
# The error was: (1932, "Table 'bd20190207165244.reg_1990' doesn't exist in engine")
# Unable to inspect table 'reg_9001'
# The error was: (1932, "Table 'bd20190207165244.reg_9001' doesn't exist in engine")
# Unable to inspect table 'reg_9900'
# The error was: (1932, "Table 'bd20190207165244.reg_9900' doesn't exist in engine")
# Unable to inspect table 'reg_9990'
# The error was: (1932, "Table 'bd20190207165244.reg_9990' doesn't exist in engine")
# Unable to inspect table 'reg_9999'
# The error was: (1932, "Table 'bd20190207165244.reg_9999' doesn't exist in engine")
# Unable to inspect table 'reg_c001'
# The error was: (1932, "Table 'bd20190207165244.reg_c001' doesn't exist in engine")


class RegC100(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_oper = models.CharField(db_column='IND_OPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    chv_nfe = models.CharField(db_column='CHV_NFE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    dt_e_s = models.DateField(db_column='DT_E_S', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_pgto = models.CharField(db_column='IND_PGTO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_abat_nt = models.DecimalField(db_column='VL_ABAT_NT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_merc = models.DecimalField(db_column='VL_MERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_frt = models.CharField(db_column='IND_FRT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_frt = models.DecimalField(db_column='VL_FRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_seg = models.DecimalField(db_column='VL_SEG', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_da = models.DecimalField(db_column='VL_OUT_DA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_ipi = models.DecimalField(db_column='VL_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis_st = models.DecimalField(db_column='VL_PIS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins_st = models.DecimalField(db_column='VL_COFINS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c100'


class RegC101(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_fcp_uf_dest = models.DecimalField(db_column='VL_FCP_UF_DEST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_uf_dest = models.DecimalField(db_column='VL_ICMS_UF_DEST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_uf_rem = models.DecimalField(db_column='VL_ICMS_UF_REM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c101'


class RegC105(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    oper = models.CharField(db_column='OPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_uf = models.CharField(db_column='COD_UF', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c105'


class RegC110(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_inf = models.CharField(db_column='COD_INF', max_length=6, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c110'


class RegC111(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c111'


class RegC112(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_da = models.CharField(db_column='COD_DA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    num_da = models.CharField(db_column='NUM_DA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_aut = models.CharField(db_column='COD_AUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_da = models.DecimalField(db_column='VL_DA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dt_vcto = models.DateField(db_column='DT_VCTO', blank=True, null=True)  # Field name made lowercase.
    dt_pgto = models.DateField(db_column='DT_PGTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c112'


class RegC113(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_oper = models.CharField(db_column='IND_OPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    chv_doce = models.CharField(db_column='CHV_DOCE', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c113'


class RegC114(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ecf_fab = models.CharField(db_column='ECF_FAB', max_length=21, blank=True, null=True)  # Field name made lowercase.
    ecf_cx = models.CharField(db_column='ECF_CX', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c114'


class RegC115(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_carga = models.CharField(db_column='IND_CARGA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_col = models.CharField(db_column='CNPJ_COL', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ie_col = models.CharField(db_column='IE_COL', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cpf_col = models.CharField(db_column='CPF_COL', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cod_mun_col = models.CharField(db_column='COD_MUN_COL', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cnpj_entg = models.CharField(db_column='CNPJ_ENTG', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ie_entg = models.CharField(db_column='IE_ENTG', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cpf_entg = models.CharField(db_column='CPF_ENTG', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cod_mun_entg = models.CharField(db_column='COD_MUN_ENTG', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c115'


class RegC116(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nr_sat = models.CharField(db_column='NR_SAT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    chv_cfe = models.CharField(db_column='CHV_CFE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    num_cfe = models.CharField(db_column='NUM_CFE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.CharField(db_column='DT_DOC', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c116'


class RegC120(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_doc_imp = models.CharField(db_column='COD_DOC_IMP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    num_doc_imp = models.CharField(db_column='NUM_DOC_IMP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pis_imp = models.DecimalField(db_column='PIS_IMP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cofins_imp = models.DecimalField(db_column='COFINS_IMP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    num_acdraw = models.CharField(db_column='NUM_ACDRAW', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c120'


class RegC130(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_serv_nt = models.DecimalField(db_column='VL_SERV_NT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_issqn = models.DecimalField(db_column='VL_BC_ISSQN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_issqn = models.DecimalField(db_column='VL_ISSQN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_irrf = models.DecimalField(db_column='VL_BC_IRRF', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_irrf = models.DecimalField(db_column='VL_IRRF', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_prev = models.DecimalField(db_column='VL_BC_PREV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_prev = models.DecimalField(db_column='VL_PREV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c130'


class RegC140(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_tit = models.CharField(db_column='IND_TIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    desc_tit = models.CharField(db_column='DESC_TIT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_tit = models.CharField(db_column='NUM_TIT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qtd_parc = models.CharField(db_column='QTD_PARC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vl_tit = models.DecimalField(db_column='VL_TIT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c140'


class RegC141(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_parc = models.CharField(db_column='NUM_PARC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dt_vcto = models.DateField(db_column='DT_VCTO', blank=True, null=True)  # Field name made lowercase.
    vl_parc = models.DecimalField(db_column='VL_PARC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c141'


class RegC160(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    veic_id = models.CharField(db_column='VEIC_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.
    qtd_vol = models.CharField(db_column='QTD_VOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    peso_brt = models.DecimalField(db_column='PESO_BRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    peso_liq = models.DecimalField(db_column='PESO_LIQ', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    uf_id = models.CharField(db_column='UF_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c160'


class RegC165(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    veic_id = models.CharField(db_column='VEIC_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cod_aut = models.CharField(db_column='COD_AUT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nr_passe = models.CharField(db_column='NR_PASSE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='HORA', max_length=6, blank=True, null=True)  # Field name made lowercase.
    temper = models.DecimalField(db_column='TEMPER', max_digits=20, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    qtd_vol = models.CharField(db_column='QTD_VOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    peso_brt = models.DecimalField(db_column='PESO_BRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    peso_liq = models.DecimalField(db_column='PESO_LIQ', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nom_mot = models.CharField(db_column='NOM_MOT', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=11, blank=True, null=True)  # Field name made lowercase.
    uf_id = models.CharField(db_column='UF_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c165'


class RegC170(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_item = models.CharField(db_column='NUM_ITEM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    descr_compl = models.CharField(db_column='DESCR_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=24, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_mov = models.CharField(db_column='IND_MOV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.CharField(db_column='COD_NAT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_st = models.DecimalField(db_column='ALIQ_ST', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_apur = models.CharField(db_column='IND_APUR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cst_ipi = models.CharField(db_column='CST_IPI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_enq = models.CharField(db_column='COD_ENQ', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vl_bc_ipi = models.DecimalField(db_column='VL_BC_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_ipi = models.DecimalField(db_column='ALIQ_IPI', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_ipi = models.DecimalField(db_column='VL_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cst_pis = models.CharField(db_column='CST_PIS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_pis = models.DecimalField(db_column='VL_BC_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_pis_perc = models.DecimalField(db_column='ALIQ_PIS_PERC', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quant_bc_pis = models.DecimalField(db_column='QUANT_BC_PIS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    aliq_pis_reais = models.DecimalField(db_column='ALIQ_PIS_REAIS', max_digits=23, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cst_cofins = models.CharField(db_column='CST_COFINS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_cofins = models.DecimalField(db_column='VL_BC_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_cofins_perc = models.DecimalField(db_column='ALIQ_COFINS_PERC', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quant_bc_cofins = models.DecimalField(db_column='QUANT_BC_COFINS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    aliq_cofins_reais = models.DecimalField(db_column='ALIQ_COFINS_REAIS', max_digits=23, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c170'


class RegC171(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_tanque = models.CharField(db_column='NUM_TANQUE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    qtde = models.DecimalField(db_column='QTDE', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c171'


class RegC172(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_bc_issqn = models.DecimalField(db_column='VL_BC_ISSQN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_issqn = models.DecimalField(db_column='ALIQ_ISSQN', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_issqn = models.DecimalField(db_column='VL_ISSQN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c172'


class RegC173(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lote_med = models.CharField(db_column='LOTE_MED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qtd_item = models.DecimalField(db_column='QTD_ITEM', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    dt_fab = models.DateField(db_column='DT_FAB', blank=True, null=True)  # Field name made lowercase.
    dt_val = models.DateField(db_column='DT_VAL', blank=True, null=True)  # Field name made lowercase.
    ind_med = models.CharField(db_column='IND_MED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tp_prod = models.CharField(db_column='TP_PROD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_tab_max = models.DecimalField(db_column='VL_TAB_MAX', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c173'


class RegC174(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_arm = models.CharField(db_column='IND_ARM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    num_arm = models.CharField(db_column='NUM_ARM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descr_compl = models.CharField(db_column='DESCR_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c174'


class RegC175(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_veic_oper = models.CharField(db_column='IND_VEIC_OPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chassi_veic = models.CharField(db_column='CHASSI_VEIC', max_length=17, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c175'


class RegC176(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod_ult_e = models.CharField(db_column='COD_MOD_ULT_E', max_length=2, blank=True, null=True)  # Field name made lowercase.
    num_doc_ult_e = models.CharField(db_column='NUM_DOC_ULT_E', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ser_ult_e = models.CharField(db_column='SER_ULT_E', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dt_ult_e = models.DateField(db_column='DT_ULT_E', blank=True, null=True)  # Field name made lowercase.
    cod_part_ult_e = models.CharField(db_column='COD_PART_ULT_E', max_length=60, blank=True, null=True)  # Field name made lowercase.
    quant_ult_e = models.DecimalField(db_column='QUANT_ULT_E', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vl_unit_ult_e = models.DecimalField(db_column='VL_UNIT_ULT_E', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vl_unit_bc_st = models.DecimalField(db_column='VL_UNIT_BC_ST', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    chave_nfe_ult_e = models.CharField(db_column='CHAVE_NFE_ULT_E', max_length=44, blank=True, null=True)  # Field name made lowercase.
    num_item_ult_e = models.CharField(db_column='NUM_ITEM_ULT_E', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vl_unit_bc_icms_ult_e = models.DecimalField(db_column='VL_UNIT_BC_ICMS_ULT_E', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_icms_ult_e = models.DecimalField(db_column='ALIQ_ICMS_ULT_E', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_unit_limite_bc_icms_ult_e = models.DecimalField(db_column='VL_UNIT_LIMITE_BC_ICMS_ULT_E', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_unit_icms_ult_e = models.DecimalField(db_column='VL_UNIT_ICMS_ULT_E', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    aliq_st_ult_e = models.DecimalField(db_column='ALIQ_ST_ULT_E', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_unit_res = models.DecimalField(db_column='VL_UNIT_RES', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cod_resp_ret = models.CharField(db_column='COD_RESP_RET', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_mot_res = models.CharField(db_column='COD_MOT_RES', max_length=1, blank=True, null=True)  # Field name made lowercase.
    chave_nfe_ret = models.CharField(db_column='CHAVE_NFE_RET', max_length=44, blank=True, null=True)  # Field name made lowercase.
    cod_part_nfe_ret = models.CharField(db_column='COD_PART_NFE_RET', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ser_nfe_ret = models.CharField(db_column='SER_NFE_RET', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_nfe_ret = models.CharField(db_column='NUM_NFE_RET', max_length=9, blank=True, null=True)  # Field name made lowercase.
    item_nfe_ret = models.CharField(db_column='ITEM_NFE_RET', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_da = models.CharField(db_column='COD_DA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    num_da = models.CharField(db_column='NUM_DA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c176'


class RegC177(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_selo_ipi = models.CharField(db_column='COD_SELO_IPI', max_length=6, blank=True, null=True)  # Field name made lowercase.
    qt_selo_ipi = models.CharField(db_column='QT_SELO_IPI', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c177'


class RegC178(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cl_enq = models.CharField(db_column='CL_ENQ', max_length=5, blank=True, null=True)  # Field name made lowercase.
    vl_unid = models.DecimalField(db_column='VL_UNID', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    quant_pad = models.DecimalField(db_column='QUANT_PAD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c178'


class RegC179(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    bc_st_orig_dest = models.DecimalField(db_column='BC_ST_ORIG_DEST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    icms_st_rep = models.DecimalField(db_column='ICMS_ST_REP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    icms_st_compl = models.DecimalField(db_column='ICMS_ST_COMPL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bc_ret = models.DecimalField(db_column='BC_RET', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    icms_ret = models.DecimalField(db_column='ICMS_RET', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c179'


class RegC190(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_ipi = models.DecimalField(db_column='VL_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c190'


class RegC195(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c195'


class RegC197(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_aj = models.CharField(db_column='COD_AJ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descr_compl_aj = models.CharField(db_column='DESCR_COMPL_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_outros = models.DecimalField(db_column='VL_OUTROS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c197'


class RegC300(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc_ini = models.CharField(db_column='NUM_DOC_INI', max_length=6, blank=True, null=True)  # Field name made lowercase.
    num_doc_fin = models.CharField(db_column='NUM_DOC_FIN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c300'


class RegC310(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_doc_canc = models.CharField(db_column='NUM_DOC_CANC', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c310'


class RegC320(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c320'


class RegC321(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c321'


class RegC350(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub_ser = models.CharField(db_column='SUB_SER', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf = models.CharField(db_column='CNPJ_CPF', max_length=14, blank=True, null=True)  # Field name made lowercase.
    vl_merc = models.DecimalField(db_column='VL_MERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofis = models.DecimalField(db_column='VL_COFIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c350'


class RegC370(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_item = models.CharField(db_column='NUM_ITEM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c370'


class RegC390(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c390'


class RegC400(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ecf_mod = models.CharField(db_column='ECF_MOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ecf_fab = models.CharField(db_column='ECF_FAB', max_length=21, blank=True, null=True)  # Field name made lowercase.
    ecf_cx = models.CharField(db_column='ECF_CX', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c400'


class RegC405(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cro = models.CharField(db_column='CRO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    crz = models.CharField(db_column='CRZ', max_length=6, blank=True, null=True)  # Field name made lowercase.
    num_coo_fin = models.CharField(db_column='NUM_COO_FIN', max_length=9, blank=True, null=True)  # Field name made lowercase.
    gt_fin = models.DecimalField(db_column='GT_FIN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_brt = models.DecimalField(db_column='VL_BRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c405'


class RegC410(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c410'


class RegC420(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_tot_par = models.CharField(db_column='COD_TOT_PAR', max_length=7, blank=True, null=True)  # Field name made lowercase.
    vlr_acum_tot = models.DecimalField(db_column='VLR_ACUM_TOT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nr_tot = models.CharField(db_column='NR_TOT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    descr_nr_tot = models.CharField(db_column='DESCR_NR_TOT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c420'


class RegC425(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c425'


class RegC460(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cpf_cnpj = models.CharField(db_column='CPF_CNPJ', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nome_adq = models.CharField(db_column='NOME_ADQ', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c460'


class RegC465(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    chv_cfe = models.CharField(db_column='CHV_CFE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    num_ccf = models.CharField(db_column='NUM_CCF', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c465'


class RegC470(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtd_canc = models.DecimalField(db_column='QTD_CANC', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c470'


class RegC490(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c490'


class RegC500(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_oper = models.CharField(db_column='IND_OPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_cons = models.CharField(db_column='COD_CONS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    dt_e_s = models.DateField(db_column='DT_E_S', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_forn = models.DecimalField(db_column='VL_FORN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv_nt = models.DecimalField(db_column='VL_SERV_NT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_terc = models.DecimalField(db_column='VL_TERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_da = models.DecimalField(db_column='VL_DA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_inf = models.CharField(db_column='COD_INF', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tp_ligacao = models.CharField(db_column='TP_LIGACAO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_grupo_tensao = models.CharField(db_column='COD_GRUPO_TENSAO', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c500'


class RegC510(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_item = models.CharField(db_column='NUM_ITEM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_class = models.CharField(db_column='COD_CLASS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_st = models.DecimalField(db_column='ALIQ_ST', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_rec = models.CharField(db_column='IND_REC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c510'


class RegC590(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c590'


class RegC600(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mun = models.CharField(db_column='COD_MUN', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_cons = models.CharField(db_column='COD_CONS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    qtd_cons = models.CharField(db_column='QTD_CONS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qtd_canc = models.CharField(db_column='QTD_CANC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cons = models.CharField(db_column='CONS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_forn = models.DecimalField(db_column='VL_FORN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv_nt = models.DecimalField(db_column='VL_SERV_NT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_terc = models.DecimalField(db_column='VL_TERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_da = models.DecimalField(db_column='VL_DA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c600'


class RegC601(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_doc_canc = models.CharField(db_column='NUM_DOC_CANC', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c601'


class RegC610(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_class = models.CharField(db_column='COD_CLASS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c610'


class RegC690(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c690'


class RegC700(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nro_ord_ini = models.CharField(db_column='NRO_ORD_INI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    nro_ord_fin = models.CharField(db_column='NRO_ORD_FIN', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc_ini = models.DateField(db_column='DT_DOC_INI', blank=True, null=True)  # Field name made lowercase.
    dt_doc_fin = models.DateField(db_column='DT_DOC_FIN', blank=True, null=True)  # Field name made lowercase.
    nom_mest = models.CharField(db_column='NOM_MEST', max_length=33, blank=True, null=True)  # Field name made lowercase.
    chv_cod_dig = models.CharField(db_column='CHV_COD_DIG', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c700'


class RegC790(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c790'


class RegC791(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c791'


class RegC800(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    num_cfe = models.CharField(db_column='NUM_CFE', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_cfe = models.DecimalField(db_column='VL_CFE', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf = models.CharField(db_column='CNPJ_CPF', max_length=14, blank=True, null=True)  # Field name made lowercase.
    nr_sat = models.CharField(db_column='NR_SAT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    chv_cfe = models.CharField(db_column='CHV_CFE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_merc = models.DecimalField(db_column='VL_MERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_da = models.DecimalField(db_column='VL_OUT_DA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis_st = models.DecimalField(db_column='VL_PIS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins_st = models.DecimalField(db_column='VL_COFINS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c800'


class RegC850(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c850'


class RegC860(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nr_sat = models.CharField(db_column='NR_SAT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    doc_ini = models.CharField(db_column='DOC_INI', max_length=6, blank=True, null=True)  # Field name made lowercase.
    doc_fim = models.CharField(db_column='DOC_FIM', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c860'


class RegC890(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_c890'
# Unable to inspect table 'reg_c990'
# The error was: (1932, "Table 'bd20190207165244.reg_c990' doesn't exist in engine")
# Unable to inspect table 'reg_d001'
# The error was: (1932, "Table 'bd20190207165244.reg_d001' doesn't exist in engine")


class RegD100(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_oper = models.CharField(db_column='IND_OPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    chv_cte = models.CharField(db_column='CHV_CTE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    dt_a_p = models.DateField(db_column='DT_A_P', blank=True, null=True)  # Field name made lowercase.
    tp_ct_e = models.CharField(db_column='TP_CT_E', max_length=1, blank=True, null=True)  # Field name made lowercase.
    chv_cte_ref = models.CharField(db_column='CHV_CTE_REF', max_length=44, blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_frt = models.CharField(db_column='IND_FRT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_nt = models.DecimalField(db_column='VL_NT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_inf = models.CharField(db_column='COD_INF', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cod_mun_dest = models.CharField(db_column='COD_MUN_DEST', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d100'


class RegD101(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_fcp_uf_dest = models.DecimalField(db_column='VL_FCP_UF_DEST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_uf_dest = models.DecimalField(db_column='VL_ICMS_UF_DEST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_uf_rem = models.DecimalField(db_column='VL_ICMS_UF_REM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d101'


class RegD110(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_item = models.CharField(db_column='NUM_ITEM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out = models.DecimalField(db_column='VL_OUT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d110'


class RegD120(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cod_mun_dest = models.CharField(db_column='COD_MUN_DEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    veic_id = models.CharField(db_column='VEIC_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.
    uf_id = models.CharField(db_column='UF_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d120'


class RegD130(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part_consg = models.CharField(db_column='COD_PART_CONSG', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_part_red = models.CharField(db_column='COD_PART_RED', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ind_frt_red = models.CharField(db_column='IND_FRT_RED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cod_mun_dest = models.CharField(db_column='COD_MUN_DEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    veic_id = models.CharField(db_column='VEIC_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.
    vl_liq_frt = models.DecimalField(db_column='VL_LIQ_FRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sec_cat = models.DecimalField(db_column='VL_SEC_CAT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desp = models.DecimalField(db_column='VL_DESP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pedg = models.DecimalField(db_column='VL_PEDG', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out = models.DecimalField(db_column='VL_OUT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_frt = models.DecimalField(db_column='VL_FRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    uf_id = models.CharField(db_column='UF_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d130'


class RegD140(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part_consg = models.CharField(db_column='COD_PART_CONSG', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cod_mun_dest = models.CharField(db_column='COD_MUN_DEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ind_veic = models.CharField(db_column='IND_VEIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    veic_id = models.CharField(db_column='VEIC_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ind_nav = models.CharField(db_column='IND_NAV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    viagem = models.CharField(db_column='VIAGEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_frt_liq = models.DecimalField(db_column='VL_FRT_LIQ', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desp_port = models.DecimalField(db_column='VL_DESP_PORT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desp_car_desc = models.DecimalField(db_column='VL_DESP_CAR_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out = models.DecimalField(db_column='VL_OUT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_frt_brt = models.DecimalField(db_column='VL_FRT_BRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_frt_mm = models.DecimalField(db_column='VL_FRT_MM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d140'


class RegD150(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cod_mun_dest = models.CharField(db_column='COD_MUN_DEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    veic_id = models.CharField(db_column='VEIC_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    viagem = models.CharField(db_column='VIAGEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ind_tfa = models.CharField(db_column='IND_TFA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_peso_tx = models.DecimalField(db_column='VL_PESO_TX', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tx_terr = models.DecimalField(db_column='VL_TX_TERR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tx_red = models.DecimalField(db_column='VL_TX_RED', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out = models.DecimalField(db_column='VL_OUT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tx_adv = models.DecimalField(db_column='VL_TX_ADV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d150'


class RegD160(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    despacho = models.CharField(db_column='DESPACHO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf_rem = models.CharField(db_column='CNPJ_CPF_REM', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ie_rem = models.CharField(db_column='IE_REM', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cod_mun_ori = models.CharField(db_column='COD_MUN_ORI', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf_dest = models.CharField(db_column='CNPJ_CPF_DEST', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ie_dest = models.CharField(db_column='IE_DEST', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cod_mun_dest = models.CharField(db_column='COD_MUN_DEST', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d160'


class RegD161(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_carga = models.CharField(db_column='IND_CARGA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf_col = models.CharField(db_column='CNPJ_CPF_COL', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ie_col = models.CharField(db_column='IE_COL', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cod_mun_col = models.CharField(db_column='COD_MUN_COL', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf_entg = models.CharField(db_column='CNPJ_CPF_ENTG', max_length=14, blank=True, null=True)  # Field name made lowercase.
    ie_entg = models.CharField(db_column='IE_ENTG', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cod_mun_entg = models.CharField(db_column='COD_MUN_ENTG', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d161'


class RegD162(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_merc = models.DecimalField(db_column='VL_MERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtd_vol = models.CharField(db_column='QTD_VOL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    peso_brt = models.DecimalField(db_column='PESO_BRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    peso_liq = models.DecimalField(db_column='PESO_LIQ', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d162'


class RegD170(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part_consg = models.CharField(db_column='COD_PART_CONSG', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_part_red = models.CharField(db_column='COD_PART_RED', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cod_mun_dest = models.CharField(db_column='COD_MUN_DEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    otm = models.CharField(db_column='OTM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ind_nat_frt = models.CharField(db_column='IND_NAT_FRT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_liq_frt = models.DecimalField(db_column='VL_LIQ_FRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_gris = models.DecimalField(db_column='VL_GRIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pdg = models.DecimalField(db_column='VL_PDG', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out = models.DecimalField(db_column='VL_OUT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_frt = models.DecimalField(db_column='VL_FRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    veic_id = models.CharField(db_column='VEIC_ID', max_length=7, blank=True, null=True)  # Field name made lowercase.
    uf_id = models.CharField(db_column='UF_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d170'


class RegD180(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_seq = models.CharField(db_column='NUM_SEQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf_emit = models.CharField(db_column='CNPJ_CPF_EMIT', max_length=14, blank=True, null=True)  # Field name made lowercase.
    uf_emit = models.CharField(db_column='UF_EMIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ie_emit = models.CharField(db_column='IE_EMIT', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf_tom = models.CharField(db_column='CNPJ_CPF_TOM', max_length=14, blank=True, null=True)  # Field name made lowercase.
    uf_tom = models.CharField(db_column='UF_TOM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ie_tom = models.CharField(db_column='IE_TOM', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cod_mun_dest = models.CharField(db_column='COD_MUN_DEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d180'


class RegD190(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d190'


class RegD195(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d195'


class RegD197(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_aj = models.CharField(db_column='COD_AJ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    descr_compl_aj = models.CharField(db_column='DESCR_COMPL_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_outros = models.DecimalField(db_column='VL_OUTROS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d197'


class RegD300(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_doc_ini = models.CharField(db_column='NUM_DOC_INI', max_length=6, blank=True, null=True)  # Field name made lowercase.
    num_doc_fin = models.CharField(db_column='NUM_DOC_FIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_seg = models.DecimalField(db_column='VL_SEG', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_desp = models.DecimalField(db_column='VL_OUT_DESP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d300'


class RegD301(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_doc_canc = models.CharField(db_column='NUM_DOC_CANC', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d301'


class RegD310(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d310'


class RegD350(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ecf_mod = models.CharField(db_column='ECF_MOD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ecf_fab = models.CharField(db_column='ECF_FAB', max_length=21, blank=True, null=True)  # Field name made lowercase.
    ecf_cx = models.CharField(db_column='ECF_CX', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d350'


class RegD355(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cro = models.CharField(db_column='CRO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    crz = models.CharField(db_column='CRZ', max_length=6, blank=True, null=True)  # Field name made lowercase.
    num_coo_fin = models.CharField(db_column='NUM_COO_FIN', max_length=9, blank=True, null=True)  # Field name made lowercase.
    gt_fin = models.DecimalField(db_column='GT_FIN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_brt = models.DecimalField(db_column='VL_BRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d355'


class RegD360(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d360'


class RegD365(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_tot_par = models.CharField(db_column='COD_TOT_PAR', max_length=7, blank=True, null=True)  # Field name made lowercase.
    vlr_acum_tot = models.DecimalField(db_column='VLR_ACUM_TOT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nr_tot = models.CharField(db_column='NR_TOT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    descr_nr_tot = models.CharField(db_column='DESCR_NR_TOT', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d365'


class RegD370(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtd_bilh = models.CharField(db_column='QTD_BILH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d370'


class RegD390(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_issqn = models.DecimalField(db_column='VL_BC_ISSQN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_issqn = models.DecimalField(db_column='ALIQ_ISSQN', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_issqn = models.DecimalField(db_column='VL_ISSQN', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d390'


class RegD400(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d400'


class RegD410(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc_ini = models.CharField(db_column='NUM_DOC_INI', max_length=6, blank=True, null=True)  # Field name made lowercase.
    num_doc_fin = models.CharField(db_column='NUM_DOC_FIN', max_length=6, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d410'


class RegD411(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_doc_canc = models.CharField(db_column='NUM_DOC_CANC', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d411'


class RegD420(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mun_orig = models.CharField(db_column='COD_MUN_ORIG', max_length=7, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d420'


class RegD500(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_oper = models.CharField(db_column='IND_OPER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    dt_a_p = models.DateField(db_column='DT_A_P', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv_nt = models.DecimalField(db_column='VL_SERV_NT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_terc = models.DecimalField(db_column='VL_TERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_da = models.DecimalField(db_column='VL_DA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_inf = models.CharField(db_column='COD_INF', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tp_assinante = models.CharField(db_column='TP_ASSINANTE', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d500'


class RegD510(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_item = models.CharField(db_column='NUM_ITEM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_class = models.CharField(db_column='COD_CLASS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_rec = models.CharField(db_column='IND_REC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d510'


class RegD530(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_serv = models.CharField(db_column='IND_SERV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dt_ini_serv = models.DateField(db_column='DT_INI_SERV', blank=True, null=True)  # Field name made lowercase.
    dt_fin_serv = models.DateField(db_column='DT_FIN_SERV', blank=True, null=True)  # Field name made lowercase.
    per_fiscal = models.CharField(db_column='PER_FISCAL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cod_area = models.CharField(db_column='COD_AREA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    terminal = models.CharField(db_column='TERMINAL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d530'


class RegD590(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d590'


class RegD600(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mun = models.CharField(db_column='COD_MUN', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_cons = models.CharField(db_column='COD_CONS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    qtd_cons = models.CharField(db_column='QTD_CONS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    vl_doc = models.DecimalField(db_column='VL_DOC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv = models.DecimalField(db_column='VL_SERV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_serv_nt = models.DecimalField(db_column='VL_SERV_NT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_terc = models.DecimalField(db_column='VL_TERC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_da = models.DecimalField(db_column='VL_DA', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d600'


class RegD610(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_class = models.CharField(db_column='COD_CLASS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_desc = models.DecimalField(db_column='VL_DESC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_pis = models.DecimalField(db_column='VL_PIS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cofins = models.DecimalField(db_column='VL_COFINS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d610'


class RegD690(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d690'


class RegD695(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nro_ord_ini = models.CharField(db_column='NRO_ORD_INI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nro_ord_fin = models.CharField(db_column='NRO_ORD_FIN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dt_doc_ini = models.DateField(db_column='DT_DOC_INI', blank=True, null=True)  # Field name made lowercase.
    dt_doc_fin = models.DateField(db_column='DT_DOC_FIN', blank=True, null=True)  # Field name made lowercase.
    nom_mest = models.CharField(db_column='NOM_MEST', max_length=33, blank=True, null=True)  # Field name made lowercase.
    chv_cod_dig = models.CharField(db_column='CHV_COD_DIG', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d695'


class RegD696(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    aliq_icms = models.DecimalField(db_column='ALIQ_ICMS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_opr = models.DecimalField(db_column='VL_OPR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms = models.DecimalField(db_column='VL_BC_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_red_bc = models.DecimalField(db_column='VL_RED_BC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_obs = models.CharField(db_column='COD_OBS', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d696'


class RegD697(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_icms_st = models.DecimalField(db_column='VL_BC_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_st = models.DecimalField(db_column='VL_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_d697'
# Unable to inspect table 'reg_d990'
# The error was: (1932, "Table 'bd20190207165244.reg_d990' doesn't exist in engine")
# Unable to inspect table 'reg_e001'
# The error was: (1932, "Table 'bd20190207165244.reg_e001' doesn't exist in engine")


class RegE100(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e100'


class RegE110(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_tot_debitos = models.DecimalField(db_column='VL_TOT_DEBITOS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_aj_debitos = models.DecimalField(db_column='VL_AJ_DEBITOS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_aj_debitos = models.DecimalField(db_column='VL_TOT_AJ_DEBITOS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_estornos_cred = models.DecimalField(db_column='VL_ESTORNOS_CRED', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_creditos = models.DecimalField(db_column='VL_TOT_CREDITOS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_aj_creditos = models.DecimalField(db_column='VL_AJ_CREDITOS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_aj_creditos = models.DecimalField(db_column='VL_TOT_AJ_CREDITOS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_estornos_deb = models.DecimalField(db_column='VL_ESTORNOS_DEB', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_credor_ant = models.DecimalField(db_column='VL_SLD_CREDOR_ANT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_apurado = models.DecimalField(db_column='VL_SLD_APURADO', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_ded = models.DecimalField(db_column='VL_TOT_DED', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_recolher = models.DecimalField(db_column='VL_ICMS_RECOLHER', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_credor_transportar = models.DecimalField(db_column='VL_SLD_CREDOR_TRANSPORTAR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deb_esp = models.DecimalField(db_column='DEB_ESP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e110'


class RegE111(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_aj_apur = models.CharField(db_column='COD_AJ_APUR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    descr_compl_aj = models.CharField(db_column='DESCR_COMPL_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_aj_apur = models.DecimalField(db_column='VL_AJ_APUR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e111'


class RegE112(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_da = models.CharField(db_column='NUM_DA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc = models.CharField(db_column='PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e112'


class RegE113(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_aj_item = models.DecimalField(db_column='VL_AJ_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chv_doce = models.CharField(db_column='CHV_DOCE', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e113'


class RegE115(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_inf_adic = models.CharField(db_column='COD_INF_ADIC', max_length=8, blank=True, null=True)  # Field name made lowercase.
    vl_inf_adic = models.DecimalField(db_column='VL_INF_ADIC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descr_compl_aj = models.CharField(db_column='DESCR_COMPL_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e115'


class RegE116(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_or = models.CharField(db_column='COD_OR', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vl_or = models.DecimalField(db_column='VL_OR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dt_vcto = models.DateField(db_column='DT_VCTO', blank=True, null=True)  # Field name made lowercase.
    cod_rec = models.CharField(db_column='COD_REC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc = models.CharField(db_column='PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mes_ref = models.CharField(db_column='MES_REF', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e116'


class RegE200(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e200'


class RegE210(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_mov_st = models.CharField(db_column='IND_MOV_ST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_sld_cred_ant_st = models.DecimalField(db_column='VL_SLD_CRED_ANT_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_devol_st = models.DecimalField(db_column='VL_DEVOL_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_ressarc_st = models.DecimalField(db_column='VL_RESSARC_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_cred_st = models.DecimalField(db_column='VL_OUT_CRED_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_aj_creditos_st = models.DecimalField(db_column='VL_AJ_CREDITOS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_retencao_st = models.DecimalField(db_column='VL_RETENCAO_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_deb_st = models.DecimalField(db_column='VL_OUT_DEB_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_aj_debitos_st = models.DecimalField(db_column='VL_AJ_DEBITOS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_dev_ant_st = models.DecimalField(db_column='VL_SLD_DEV_ANT_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_deducoes_st = models.DecimalField(db_column='VL_DEDUCOES_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms_recol_st = models.DecimalField(db_column='VL_ICMS_RECOL_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_cred_st_transportar = models.DecimalField(db_column='VL_SLD_CRED_ST_TRANSPORTAR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deb_esp_st = models.DecimalField(db_column='DEB_ESP_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e210'


class RegE220(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_aj_apur = models.CharField(db_column='COD_AJ_APUR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    descr_compl_aj = models.CharField(db_column='DESCR_COMPL_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_aj_apur = models.DecimalField(db_column='VL_AJ_APUR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e220'


class RegE230(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_da = models.CharField(db_column='NUM_DA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc = models.CharField(db_column='PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e230'


class RegE240(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_aj_item = models.DecimalField(db_column='VL_AJ_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chv_doce = models.CharField(db_column='CHV_DOCE', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e240'


class RegE250(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_or = models.CharField(db_column='COD_OR', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vl_or = models.DecimalField(db_column='VL_OR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dt_vcto = models.DateField(db_column='DT_VCTO', blank=True, null=True)  # Field name made lowercase.
    cod_rec = models.CharField(db_column='COD_REC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc = models.CharField(db_column='PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mes_ref = models.CharField(db_column='MES_REF', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e250'


class RegE300(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e300'


class RegE310(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_mov_difal = models.CharField(db_column='IND_MOV_DIFAL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_sld_cred_ant_difal = models.DecimalField(db_column='VL_SLD_CRED_ANT_DIFAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_debitos_difal = models.DecimalField(db_column='VL_TOT_DEBITOS_DIFAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_deb_difal = models.DecimalField(db_column='VL_OUT_DEB_DIFAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_creditos_difal = models.DecimalField(db_column='VL_TOT_CREDITOS_DIFAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_cred_difal = models.DecimalField(db_column='VL_OUT_CRED_DIFAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_dev_ant_difal = models.DecimalField(db_column='VL_SLD_DEV_ANT_DIFAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_deducoes_difal = models.DecimalField(db_column='VL_DEDUCOES_DIFAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_recol = models.DecimalField(db_column='VL_RECOL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_cred_transportar = models.DecimalField(db_column='VL_SLD_CRED_TRANSPORTAR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deb_esp_difal = models.DecimalField(db_column='DEB_ESP_DIFAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_cred_ant_fcp = models.DecimalField(db_column='VL_SLD_CRED_ANT_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_deb_fcp = models.DecimalField(db_column='VL_TOT_DEB_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_deb_fcp = models.DecimalField(db_column='VL_OUT_DEB_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_tot_cred_fcp = models.DecimalField(db_column='VL_TOT_CRED_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_out_cred_fcp = models.DecimalField(db_column='VL_OUT_CRED_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_dev_ant_fcp = models.DecimalField(db_column='VL_SLD_DEV_ANT_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_deducoes_fcp = models.DecimalField(db_column='VL_DEDUCOES_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_recol_fcp = models.DecimalField(db_column='VL_RECOL_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sld_cred_transportar_fcp = models.DecimalField(db_column='VL_SLD_CRED_TRANSPORTAR_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deb_esp_fcp = models.DecimalField(db_column='DEB_ESP_FCP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e310'


class RegE311(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_aj_apur = models.CharField(db_column='COD_AJ_APUR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    descr_compl_aj = models.CharField(db_column='DESCR_COMPL_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_aj_apur = models.DecimalField(db_column='VL_AJ_APUR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e311'


class RegE312(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_da = models.CharField(db_column='NUM_DA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc = models.CharField(db_column='PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e312'


class RegE313(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    chv_doce = models.CharField(db_column='CHV_DOCE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    vl_aj_item = models.DecimalField(db_column='VL_AJ_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e313'


class RegE316(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_or = models.CharField(db_column='COD_OR', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vl_or = models.DecimalField(db_column='VL_OR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dt_vcto = models.DateField(db_column='DT_VCTO', blank=True, null=True)  # Field name made lowercase.
    cod_rec = models.CharField(db_column='COD_REC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    num_proc = models.CharField(db_column='NUM_PROC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ind_proc = models.CharField(db_column='IND_PROC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proc = models.CharField(db_column='PROC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mes_ref = models.CharField(db_column='MES_REF', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e316'


class RegE500(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_apur = models.CharField(db_column='IND_APUR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e500'


class RegE510(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_ipi = models.CharField(db_column='CST_IPI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vl_cont_ipi = models.DecimalField(db_column='VL_CONT_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_bc_ipi = models.DecimalField(db_column='VL_BC_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_ipi = models.DecimalField(db_column='VL_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e510'


class RegE520(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vl_sd_ant_ipi = models.DecimalField(db_column='VL_SD_ANT_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_deb_ipi = models.DecimalField(db_column='VL_DEB_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_cred_ipi = models.DecimalField(db_column='VL_CRED_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_od_ipi = models.DecimalField(db_column='VL_OD_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_oc_ipi = models.DecimalField(db_column='VL_OC_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sc_ipi = models.DecimalField(db_column='VL_SC_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_sd_ipi = models.DecimalField(db_column='VL_SD_IPI', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e520'


class RegE530(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_aj = models.CharField(db_column='IND_AJ', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vl_aj = models.DecimalField(db_column='VL_AJ', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_aj = models.CharField(db_column='COD_AJ', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ind_doc = models.CharField(db_column='IND_DOC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descr_aj = models.CharField(db_column='DESCR_AJ', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e530'


class RegE531(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ser = models.CharField(db_column='SER', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sub = models.CharField(db_column='SUB', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_aj_item = models.DecimalField(db_column='VL_AJ_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    chv_nfe = models.CharField(db_column='CHV_NFE', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_e531'
# Unable to inspect table 'reg_e990'
# The error was: (1932, "Table 'bd20190207165244.reg_e990' doesn't exist in engine")
# Unable to inspect table 'reg_g001'
# The error was: (1932, "Table 'bd20190207165244.reg_g001' doesn't exist in engine")


class RegG110(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.
    saldo_in_icms = models.DecimalField(db_column='SALDO_IN_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    som_parc = models.DecimalField(db_column='SOM_PARC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_trib_exp = models.DecimalField(db_column='VL_TRIB_EXP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_total = models.DecimalField(db_column='VL_TOTAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_per_sai = models.DecimalField(db_column='IND_PER_SAI', max_digits=27, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    icms_aprop = models.DecimalField(db_column='ICMS_APROP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    som_icms_oc = models.DecimalField(db_column='SOM_ICMS_OC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_g110'


class RegG125(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_ind_bem = models.CharField(db_column='COD_IND_BEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dt_mov = models.DateField(db_column='DT_MOV', blank=True, null=True)  # Field name made lowercase.
    tipo_mov = models.CharField(db_column='TIPO_MOV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    vl_imob_icms_op = models.DecimalField(db_column='VL_IMOB_ICMS_OP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_imob_icms_st = models.DecimalField(db_column='VL_IMOB_ICMS_ST', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_imob_icms_frt = models.DecimalField(db_column='VL_IMOB_ICMS_FRT', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_imob_icms_dif = models.DecimalField(db_column='VL_IMOB_ICMS_DIF', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    num_parc = models.CharField(db_column='NUM_PARC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vl_parc_pass = models.DecimalField(db_column='VL_PARC_PASS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_g125'


class RegG126(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.
    num_parc = models.CharField(db_column='NUM_PARC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vl_parc_pass = models.DecimalField(db_column='VL_PARC_PASS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_trib_oc = models.DecimalField(db_column='VL_TRIB_OC', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_total = models.DecimalField(db_column='VL_TOTAL', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_per_sai = models.DecimalField(db_column='IND_PER_SAI', max_digits=27, decimal_places=8, blank=True, null=True)  # Field name made lowercase.
    vl_parc_aprop = models.DecimalField(db_column='VL_PARC_APROP', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_g126'


class RegG130(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ind_emit = models.CharField(db_column='IND_EMIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_doc = models.CharField(db_column='NUM_DOC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    chv_nfe_cte = models.CharField(db_column='CHV_NFE_CTE', max_length=44, blank=True, null=True)  # Field name made lowercase.
    dt_doc = models.DateField(db_column='DT_DOC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_g130'


class RegG140(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    num_item = models.CharField(db_column='NUM_ITEM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_g140'
# Unable to inspect table 'reg_g990'
# The error was: (1932, "Table 'bd20190207165244.reg_g990' doesn't exist in engine")
# Unable to inspect table 'reg_h001'
# The error was: (1932, "Table 'bd20190207165244.reg_h001' doesn't exist in engine")


class RegH005(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_inv = models.DateField(db_column='DT_INV', blank=True, null=True)  # Field name made lowercase.
    vl_inv = models.DecimalField(db_column='VL_INV', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mot_inv = models.CharField(db_column='MOT_INV', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_h005'


class RegH010(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=6, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    vl_unit = models.DecimalField(db_column='VL_UNIT', max_digits=25, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    vl_item = models.DecimalField(db_column='VL_ITEM', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ind_prop = models.CharField(db_column='IND_PROP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.
    txt_compl = models.CharField(db_column='TXT_COMPL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_cta = models.CharField(db_column='COD_CTA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vl_item_ir = models.DecimalField(db_column='VL_ITEM_IR', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_h010'


class RegH020(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cst_icms = models.CharField(db_column='CST_ICMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bl_icms = models.DecimalField(db_column='BL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vl_icms = models.DecimalField(db_column='VL_ICMS', max_digits=21, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_h020'
# Unable to inspect table 'reg_h990'
# The error was: (1932, "Table 'bd20190207165244.reg_h990' doesn't exist in engine")
# Unable to inspect table 'reg_k001'
# The error was: (1932, "Table 'bd20190207165244.reg_k001' doesn't exist in engine")


class RegK100(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_ini = models.DateField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase.
    dt_fin = models.DateField(db_column='DT_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k100'


class RegK200(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_est = models.DateField(db_column='DT_EST', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ind_est = models.CharField(db_column='IND_EST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k200'


class RegK210(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_ini_os = models.DateField(db_column='DT_INI_OS', blank=True, null=True)  # Field name made lowercase.
    dt_fin_os = models.DateField(db_column='DT_FIN_OS', blank=True, null=True)  # Field name made lowercase.
    cod_doc_os = models.CharField(db_column='COD_DOC_OS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_item_ori = models.CharField(db_column='COD_ITEM_ORI', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_ori = models.DecimalField(db_column='QTD_ORI', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k210'


class RegK215(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item_dest = models.CharField(db_column='COD_ITEM_DEST', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_des = models.DecimalField(db_column='QTD_DES', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k215'


class RegK220(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_mov = models.DateField(db_column='DT_MOV', blank=True, null=True)  # Field name made lowercase.
    cod_item_ori = models.CharField(db_column='COD_ITEM_ORI', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_item_dest = models.CharField(db_column='COD_ITEM_DEST', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_ori = models.DecimalField(db_column='QTD_ORI', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtd_dest = models.DecimalField(db_column='QTD_DEST', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k220'


class RegK230(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_ini_op = models.DateField(db_column='DT_INI_OP', blank=True, null=True)  # Field name made lowercase.
    dt_fin_op = models.DateField(db_column='DT_FIN_OP', blank=True, null=True)  # Field name made lowercase.
    cod_doc_op = models.CharField(db_column='COD_DOC_OP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_enc = models.DecimalField(db_column='QTD_ENC', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k230'


class RegK235(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_saida = models.DateField(db_column='DT_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cod_ins_subst = models.CharField(db_column='COD_INS_SUBST', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k235'


class RegK250(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_prod = models.DateField(db_column='DT_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k250'


class RegK255(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_cons = models.DateField(db_column='DT_CONS', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd = models.DecimalField(db_column='QTD', max_digits=20, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cod_ins_subst = models.CharField(db_column='COD_INS_SUBST', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k255'


class RegK260(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_op_os = models.CharField(db_column='COD_OP_OS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dt_saida = models.DateField(db_column='DT_SAIDA', blank=True, null=True)  # Field name made lowercase.
    qtd_saida = models.DecimalField(db_column='QTD_SAIDA', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    dt_ret = models.DateField(db_column='DT_RET', blank=True, null=True)  # Field name made lowercase.
    qtd_ret = models.DecimalField(db_column='QTD_RET', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k260'


class RegK265(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_cons = models.DecimalField(db_column='QTD_CONS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtd_ret = models.DecimalField(db_column='QTD_RET', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k265'


class RegK270(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_ini_ap = models.DateField(db_column='DT_INI_AP', blank=True, null=True)  # Field name made lowercase.
    dt_fin_ap = models.DateField(db_column='DT_FIN_AP', blank=True, null=True)  # Field name made lowercase.
    cod_op_os = models.CharField(db_column='COD_OP_OS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_cor_pos = models.DecimalField(db_column='QTD_COR_POS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtd_cor_neg = models.DecimalField(db_column='QTD_COR_NEG', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    origem = models.CharField(db_column='ORIGEM', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k270'


class RegK275(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_cor_pos = models.DecimalField(db_column='QTD_COR_POS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtd_cor_neg = models.DecimalField(db_column='QTD_COR_NEG', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    cod_ins_subst = models.CharField(db_column='COD_INS_SUBST', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k275'


class RegK280(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_pai = models.BigIntegerField(db_column='ID_PAI')  # Field name made lowercase.
    linha = models.BigIntegerField(db_column='LINHA')  # Field name made lowercase.
    hash = models.BigIntegerField(db_column='HASH')  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dt_est = models.DateField(db_column='DT_EST', blank=True, null=True)  # Field name made lowercase.
    cod_item = models.CharField(db_column='COD_ITEM', max_length=60, blank=True, null=True)  # Field name made lowercase.
    qtd_cor_pos = models.DecimalField(db_column='QTD_COR_POS', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    qtd_cor_neg = models.DecimalField(db_column='QTD_COR_NEG', max_digits=22, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ind_est = models.CharField(db_column='IND_EST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_part = models.CharField(db_column='COD_PART', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reg_k280'
# Unable to inspect table 'reg_k990'
# The error was: (1932, "Table 'bd20190207165244.reg_k990' doesn't exist in engine")


class Tabelaexternareferenciada(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    versao = models.IntegerField()
    listaufs = models.CharField(db_column='listaUfs', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hash = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'tabelaexternareferenciada'

    def __str__(self):
        return self.tipo+" : "+self.listaufs