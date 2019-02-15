# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class GjeldEgenkapitalKonsern(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'regnskaps_av_ar_field': 'int',
        'regnskaps_av_mnd_field': 'int',
        'sum_egenkapital_field': 'int',
        'innskutt_egenkapital_field': 'int',
        'selskapskapital_field': 'int',
        'egne_aksjer_field': 'int',
        'overkursfond_field': 'int',
        'opptjent_egenkapital_field': 'int',
        'fond_for_vurd_field': 'int',
        'annen_egenkapital_field': 'int',
        'minoritetsinteresser_field': 'int',
        'sum_gjeld_field': 'int',
        'avsetning_forpliktelser_field': 'int',
        'pensjon_forpliktelser_field': 'int',
        'utsatt_skatt_field': 'int',
        'andre_avsetninger_field': 'int',
        'sum_langsiktig_gjeld_field': 'int',
        'annen_langsiktig_gjeld_field': 'int',
        'konvertible_lan_lang_field': 'int',
        'obligasjons_lan_field': 'int',
        'gjeld_kreditt_lang_field': 'int',
        'gjeld_konsern_lang_field': 'int',
        'ansvarlig_lanekapital_field': 'int',
        'ovrig_langsiktig_gjeld_field': 'int',
        'sum_kortsiktig_gjeld_field': 'int',
        'konvertible_lan_kort_field': 'int',
        'sertifikat_lan_field': 'int',
        'gjeld_kreditt_kort_field': 'int',
        'kassakreditt_field': 'int',
        'leverandor_gjeld_field': 'int',
        'betalbar_skatt_field': 'int',
        'skyld_offentlig_avgift_field': 'int',
        'gjeld_konsern_kort_field': 'int',
        'utbytte_field': 'int',
        'annen_kortsiktig_gjeld_field': 'int',
        'sum_gjeld_egenkapital_field': 'int',
        'kassekredittlimit_field': 'int',
        'skyld_konsernbidrag_field': 'int',
        'avdrag_langsiktig_gjeld_field': 'int'
    }

    attribute_map = {
        'regnskaps_av_ar_field': 'regnskapsAvArField',
        'regnskaps_av_mnd_field': 'regnskapsAvMndField',
        'sum_egenkapital_field': 'sumEgenkapitalField',
        'innskutt_egenkapital_field': 'innskuttEgenkapitalField',
        'selskapskapital_field': 'selskapskapitalField',
        'egne_aksjer_field': 'egneAksjerField',
        'overkursfond_field': 'overkursfondField',
        'opptjent_egenkapital_field': 'opptjentEgenkapitalField',
        'fond_for_vurd_field': 'fondForVurdField',
        'annen_egenkapital_field': 'annenEgenkapitalField',
        'minoritetsinteresser_field': 'minoritetsinteresserField',
        'sum_gjeld_field': 'sumGjeldField',
        'avsetning_forpliktelser_field': 'avsetningForpliktelserField',
        'pensjon_forpliktelser_field': 'pensjonForpliktelserField',
        'utsatt_skatt_field': 'utsattSkattField',
        'andre_avsetninger_field': 'andreAvsetningerField',
        'sum_langsiktig_gjeld_field': 'sumLangsiktigGjeldField',
        'annen_langsiktig_gjeld_field': 'annenLangsiktigGjeldField',
        'konvertible_lan_lang_field': 'konvertibleLanLangField',
        'obligasjons_lan_field': 'obligasjonsLanField',
        'gjeld_kreditt_lang_field': 'gjeldKredittLangField',
        'gjeld_konsern_lang_field': 'gjeldKonsernLangField',
        'ansvarlig_lanekapital_field': 'ansvarligLanekapitalField',
        'ovrig_langsiktig_gjeld_field': 'ovrigLangsiktigGjeldField',
        'sum_kortsiktig_gjeld_field': 'sumKortsiktigGjeldField',
        'konvertible_lan_kort_field': 'konvertibleLanKortField',
        'sertifikat_lan_field': 'sertifikatLanField',
        'gjeld_kreditt_kort_field': 'gjeldKredittKortField',
        'kassakreditt_field': 'kassakredittField',
        'leverandor_gjeld_field': 'leverandorGjeldField',
        'betalbar_skatt_field': 'betalbarSkattField',
        'skyld_offentlig_avgift_field': 'skyldOffentligAvgiftField',
        'gjeld_konsern_kort_field': 'gjeldKonsernKortField',
        'utbytte_field': 'utbytteField',
        'annen_kortsiktig_gjeld_field': 'annenKortsiktigGjeldField',
        'sum_gjeld_egenkapital_field': 'sumGjeldEgenkapitalField',
        'kassekredittlimit_field': 'kassekredittlimitField',
        'skyld_konsernbidrag_field': 'skyldKonsernbidragField',
        'avdrag_langsiktig_gjeld_field': 'avdragLangsiktigGjeldField'
    }

    def __init__(self, regnskaps_av_ar_field=None, regnskaps_av_mnd_field=None, sum_egenkapital_field=None, innskutt_egenkapital_field=None, selskapskapital_field=None, egne_aksjer_field=None, overkursfond_field=None, opptjent_egenkapital_field=None, fond_for_vurd_field=None, annen_egenkapital_field=None, minoritetsinteresser_field=None, sum_gjeld_field=None, avsetning_forpliktelser_field=None, pensjon_forpliktelser_field=None, utsatt_skatt_field=None, andre_avsetninger_field=None, sum_langsiktig_gjeld_field=None, annen_langsiktig_gjeld_field=None, konvertible_lan_lang_field=None, obligasjons_lan_field=None, gjeld_kreditt_lang_field=None, gjeld_konsern_lang_field=None, ansvarlig_lanekapital_field=None, ovrig_langsiktig_gjeld_field=None, sum_kortsiktig_gjeld_field=None, konvertible_lan_kort_field=None, sertifikat_lan_field=None, gjeld_kreditt_kort_field=None, kassakreditt_field=None, leverandor_gjeld_field=None, betalbar_skatt_field=None, skyld_offentlig_avgift_field=None, gjeld_konsern_kort_field=None, utbytte_field=None, annen_kortsiktig_gjeld_field=None, sum_gjeld_egenkapital_field=None, kassekredittlimit_field=None, skyld_konsernbidrag_field=None, avdrag_langsiktig_gjeld_field=None):  
        """GjeldEgenkapitalKonsern"""  

        self._regnskaps_av_ar_field = None
        self._regnskaps_av_mnd_field = None
        self._sum_egenkapital_field = None
        self._innskutt_egenkapital_field = None
        self._selskapskapital_field = None
        self._egne_aksjer_field = None
        self._overkursfond_field = None
        self._opptjent_egenkapital_field = None
        self._fond_for_vurd_field = None
        self._annen_egenkapital_field = None
        self._minoritetsinteresser_field = None
        self._sum_gjeld_field = None
        self._avsetning_forpliktelser_field = None
        self._pensjon_forpliktelser_field = None
        self._utsatt_skatt_field = None
        self._andre_avsetninger_field = None
        self._sum_langsiktig_gjeld_field = None
        self._annen_langsiktig_gjeld_field = None
        self._konvertible_lan_lang_field = None
        self._obligasjons_lan_field = None
        self._gjeld_kreditt_lang_field = None
        self._gjeld_konsern_lang_field = None
        self._ansvarlig_lanekapital_field = None
        self._ovrig_langsiktig_gjeld_field = None
        self._sum_kortsiktig_gjeld_field = None
        self._konvertible_lan_kort_field = None
        self._sertifikat_lan_field = None
        self._gjeld_kreditt_kort_field = None
        self._kassakreditt_field = None
        self._leverandor_gjeld_field = None
        self._betalbar_skatt_field = None
        self._skyld_offentlig_avgift_field = None
        self._gjeld_konsern_kort_field = None
        self._utbytte_field = None
        self._annen_kortsiktig_gjeld_field = None
        self._sum_gjeld_egenkapital_field = None
        self._kassekredittlimit_field = None
        self._skyld_konsernbidrag_field = None
        self._avdrag_langsiktig_gjeld_field = None
        self.discriminator = None

        if regnskaps_av_ar_field is not None:
            self.regnskaps_av_ar_field = regnskaps_av_ar_field
        if regnskaps_av_mnd_field is not None:
            self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        if sum_egenkapital_field is not None:
            self.sum_egenkapital_field = sum_egenkapital_field
        if innskutt_egenkapital_field is not None:
            self.innskutt_egenkapital_field = innskutt_egenkapital_field
        if selskapskapital_field is not None:
            self.selskapskapital_field = selskapskapital_field
        if egne_aksjer_field is not None:
            self.egne_aksjer_field = egne_aksjer_field
        if overkursfond_field is not None:
            self.overkursfond_field = overkursfond_field
        if opptjent_egenkapital_field is not None:
            self.opptjent_egenkapital_field = opptjent_egenkapital_field
        if fond_for_vurd_field is not None:
            self.fond_for_vurd_field = fond_for_vurd_field
        if annen_egenkapital_field is not None:
            self.annen_egenkapital_field = annen_egenkapital_field
        if minoritetsinteresser_field is not None:
            self.minoritetsinteresser_field = minoritetsinteresser_field
        if sum_gjeld_field is not None:
            self.sum_gjeld_field = sum_gjeld_field
        if avsetning_forpliktelser_field is not None:
            self.avsetning_forpliktelser_field = avsetning_forpliktelser_field
        if pensjon_forpliktelser_field is not None:
            self.pensjon_forpliktelser_field = pensjon_forpliktelser_field
        if utsatt_skatt_field is not None:
            self.utsatt_skatt_field = utsatt_skatt_field
        if andre_avsetninger_field is not None:
            self.andre_avsetninger_field = andre_avsetninger_field
        if sum_langsiktig_gjeld_field is not None:
            self.sum_langsiktig_gjeld_field = sum_langsiktig_gjeld_field
        if annen_langsiktig_gjeld_field is not None:
            self.annen_langsiktig_gjeld_field = annen_langsiktig_gjeld_field
        if konvertible_lan_lang_field is not None:
            self.konvertible_lan_lang_field = konvertible_lan_lang_field
        if obligasjons_lan_field is not None:
            self.obligasjons_lan_field = obligasjons_lan_field
        if gjeld_kreditt_lang_field is not None:
            self.gjeld_kreditt_lang_field = gjeld_kreditt_lang_field
        if gjeld_konsern_lang_field is not None:
            self.gjeld_konsern_lang_field = gjeld_konsern_lang_field
        if ansvarlig_lanekapital_field is not None:
            self.ansvarlig_lanekapital_field = ansvarlig_lanekapital_field
        if ovrig_langsiktig_gjeld_field is not None:
            self.ovrig_langsiktig_gjeld_field = ovrig_langsiktig_gjeld_field
        if sum_kortsiktig_gjeld_field is not None:
            self.sum_kortsiktig_gjeld_field = sum_kortsiktig_gjeld_field
        if konvertible_lan_kort_field is not None:
            self.konvertible_lan_kort_field = konvertible_lan_kort_field
        if sertifikat_lan_field is not None:
            self.sertifikat_lan_field = sertifikat_lan_field
        if gjeld_kreditt_kort_field is not None:
            self.gjeld_kreditt_kort_field = gjeld_kreditt_kort_field
        if kassakreditt_field is not None:
            self.kassakreditt_field = kassakreditt_field
        if leverandor_gjeld_field is not None:
            self.leverandor_gjeld_field = leverandor_gjeld_field
        if betalbar_skatt_field is not None:
            self.betalbar_skatt_field = betalbar_skatt_field
        if skyld_offentlig_avgift_field is not None:
            self.skyld_offentlig_avgift_field = skyld_offentlig_avgift_field
        if gjeld_konsern_kort_field is not None:
            self.gjeld_konsern_kort_field = gjeld_konsern_kort_field
        if utbytte_field is not None:
            self.utbytte_field = utbytte_field
        if annen_kortsiktig_gjeld_field is not None:
            self.annen_kortsiktig_gjeld_field = annen_kortsiktig_gjeld_field
        if sum_gjeld_egenkapital_field is not None:
            self.sum_gjeld_egenkapital_field = sum_gjeld_egenkapital_field
        if kassekredittlimit_field is not None:
            self.kassekredittlimit_field = kassekredittlimit_field
        if skyld_konsernbidrag_field is not None:
            self.skyld_konsernbidrag_field = skyld_konsernbidrag_field
        if avdrag_langsiktig_gjeld_field is not None:
            self.avdrag_langsiktig_gjeld_field = avdrag_langsiktig_gjeld_field

    @property
    def regnskaps_av_ar_field(self):
        """Gets the regnskaps_av_ar_field of this GjeldEgenkapitalKonsern.  


        :return: The regnskaps_av_ar_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._regnskaps_av_ar_field

    @regnskaps_av_ar_field.setter
    def regnskaps_av_ar_field(self, regnskaps_av_ar_field):
        """Sets the regnskaps_av_ar_field of this GjeldEgenkapitalKonsern.


        :param regnskaps_av_ar_field: The regnskaps_av_ar_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._regnskaps_av_ar_field = regnskaps_av_ar_field

    @property
    def regnskaps_av_mnd_field(self):
        """Gets the regnskaps_av_mnd_field of this GjeldEgenkapitalKonsern.  


        :return: The regnskaps_av_mnd_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._regnskaps_av_mnd_field

    @regnskaps_av_mnd_field.setter
    def regnskaps_av_mnd_field(self, regnskaps_av_mnd_field):
        """Sets the regnskaps_av_mnd_field of this GjeldEgenkapitalKonsern.


        :param regnskaps_av_mnd_field: The regnskaps_av_mnd_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._regnskaps_av_mnd_field = regnskaps_av_mnd_field

    @property
    def sum_egenkapital_field(self):
        """Gets the sum_egenkapital_field of this GjeldEgenkapitalKonsern.  


        :return: The sum_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._sum_egenkapital_field

    @sum_egenkapital_field.setter
    def sum_egenkapital_field(self, sum_egenkapital_field):
        """Sets the sum_egenkapital_field of this GjeldEgenkapitalKonsern.


        :param sum_egenkapital_field: The sum_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._sum_egenkapital_field = sum_egenkapital_field

    @property
    def innskutt_egenkapital_field(self):
        """Gets the innskutt_egenkapital_field of this GjeldEgenkapitalKonsern.  


        :return: The innskutt_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._innskutt_egenkapital_field

    @innskutt_egenkapital_field.setter
    def innskutt_egenkapital_field(self, innskutt_egenkapital_field):
        """Sets the innskutt_egenkapital_field of this GjeldEgenkapitalKonsern.


        :param innskutt_egenkapital_field: The innskutt_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._innskutt_egenkapital_field = innskutt_egenkapital_field

    @property
    def selskapskapital_field(self):
        """Gets the selskapskapital_field of this GjeldEgenkapitalKonsern.  


        :return: The selskapskapital_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._selskapskapital_field

    @selskapskapital_field.setter
    def selskapskapital_field(self, selskapskapital_field):
        """Sets the selskapskapital_field of this GjeldEgenkapitalKonsern.


        :param selskapskapital_field: The selskapskapital_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._selskapskapital_field = selskapskapital_field

    @property
    def egne_aksjer_field(self):
        """Gets the egne_aksjer_field of this GjeldEgenkapitalKonsern.  


        :return: The egne_aksjer_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._egne_aksjer_field

    @egne_aksjer_field.setter
    def egne_aksjer_field(self, egne_aksjer_field):
        """Sets the egne_aksjer_field of this GjeldEgenkapitalKonsern.


        :param egne_aksjer_field: The egne_aksjer_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._egne_aksjer_field = egne_aksjer_field

    @property
    def overkursfond_field(self):
        """Gets the overkursfond_field of this GjeldEgenkapitalKonsern.  


        :return: The overkursfond_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._overkursfond_field

    @overkursfond_field.setter
    def overkursfond_field(self, overkursfond_field):
        """Sets the overkursfond_field of this GjeldEgenkapitalKonsern.


        :param overkursfond_field: The overkursfond_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._overkursfond_field = overkursfond_field

    @property
    def opptjent_egenkapital_field(self):
        """Gets the opptjent_egenkapital_field of this GjeldEgenkapitalKonsern.  


        :return: The opptjent_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._opptjent_egenkapital_field

    @opptjent_egenkapital_field.setter
    def opptjent_egenkapital_field(self, opptjent_egenkapital_field):
        """Sets the opptjent_egenkapital_field of this GjeldEgenkapitalKonsern.


        :param opptjent_egenkapital_field: The opptjent_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._opptjent_egenkapital_field = opptjent_egenkapital_field

    @property
    def fond_for_vurd_field(self):
        """Gets the fond_for_vurd_field of this GjeldEgenkapitalKonsern.  


        :return: The fond_for_vurd_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._fond_for_vurd_field

    @fond_for_vurd_field.setter
    def fond_for_vurd_field(self, fond_for_vurd_field):
        """Sets the fond_for_vurd_field of this GjeldEgenkapitalKonsern.


        :param fond_for_vurd_field: The fond_for_vurd_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._fond_for_vurd_field = fond_for_vurd_field

    @property
    def annen_egenkapital_field(self):
        """Gets the annen_egenkapital_field of this GjeldEgenkapitalKonsern.  


        :return: The annen_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._annen_egenkapital_field

    @annen_egenkapital_field.setter
    def annen_egenkapital_field(self, annen_egenkapital_field):
        """Sets the annen_egenkapital_field of this GjeldEgenkapitalKonsern.


        :param annen_egenkapital_field: The annen_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._annen_egenkapital_field = annen_egenkapital_field

    @property
    def minoritetsinteresser_field(self):
        """Gets the minoritetsinteresser_field of this GjeldEgenkapitalKonsern.  


        :return: The minoritetsinteresser_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._minoritetsinteresser_field

    @minoritetsinteresser_field.setter
    def minoritetsinteresser_field(self, minoritetsinteresser_field):
        """Sets the minoritetsinteresser_field of this GjeldEgenkapitalKonsern.


        :param minoritetsinteresser_field: The minoritetsinteresser_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._minoritetsinteresser_field = minoritetsinteresser_field

    @property
    def sum_gjeld_field(self):
        """Gets the sum_gjeld_field of this GjeldEgenkapitalKonsern.  


        :return: The sum_gjeld_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._sum_gjeld_field

    @sum_gjeld_field.setter
    def sum_gjeld_field(self, sum_gjeld_field):
        """Sets the sum_gjeld_field of this GjeldEgenkapitalKonsern.


        :param sum_gjeld_field: The sum_gjeld_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._sum_gjeld_field = sum_gjeld_field

    @property
    def avsetning_forpliktelser_field(self):
        """Gets the avsetning_forpliktelser_field of this GjeldEgenkapitalKonsern.  


        :return: The avsetning_forpliktelser_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._avsetning_forpliktelser_field

    @avsetning_forpliktelser_field.setter
    def avsetning_forpliktelser_field(self, avsetning_forpliktelser_field):
        """Sets the avsetning_forpliktelser_field of this GjeldEgenkapitalKonsern.


        :param avsetning_forpliktelser_field: The avsetning_forpliktelser_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._avsetning_forpliktelser_field = avsetning_forpliktelser_field

    @property
    def pensjon_forpliktelser_field(self):
        """Gets the pensjon_forpliktelser_field of this GjeldEgenkapitalKonsern.  


        :return: The pensjon_forpliktelser_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._pensjon_forpliktelser_field

    @pensjon_forpliktelser_field.setter
    def pensjon_forpliktelser_field(self, pensjon_forpliktelser_field):
        """Sets the pensjon_forpliktelser_field of this GjeldEgenkapitalKonsern.


        :param pensjon_forpliktelser_field: The pensjon_forpliktelser_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._pensjon_forpliktelser_field = pensjon_forpliktelser_field

    @property
    def utsatt_skatt_field(self):
        """Gets the utsatt_skatt_field of this GjeldEgenkapitalKonsern.  


        :return: The utsatt_skatt_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._utsatt_skatt_field

    @utsatt_skatt_field.setter
    def utsatt_skatt_field(self, utsatt_skatt_field):
        """Sets the utsatt_skatt_field of this GjeldEgenkapitalKonsern.


        :param utsatt_skatt_field: The utsatt_skatt_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._utsatt_skatt_field = utsatt_skatt_field

    @property
    def andre_avsetninger_field(self):
        """Gets the andre_avsetninger_field of this GjeldEgenkapitalKonsern.  


        :return: The andre_avsetninger_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._andre_avsetninger_field

    @andre_avsetninger_field.setter
    def andre_avsetninger_field(self, andre_avsetninger_field):
        """Sets the andre_avsetninger_field of this GjeldEgenkapitalKonsern.


        :param andre_avsetninger_field: The andre_avsetninger_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._andre_avsetninger_field = andre_avsetninger_field

    @property
    def sum_langsiktig_gjeld_field(self):
        """Gets the sum_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  


        :return: The sum_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._sum_langsiktig_gjeld_field

    @sum_langsiktig_gjeld_field.setter
    def sum_langsiktig_gjeld_field(self, sum_langsiktig_gjeld_field):
        """Sets the sum_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.


        :param sum_langsiktig_gjeld_field: The sum_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._sum_langsiktig_gjeld_field = sum_langsiktig_gjeld_field

    @property
    def annen_langsiktig_gjeld_field(self):
        """Gets the annen_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  


        :return: The annen_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._annen_langsiktig_gjeld_field

    @annen_langsiktig_gjeld_field.setter
    def annen_langsiktig_gjeld_field(self, annen_langsiktig_gjeld_field):
        """Sets the annen_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.


        :param annen_langsiktig_gjeld_field: The annen_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._annen_langsiktig_gjeld_field = annen_langsiktig_gjeld_field

    @property
    def konvertible_lan_lang_field(self):
        """Gets the konvertible_lan_lang_field of this GjeldEgenkapitalKonsern.  


        :return: The konvertible_lan_lang_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._konvertible_lan_lang_field

    @konvertible_lan_lang_field.setter
    def konvertible_lan_lang_field(self, konvertible_lan_lang_field):
        """Sets the konvertible_lan_lang_field of this GjeldEgenkapitalKonsern.


        :param konvertible_lan_lang_field: The konvertible_lan_lang_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._konvertible_lan_lang_field = konvertible_lan_lang_field

    @property
    def obligasjons_lan_field(self):
        """Gets the obligasjons_lan_field of this GjeldEgenkapitalKonsern.  


        :return: The obligasjons_lan_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._obligasjons_lan_field

    @obligasjons_lan_field.setter
    def obligasjons_lan_field(self, obligasjons_lan_field):
        """Sets the obligasjons_lan_field of this GjeldEgenkapitalKonsern.


        :param obligasjons_lan_field: The obligasjons_lan_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._obligasjons_lan_field = obligasjons_lan_field

    @property
    def gjeld_kreditt_lang_field(self):
        """Gets the gjeld_kreditt_lang_field of this GjeldEgenkapitalKonsern.  


        :return: The gjeld_kreditt_lang_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._gjeld_kreditt_lang_field

    @gjeld_kreditt_lang_field.setter
    def gjeld_kreditt_lang_field(self, gjeld_kreditt_lang_field):
        """Sets the gjeld_kreditt_lang_field of this GjeldEgenkapitalKonsern.


        :param gjeld_kreditt_lang_field: The gjeld_kreditt_lang_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._gjeld_kreditt_lang_field = gjeld_kreditt_lang_field

    @property
    def gjeld_konsern_lang_field(self):
        """Gets the gjeld_konsern_lang_field of this GjeldEgenkapitalKonsern.  


        :return: The gjeld_konsern_lang_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._gjeld_konsern_lang_field

    @gjeld_konsern_lang_field.setter
    def gjeld_konsern_lang_field(self, gjeld_konsern_lang_field):
        """Sets the gjeld_konsern_lang_field of this GjeldEgenkapitalKonsern.


        :param gjeld_konsern_lang_field: The gjeld_konsern_lang_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._gjeld_konsern_lang_field = gjeld_konsern_lang_field

    @property
    def ansvarlig_lanekapital_field(self):
        """Gets the ansvarlig_lanekapital_field of this GjeldEgenkapitalKonsern.  


        :return: The ansvarlig_lanekapital_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._ansvarlig_lanekapital_field

    @ansvarlig_lanekapital_field.setter
    def ansvarlig_lanekapital_field(self, ansvarlig_lanekapital_field):
        """Sets the ansvarlig_lanekapital_field of this GjeldEgenkapitalKonsern.


        :param ansvarlig_lanekapital_field: The ansvarlig_lanekapital_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._ansvarlig_lanekapital_field = ansvarlig_lanekapital_field

    @property
    def ovrig_langsiktig_gjeld_field(self):
        """Gets the ovrig_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  


        :return: The ovrig_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._ovrig_langsiktig_gjeld_field

    @ovrig_langsiktig_gjeld_field.setter
    def ovrig_langsiktig_gjeld_field(self, ovrig_langsiktig_gjeld_field):
        """Sets the ovrig_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.


        :param ovrig_langsiktig_gjeld_field: The ovrig_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._ovrig_langsiktig_gjeld_field = ovrig_langsiktig_gjeld_field

    @property
    def sum_kortsiktig_gjeld_field(self):
        """Gets the sum_kortsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  


        :return: The sum_kortsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._sum_kortsiktig_gjeld_field

    @sum_kortsiktig_gjeld_field.setter
    def sum_kortsiktig_gjeld_field(self, sum_kortsiktig_gjeld_field):
        """Sets the sum_kortsiktig_gjeld_field of this GjeldEgenkapitalKonsern.


        :param sum_kortsiktig_gjeld_field: The sum_kortsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._sum_kortsiktig_gjeld_field = sum_kortsiktig_gjeld_field

    @property
    def konvertible_lan_kort_field(self):
        """Gets the konvertible_lan_kort_field of this GjeldEgenkapitalKonsern.  


        :return: The konvertible_lan_kort_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._konvertible_lan_kort_field

    @konvertible_lan_kort_field.setter
    def konvertible_lan_kort_field(self, konvertible_lan_kort_field):
        """Sets the konvertible_lan_kort_field of this GjeldEgenkapitalKonsern.


        :param konvertible_lan_kort_field: The konvertible_lan_kort_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._konvertible_lan_kort_field = konvertible_lan_kort_field

    @property
    def sertifikat_lan_field(self):
        """Gets the sertifikat_lan_field of this GjeldEgenkapitalKonsern.  


        :return: The sertifikat_lan_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._sertifikat_lan_field

    @sertifikat_lan_field.setter
    def sertifikat_lan_field(self, sertifikat_lan_field):
        """Sets the sertifikat_lan_field of this GjeldEgenkapitalKonsern.


        :param sertifikat_lan_field: The sertifikat_lan_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._sertifikat_lan_field = sertifikat_lan_field

    @property
    def gjeld_kreditt_kort_field(self):
        """Gets the gjeld_kreditt_kort_field of this GjeldEgenkapitalKonsern.  


        :return: The gjeld_kreditt_kort_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._gjeld_kreditt_kort_field

    @gjeld_kreditt_kort_field.setter
    def gjeld_kreditt_kort_field(self, gjeld_kreditt_kort_field):
        """Sets the gjeld_kreditt_kort_field of this GjeldEgenkapitalKonsern.


        :param gjeld_kreditt_kort_field: The gjeld_kreditt_kort_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._gjeld_kreditt_kort_field = gjeld_kreditt_kort_field

    @property
    def kassakreditt_field(self):
        """Gets the kassakreditt_field of this GjeldEgenkapitalKonsern.  


        :return: The kassakreditt_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._kassakreditt_field

    @kassakreditt_field.setter
    def kassakreditt_field(self, kassakreditt_field):
        """Sets the kassakreditt_field of this GjeldEgenkapitalKonsern.


        :param kassakreditt_field: The kassakreditt_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._kassakreditt_field = kassakreditt_field

    @property
    def leverandor_gjeld_field(self):
        """Gets the leverandor_gjeld_field of this GjeldEgenkapitalKonsern.  


        :return: The leverandor_gjeld_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._leverandor_gjeld_field

    @leverandor_gjeld_field.setter
    def leverandor_gjeld_field(self, leverandor_gjeld_field):
        """Sets the leverandor_gjeld_field of this GjeldEgenkapitalKonsern.


        :param leverandor_gjeld_field: The leverandor_gjeld_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._leverandor_gjeld_field = leverandor_gjeld_field

    @property
    def betalbar_skatt_field(self):
        """Gets the betalbar_skatt_field of this GjeldEgenkapitalKonsern.  


        :return: The betalbar_skatt_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._betalbar_skatt_field

    @betalbar_skatt_field.setter
    def betalbar_skatt_field(self, betalbar_skatt_field):
        """Sets the betalbar_skatt_field of this GjeldEgenkapitalKonsern.


        :param betalbar_skatt_field: The betalbar_skatt_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._betalbar_skatt_field = betalbar_skatt_field

    @property
    def skyld_offentlig_avgift_field(self):
        """Gets the skyld_offentlig_avgift_field of this GjeldEgenkapitalKonsern.  


        :return: The skyld_offentlig_avgift_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._skyld_offentlig_avgift_field

    @skyld_offentlig_avgift_field.setter
    def skyld_offentlig_avgift_field(self, skyld_offentlig_avgift_field):
        """Sets the skyld_offentlig_avgift_field of this GjeldEgenkapitalKonsern.


        :param skyld_offentlig_avgift_field: The skyld_offentlig_avgift_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._skyld_offentlig_avgift_field = skyld_offentlig_avgift_field

    @property
    def gjeld_konsern_kort_field(self):
        """Gets the gjeld_konsern_kort_field of this GjeldEgenkapitalKonsern.  


        :return: The gjeld_konsern_kort_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._gjeld_konsern_kort_field

    @gjeld_konsern_kort_field.setter
    def gjeld_konsern_kort_field(self, gjeld_konsern_kort_field):
        """Sets the gjeld_konsern_kort_field of this GjeldEgenkapitalKonsern.


        :param gjeld_konsern_kort_field: The gjeld_konsern_kort_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._gjeld_konsern_kort_field = gjeld_konsern_kort_field

    @property
    def utbytte_field(self):
        """Gets the utbytte_field of this GjeldEgenkapitalKonsern.  


        :return: The utbytte_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._utbytte_field

    @utbytte_field.setter
    def utbytte_field(self, utbytte_field):
        """Sets the utbytte_field of this GjeldEgenkapitalKonsern.


        :param utbytte_field: The utbytte_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._utbytte_field = utbytte_field

    @property
    def annen_kortsiktig_gjeld_field(self):
        """Gets the annen_kortsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  


        :return: The annen_kortsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._annen_kortsiktig_gjeld_field

    @annen_kortsiktig_gjeld_field.setter
    def annen_kortsiktig_gjeld_field(self, annen_kortsiktig_gjeld_field):
        """Sets the annen_kortsiktig_gjeld_field of this GjeldEgenkapitalKonsern.


        :param annen_kortsiktig_gjeld_field: The annen_kortsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._annen_kortsiktig_gjeld_field = annen_kortsiktig_gjeld_field

    @property
    def sum_gjeld_egenkapital_field(self):
        """Gets the sum_gjeld_egenkapital_field of this GjeldEgenkapitalKonsern.  


        :return: The sum_gjeld_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._sum_gjeld_egenkapital_field

    @sum_gjeld_egenkapital_field.setter
    def sum_gjeld_egenkapital_field(self, sum_gjeld_egenkapital_field):
        """Sets the sum_gjeld_egenkapital_field of this GjeldEgenkapitalKonsern.


        :param sum_gjeld_egenkapital_field: The sum_gjeld_egenkapital_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._sum_gjeld_egenkapital_field = sum_gjeld_egenkapital_field

    @property
    def kassekredittlimit_field(self):
        """Gets the kassekredittlimit_field of this GjeldEgenkapitalKonsern.  


        :return: The kassekredittlimit_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._kassekredittlimit_field

    @kassekredittlimit_field.setter
    def kassekredittlimit_field(self, kassekredittlimit_field):
        """Sets the kassekredittlimit_field of this GjeldEgenkapitalKonsern.


        :param kassekredittlimit_field: The kassekredittlimit_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._kassekredittlimit_field = kassekredittlimit_field

    @property
    def skyld_konsernbidrag_field(self):
        """Gets the skyld_konsernbidrag_field of this GjeldEgenkapitalKonsern.  


        :return: The skyld_konsernbidrag_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._skyld_konsernbidrag_field

    @skyld_konsernbidrag_field.setter
    def skyld_konsernbidrag_field(self, skyld_konsernbidrag_field):
        """Sets the skyld_konsernbidrag_field of this GjeldEgenkapitalKonsern.


        :param skyld_konsernbidrag_field: The skyld_konsernbidrag_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._skyld_konsernbidrag_field = skyld_konsernbidrag_field

    @property
    def avdrag_langsiktig_gjeld_field(self):
        """Gets the avdrag_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  


        :return: The avdrag_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :rtype: int
        """
        return self._avdrag_langsiktig_gjeld_field

    @avdrag_langsiktig_gjeld_field.setter
    def avdrag_langsiktig_gjeld_field(self, avdrag_langsiktig_gjeld_field):
        """Sets the avdrag_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.


        :param avdrag_langsiktig_gjeld_field: The avdrag_langsiktig_gjeld_field of this GjeldEgenkapitalKonsern.  
        :type: int
        """

        self._avdrag_langsiktig_gjeld_field = avdrag_langsiktig_gjeld_field

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GjeldEgenkapitalKonsern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
