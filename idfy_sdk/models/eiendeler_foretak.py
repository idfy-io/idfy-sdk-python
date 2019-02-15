# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class EiendelerForetak(object):

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
        'sum_anleggsmidler_field': 'int',
        'sum_immatrielle_eiendeler_field': 'int',
        'forskning_utvikling_field': 'int',
        'konsesjoner_field': 'int',
        'utsatt_skattefordel_field': 'int',
        'goodwill_field': 'int',
        'sum_varige_driftsmidler_field': 'int',
        'fast_eiendom_field': 'int',
        'maskiner_anlegg_field': 'int',
        'skip_rigg_fly_field': 'int',
        'drifts_losore_field': 'int',
        'sum_finansielle_anleggsmilder_field': 'int',
        'invest_datter_field': 'int',
        'invest_annet_konsern_field': 'int',
        'konsernfordring_field': 'int',
        'invest_tilknyttet_field': 'int',
        'lan_tilknyttet_field': 'int',
        'invest_aksjer_field': 'int',
        'obligasjoner_field': 'int',
        'pensjonsmidler_field': 'int',
        'andre_anleggsmidler_field': 'int',
        'sum_omlopsmidler_field': 'int',
        'sum_varer_field': 'int',
        'lager_ravarer_field': 'int',
        'lager_uferdige_varer_field': 'int',
        'lager_ferdige_varer_field': 'int',
        'sum_fordringer_field': 'int',
        'fordringer_kunder_field': 'int',
        'fordringer_andre_field': 'int',
        'fordringer_konsern_field': 'int',
        'krav_innbet_selskapskapital_field': 'int',
        'sum_investeringer_field': 'int',
        'aksjer_konsern_field': 'int',
        'aksjer_marked_field': 'int',
        'obligasjoner_marked_field': 'int',
        'andre_marked_fin_inv_field': 'int',
        'andre_fin_inst_field': 'int',
        'bankinnskudd_field': 'int',
        'andre_omlopsmidler_field': 'int',
        'sum_eiendeler_field': 'int',
        'pantstillelser_field': 'int'
    }

    attribute_map = {
        'regnskaps_av_ar_field': 'regnskapsAvArField',
        'regnskaps_av_mnd_field': 'regnskapsAvMndField',
        'sum_anleggsmidler_field': 'sumAnleggsmidlerField',
        'sum_immatrielle_eiendeler_field': 'sumImmatrielleEiendelerField',
        'forskning_utvikling_field': 'forskningUtviklingField',
        'konsesjoner_field': 'konsesjonerField',
        'utsatt_skattefordel_field': 'utsattSkattefordelField',
        'goodwill_field': 'goodwillField',
        'sum_varige_driftsmidler_field': 'sumVarigeDriftsmidlerField',
        'fast_eiendom_field': 'fastEiendomField',
        'maskiner_anlegg_field': 'maskinerAnleggField',
        'skip_rigg_fly_field': 'skipRiggFlyField',
        'drifts_losore_field': 'driftsLosoreField',
        'sum_finansielle_anleggsmilder_field': 'sumFinansielleAnleggsmilderField',
        'invest_datter_field': 'investDatterField',
        'invest_annet_konsern_field': 'investAnnetKonsernField',
        'konsernfordring_field': 'konsernfordringField',
        'invest_tilknyttet_field': 'investTilknyttetField',
        'lan_tilknyttet_field': 'lanTilknyttetField',
        'invest_aksjer_field': 'investAksjerField',
        'obligasjoner_field': 'obligasjonerField',
        'pensjonsmidler_field': 'pensjonsmidlerField',
        'andre_anleggsmidler_field': 'andreAnleggsmidlerField',
        'sum_omlopsmidler_field': 'sumOmlopsmidlerField',
        'sum_varer_field': 'sumVarerField',
        'lager_ravarer_field': 'lagerRavarerField',
        'lager_uferdige_varer_field': 'lagerUferdigeVarerField',
        'lager_ferdige_varer_field': 'lagerFerdigeVarerField',
        'sum_fordringer_field': 'sumFordringerField',
        'fordringer_kunder_field': 'fordringerKunderField',
        'fordringer_andre_field': 'fordringerAndreField',
        'fordringer_konsern_field': 'fordringerKonsernField',
        'krav_innbet_selskapskapital_field': 'kravInnbetSelskapskapitalField',
        'sum_investeringer_field': 'sumInvesteringerField',
        'aksjer_konsern_field': 'aksjerKonsernField',
        'aksjer_marked_field': 'aksjerMarkedField',
        'obligasjoner_marked_field': 'obligasjonerMarkedField',
        'andre_marked_fin_inv_field': 'andreMarkedFinInvField',
        'andre_fin_inst_field': 'andreFinInstField',
        'bankinnskudd_field': 'bankinnskuddField',
        'andre_omlopsmidler_field': 'andreOmlopsmidlerField',
        'sum_eiendeler_field': 'sumEiendelerField',
        'pantstillelser_field': 'pantstillelserField'
    }

    def __init__(self, regnskaps_av_ar_field=None, regnskaps_av_mnd_field=None, sum_anleggsmidler_field=None, sum_immatrielle_eiendeler_field=None, forskning_utvikling_field=None, konsesjoner_field=None, utsatt_skattefordel_field=None, goodwill_field=None, sum_varige_driftsmidler_field=None, fast_eiendom_field=None, maskiner_anlegg_field=None, skip_rigg_fly_field=None, drifts_losore_field=None, sum_finansielle_anleggsmilder_field=None, invest_datter_field=None, invest_annet_konsern_field=None, konsernfordring_field=None, invest_tilknyttet_field=None, lan_tilknyttet_field=None, invest_aksjer_field=None, obligasjoner_field=None, pensjonsmidler_field=None, andre_anleggsmidler_field=None, sum_omlopsmidler_field=None, sum_varer_field=None, lager_ravarer_field=None, lager_uferdige_varer_field=None, lager_ferdige_varer_field=None, sum_fordringer_field=None, fordringer_kunder_field=None, fordringer_andre_field=None, fordringer_konsern_field=None, krav_innbet_selskapskapital_field=None, sum_investeringer_field=None, aksjer_konsern_field=None, aksjer_marked_field=None, obligasjoner_marked_field=None, andre_marked_fin_inv_field=None, andre_fin_inst_field=None, bankinnskudd_field=None, andre_omlopsmidler_field=None, sum_eiendeler_field=None, pantstillelser_field=None):  
        """EiendelerForetak"""  

        self._regnskaps_av_ar_field = None
        self._regnskaps_av_mnd_field = None
        self._sum_anleggsmidler_field = None
        self._sum_immatrielle_eiendeler_field = None
        self._forskning_utvikling_field = None
        self._konsesjoner_field = None
        self._utsatt_skattefordel_field = None
        self._goodwill_field = None
        self._sum_varige_driftsmidler_field = None
        self._fast_eiendom_field = None
        self._maskiner_anlegg_field = None
        self._skip_rigg_fly_field = None
        self._drifts_losore_field = None
        self._sum_finansielle_anleggsmilder_field = None
        self._invest_datter_field = None
        self._invest_annet_konsern_field = None
        self._konsernfordring_field = None
        self._invest_tilknyttet_field = None
        self._lan_tilknyttet_field = None
        self._invest_aksjer_field = None
        self._obligasjoner_field = None
        self._pensjonsmidler_field = None
        self._andre_anleggsmidler_field = None
        self._sum_omlopsmidler_field = None
        self._sum_varer_field = None
        self._lager_ravarer_field = None
        self._lager_uferdige_varer_field = None
        self._lager_ferdige_varer_field = None
        self._sum_fordringer_field = None
        self._fordringer_kunder_field = None
        self._fordringer_andre_field = None
        self._fordringer_konsern_field = None
        self._krav_innbet_selskapskapital_field = None
        self._sum_investeringer_field = None
        self._aksjer_konsern_field = None
        self._aksjer_marked_field = None
        self._obligasjoner_marked_field = None
        self._andre_marked_fin_inv_field = None
        self._andre_fin_inst_field = None
        self._bankinnskudd_field = None
        self._andre_omlopsmidler_field = None
        self._sum_eiendeler_field = None
        self._pantstillelser_field = None
        self.discriminator = None

        if regnskaps_av_ar_field is not None:
            self.regnskaps_av_ar_field = regnskaps_av_ar_field
        if regnskaps_av_mnd_field is not None:
            self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        if sum_anleggsmidler_field is not None:
            self.sum_anleggsmidler_field = sum_anleggsmidler_field
        if sum_immatrielle_eiendeler_field is not None:
            self.sum_immatrielle_eiendeler_field = sum_immatrielle_eiendeler_field
        if forskning_utvikling_field is not None:
            self.forskning_utvikling_field = forskning_utvikling_field
        if konsesjoner_field is not None:
            self.konsesjoner_field = konsesjoner_field
        if utsatt_skattefordel_field is not None:
            self.utsatt_skattefordel_field = utsatt_skattefordel_field
        if goodwill_field is not None:
            self.goodwill_field = goodwill_field
        if sum_varige_driftsmidler_field is not None:
            self.sum_varige_driftsmidler_field = sum_varige_driftsmidler_field
        if fast_eiendom_field is not None:
            self.fast_eiendom_field = fast_eiendom_field
        if maskiner_anlegg_field is not None:
            self.maskiner_anlegg_field = maskiner_anlegg_field
        if skip_rigg_fly_field is not None:
            self.skip_rigg_fly_field = skip_rigg_fly_field
        if drifts_losore_field is not None:
            self.drifts_losore_field = drifts_losore_field
        if sum_finansielle_anleggsmilder_field is not None:
            self.sum_finansielle_anleggsmilder_field = sum_finansielle_anleggsmilder_field
        if invest_datter_field is not None:
            self.invest_datter_field = invest_datter_field
        if invest_annet_konsern_field is not None:
            self.invest_annet_konsern_field = invest_annet_konsern_field
        if konsernfordring_field is not None:
            self.konsernfordring_field = konsernfordring_field
        if invest_tilknyttet_field is not None:
            self.invest_tilknyttet_field = invest_tilknyttet_field
        if lan_tilknyttet_field is not None:
            self.lan_tilknyttet_field = lan_tilknyttet_field
        if invest_aksjer_field is not None:
            self.invest_aksjer_field = invest_aksjer_field
        if obligasjoner_field is not None:
            self.obligasjoner_field = obligasjoner_field
        if pensjonsmidler_field is not None:
            self.pensjonsmidler_field = pensjonsmidler_field
        if andre_anleggsmidler_field is not None:
            self.andre_anleggsmidler_field = andre_anleggsmidler_field
        if sum_omlopsmidler_field is not None:
            self.sum_omlopsmidler_field = sum_omlopsmidler_field
        if sum_varer_field is not None:
            self.sum_varer_field = sum_varer_field
        if lager_ravarer_field is not None:
            self.lager_ravarer_field = lager_ravarer_field
        if lager_uferdige_varer_field is not None:
            self.lager_uferdige_varer_field = lager_uferdige_varer_field
        if lager_ferdige_varer_field is not None:
            self.lager_ferdige_varer_field = lager_ferdige_varer_field
        if sum_fordringer_field is not None:
            self.sum_fordringer_field = sum_fordringer_field
        if fordringer_kunder_field is not None:
            self.fordringer_kunder_field = fordringer_kunder_field
        if fordringer_andre_field is not None:
            self.fordringer_andre_field = fordringer_andre_field
        if fordringer_konsern_field is not None:
            self.fordringer_konsern_field = fordringer_konsern_field
        if krav_innbet_selskapskapital_field is not None:
            self.krav_innbet_selskapskapital_field = krav_innbet_selskapskapital_field
        if sum_investeringer_field is not None:
            self.sum_investeringer_field = sum_investeringer_field
        if aksjer_konsern_field is not None:
            self.aksjer_konsern_field = aksjer_konsern_field
        if aksjer_marked_field is not None:
            self.aksjer_marked_field = aksjer_marked_field
        if obligasjoner_marked_field is not None:
            self.obligasjoner_marked_field = obligasjoner_marked_field
        if andre_marked_fin_inv_field is not None:
            self.andre_marked_fin_inv_field = andre_marked_fin_inv_field
        if andre_fin_inst_field is not None:
            self.andre_fin_inst_field = andre_fin_inst_field
        if bankinnskudd_field is not None:
            self.bankinnskudd_field = bankinnskudd_field
        if andre_omlopsmidler_field is not None:
            self.andre_omlopsmidler_field = andre_omlopsmidler_field
        if sum_eiendeler_field is not None:
            self.sum_eiendeler_field = sum_eiendeler_field
        if pantstillelser_field is not None:
            self.pantstillelser_field = pantstillelser_field

    @property
    def regnskaps_av_ar_field(self):
        """Gets the regnskaps_av_ar_field of this EiendelerForetak.  


        :return: The regnskaps_av_ar_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._regnskaps_av_ar_field

    @regnskaps_av_ar_field.setter
    def regnskaps_av_ar_field(self, regnskaps_av_ar_field):
        """Sets the regnskaps_av_ar_field of this EiendelerForetak.


        :param regnskaps_av_ar_field: The regnskaps_av_ar_field of this EiendelerForetak.  
        :type: int
        """

        self._regnskaps_av_ar_field = regnskaps_av_ar_field

    @property
    def regnskaps_av_mnd_field(self):
        """Gets the regnskaps_av_mnd_field of this EiendelerForetak.  


        :return: The regnskaps_av_mnd_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._regnskaps_av_mnd_field

    @regnskaps_av_mnd_field.setter
    def regnskaps_av_mnd_field(self, regnskaps_av_mnd_field):
        """Sets the regnskaps_av_mnd_field of this EiendelerForetak.


        :param regnskaps_av_mnd_field: The regnskaps_av_mnd_field of this EiendelerForetak.  
        :type: int
        """

        self._regnskaps_av_mnd_field = regnskaps_av_mnd_field

    @property
    def sum_anleggsmidler_field(self):
        """Gets the sum_anleggsmidler_field of this EiendelerForetak.  


        :return: The sum_anleggsmidler_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_anleggsmidler_field

    @sum_anleggsmidler_field.setter
    def sum_anleggsmidler_field(self, sum_anleggsmidler_field):
        """Sets the sum_anleggsmidler_field of this EiendelerForetak.


        :param sum_anleggsmidler_field: The sum_anleggsmidler_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_anleggsmidler_field = sum_anleggsmidler_field

    @property
    def sum_immatrielle_eiendeler_field(self):
        """Gets the sum_immatrielle_eiendeler_field of this EiendelerForetak.  


        :return: The sum_immatrielle_eiendeler_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_immatrielle_eiendeler_field

    @sum_immatrielle_eiendeler_field.setter
    def sum_immatrielle_eiendeler_field(self, sum_immatrielle_eiendeler_field):
        """Sets the sum_immatrielle_eiendeler_field of this EiendelerForetak.


        :param sum_immatrielle_eiendeler_field: The sum_immatrielle_eiendeler_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_immatrielle_eiendeler_field = sum_immatrielle_eiendeler_field

    @property
    def forskning_utvikling_field(self):
        """Gets the forskning_utvikling_field of this EiendelerForetak.  


        :return: The forskning_utvikling_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._forskning_utvikling_field

    @forskning_utvikling_field.setter
    def forskning_utvikling_field(self, forskning_utvikling_field):
        """Sets the forskning_utvikling_field of this EiendelerForetak.


        :param forskning_utvikling_field: The forskning_utvikling_field of this EiendelerForetak.  
        :type: int
        """

        self._forskning_utvikling_field = forskning_utvikling_field

    @property
    def konsesjoner_field(self):
        """Gets the konsesjoner_field of this EiendelerForetak.  


        :return: The konsesjoner_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._konsesjoner_field

    @konsesjoner_field.setter
    def konsesjoner_field(self, konsesjoner_field):
        """Sets the konsesjoner_field of this EiendelerForetak.


        :param konsesjoner_field: The konsesjoner_field of this EiendelerForetak.  
        :type: int
        """

        self._konsesjoner_field = konsesjoner_field

    @property
    def utsatt_skattefordel_field(self):
        """Gets the utsatt_skattefordel_field of this EiendelerForetak.  


        :return: The utsatt_skattefordel_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._utsatt_skattefordel_field

    @utsatt_skattefordel_field.setter
    def utsatt_skattefordel_field(self, utsatt_skattefordel_field):
        """Sets the utsatt_skattefordel_field of this EiendelerForetak.


        :param utsatt_skattefordel_field: The utsatt_skattefordel_field of this EiendelerForetak.  
        :type: int
        """

        self._utsatt_skattefordel_field = utsatt_skattefordel_field

    @property
    def goodwill_field(self):
        """Gets the goodwill_field of this EiendelerForetak.  


        :return: The goodwill_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._goodwill_field

    @goodwill_field.setter
    def goodwill_field(self, goodwill_field):
        """Sets the goodwill_field of this EiendelerForetak.


        :param goodwill_field: The goodwill_field of this EiendelerForetak.  
        :type: int
        """

        self._goodwill_field = goodwill_field

    @property
    def sum_varige_driftsmidler_field(self):
        """Gets the sum_varige_driftsmidler_field of this EiendelerForetak.  


        :return: The sum_varige_driftsmidler_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_varige_driftsmidler_field

    @sum_varige_driftsmidler_field.setter
    def sum_varige_driftsmidler_field(self, sum_varige_driftsmidler_field):
        """Sets the sum_varige_driftsmidler_field of this EiendelerForetak.


        :param sum_varige_driftsmidler_field: The sum_varige_driftsmidler_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_varige_driftsmidler_field = sum_varige_driftsmidler_field

    @property
    def fast_eiendom_field(self):
        """Gets the fast_eiendom_field of this EiendelerForetak.  


        :return: The fast_eiendom_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._fast_eiendom_field

    @fast_eiendom_field.setter
    def fast_eiendom_field(self, fast_eiendom_field):
        """Sets the fast_eiendom_field of this EiendelerForetak.


        :param fast_eiendom_field: The fast_eiendom_field of this EiendelerForetak.  
        :type: int
        """

        self._fast_eiendom_field = fast_eiendom_field

    @property
    def maskiner_anlegg_field(self):
        """Gets the maskiner_anlegg_field of this EiendelerForetak.  


        :return: The maskiner_anlegg_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._maskiner_anlegg_field

    @maskiner_anlegg_field.setter
    def maskiner_anlegg_field(self, maskiner_anlegg_field):
        """Sets the maskiner_anlegg_field of this EiendelerForetak.


        :param maskiner_anlegg_field: The maskiner_anlegg_field of this EiendelerForetak.  
        :type: int
        """

        self._maskiner_anlegg_field = maskiner_anlegg_field

    @property
    def skip_rigg_fly_field(self):
        """Gets the skip_rigg_fly_field of this EiendelerForetak.  


        :return: The skip_rigg_fly_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._skip_rigg_fly_field

    @skip_rigg_fly_field.setter
    def skip_rigg_fly_field(self, skip_rigg_fly_field):
        """Sets the skip_rigg_fly_field of this EiendelerForetak.


        :param skip_rigg_fly_field: The skip_rigg_fly_field of this EiendelerForetak.  
        :type: int
        """

        self._skip_rigg_fly_field = skip_rigg_fly_field

    @property
    def drifts_losore_field(self):
        """Gets the drifts_losore_field of this EiendelerForetak.  


        :return: The drifts_losore_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._drifts_losore_field

    @drifts_losore_field.setter
    def drifts_losore_field(self, drifts_losore_field):
        """Sets the drifts_losore_field of this EiendelerForetak.


        :param drifts_losore_field: The drifts_losore_field of this EiendelerForetak.  
        :type: int
        """

        self._drifts_losore_field = drifts_losore_field

    @property
    def sum_finansielle_anleggsmilder_field(self):
        """Gets the sum_finansielle_anleggsmilder_field of this EiendelerForetak.  


        :return: The sum_finansielle_anleggsmilder_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_finansielle_anleggsmilder_field

    @sum_finansielle_anleggsmilder_field.setter
    def sum_finansielle_anleggsmilder_field(self, sum_finansielle_anleggsmilder_field):
        """Sets the sum_finansielle_anleggsmilder_field of this EiendelerForetak.


        :param sum_finansielle_anleggsmilder_field: The sum_finansielle_anleggsmilder_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_finansielle_anleggsmilder_field = sum_finansielle_anleggsmilder_field

    @property
    def invest_datter_field(self):
        """Gets the invest_datter_field of this EiendelerForetak.  


        :return: The invest_datter_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._invest_datter_field

    @invest_datter_field.setter
    def invest_datter_field(self, invest_datter_field):
        """Sets the invest_datter_field of this EiendelerForetak.


        :param invest_datter_field: The invest_datter_field of this EiendelerForetak.  
        :type: int
        """

        self._invest_datter_field = invest_datter_field

    @property
    def invest_annet_konsern_field(self):
        """Gets the invest_annet_konsern_field of this EiendelerForetak.  


        :return: The invest_annet_konsern_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._invest_annet_konsern_field

    @invest_annet_konsern_field.setter
    def invest_annet_konsern_field(self, invest_annet_konsern_field):
        """Sets the invest_annet_konsern_field of this EiendelerForetak.


        :param invest_annet_konsern_field: The invest_annet_konsern_field of this EiendelerForetak.  
        :type: int
        """

        self._invest_annet_konsern_field = invest_annet_konsern_field

    @property
    def konsernfordring_field(self):
        """Gets the konsernfordring_field of this EiendelerForetak.  


        :return: The konsernfordring_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._konsernfordring_field

    @konsernfordring_field.setter
    def konsernfordring_field(self, konsernfordring_field):
        """Sets the konsernfordring_field of this EiendelerForetak.


        :param konsernfordring_field: The konsernfordring_field of this EiendelerForetak.  
        :type: int
        """

        self._konsernfordring_field = konsernfordring_field

    @property
    def invest_tilknyttet_field(self):
        """Gets the invest_tilknyttet_field of this EiendelerForetak.  


        :return: The invest_tilknyttet_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._invest_tilknyttet_field

    @invest_tilknyttet_field.setter
    def invest_tilknyttet_field(self, invest_tilknyttet_field):
        """Sets the invest_tilknyttet_field of this EiendelerForetak.


        :param invest_tilknyttet_field: The invest_tilknyttet_field of this EiendelerForetak.  
        :type: int
        """

        self._invest_tilknyttet_field = invest_tilknyttet_field

    @property
    def lan_tilknyttet_field(self):
        """Gets the lan_tilknyttet_field of this EiendelerForetak.  


        :return: The lan_tilknyttet_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._lan_tilknyttet_field

    @lan_tilknyttet_field.setter
    def lan_tilknyttet_field(self, lan_tilknyttet_field):
        """Sets the lan_tilknyttet_field of this EiendelerForetak.


        :param lan_tilknyttet_field: The lan_tilknyttet_field of this EiendelerForetak.  
        :type: int
        """

        self._lan_tilknyttet_field = lan_tilknyttet_field

    @property
    def invest_aksjer_field(self):
        """Gets the invest_aksjer_field of this EiendelerForetak.  


        :return: The invest_aksjer_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._invest_aksjer_field

    @invest_aksjer_field.setter
    def invest_aksjer_field(self, invest_aksjer_field):
        """Sets the invest_aksjer_field of this EiendelerForetak.


        :param invest_aksjer_field: The invest_aksjer_field of this EiendelerForetak.  
        :type: int
        """

        self._invest_aksjer_field = invest_aksjer_field

    @property
    def obligasjoner_field(self):
        """Gets the obligasjoner_field of this EiendelerForetak.  


        :return: The obligasjoner_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._obligasjoner_field

    @obligasjoner_field.setter
    def obligasjoner_field(self, obligasjoner_field):
        """Sets the obligasjoner_field of this EiendelerForetak.


        :param obligasjoner_field: The obligasjoner_field of this EiendelerForetak.  
        :type: int
        """

        self._obligasjoner_field = obligasjoner_field

    @property
    def pensjonsmidler_field(self):
        """Gets the pensjonsmidler_field of this EiendelerForetak.  


        :return: The pensjonsmidler_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._pensjonsmidler_field

    @pensjonsmidler_field.setter
    def pensjonsmidler_field(self, pensjonsmidler_field):
        """Sets the pensjonsmidler_field of this EiendelerForetak.


        :param pensjonsmidler_field: The pensjonsmidler_field of this EiendelerForetak.  
        :type: int
        """

        self._pensjonsmidler_field = pensjonsmidler_field

    @property
    def andre_anleggsmidler_field(self):
        """Gets the andre_anleggsmidler_field of this EiendelerForetak.  


        :return: The andre_anleggsmidler_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._andre_anleggsmidler_field

    @andre_anleggsmidler_field.setter
    def andre_anleggsmidler_field(self, andre_anleggsmidler_field):
        """Sets the andre_anleggsmidler_field of this EiendelerForetak.


        :param andre_anleggsmidler_field: The andre_anleggsmidler_field of this EiendelerForetak.  
        :type: int
        """

        self._andre_anleggsmidler_field = andre_anleggsmidler_field

    @property
    def sum_omlopsmidler_field(self):
        """Gets the sum_omlopsmidler_field of this EiendelerForetak.  


        :return: The sum_omlopsmidler_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_omlopsmidler_field

    @sum_omlopsmidler_field.setter
    def sum_omlopsmidler_field(self, sum_omlopsmidler_field):
        """Sets the sum_omlopsmidler_field of this EiendelerForetak.


        :param sum_omlopsmidler_field: The sum_omlopsmidler_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_omlopsmidler_field = sum_omlopsmidler_field

    @property
    def sum_varer_field(self):
        """Gets the sum_varer_field of this EiendelerForetak.  


        :return: The sum_varer_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_varer_field

    @sum_varer_field.setter
    def sum_varer_field(self, sum_varer_field):
        """Sets the sum_varer_field of this EiendelerForetak.


        :param sum_varer_field: The sum_varer_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_varer_field = sum_varer_field

    @property
    def lager_ravarer_field(self):
        """Gets the lager_ravarer_field of this EiendelerForetak.  


        :return: The lager_ravarer_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._lager_ravarer_field

    @lager_ravarer_field.setter
    def lager_ravarer_field(self, lager_ravarer_field):
        """Sets the lager_ravarer_field of this EiendelerForetak.


        :param lager_ravarer_field: The lager_ravarer_field of this EiendelerForetak.  
        :type: int
        """

        self._lager_ravarer_field = lager_ravarer_field

    @property
    def lager_uferdige_varer_field(self):
        """Gets the lager_uferdige_varer_field of this EiendelerForetak.  


        :return: The lager_uferdige_varer_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._lager_uferdige_varer_field

    @lager_uferdige_varer_field.setter
    def lager_uferdige_varer_field(self, lager_uferdige_varer_field):
        """Sets the lager_uferdige_varer_field of this EiendelerForetak.


        :param lager_uferdige_varer_field: The lager_uferdige_varer_field of this EiendelerForetak.  
        :type: int
        """

        self._lager_uferdige_varer_field = lager_uferdige_varer_field

    @property
    def lager_ferdige_varer_field(self):
        """Gets the lager_ferdige_varer_field of this EiendelerForetak.  


        :return: The lager_ferdige_varer_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._lager_ferdige_varer_field

    @lager_ferdige_varer_field.setter
    def lager_ferdige_varer_field(self, lager_ferdige_varer_field):
        """Sets the lager_ferdige_varer_field of this EiendelerForetak.


        :param lager_ferdige_varer_field: The lager_ferdige_varer_field of this EiendelerForetak.  
        :type: int
        """

        self._lager_ferdige_varer_field = lager_ferdige_varer_field

    @property
    def sum_fordringer_field(self):
        """Gets the sum_fordringer_field of this EiendelerForetak.  


        :return: The sum_fordringer_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_fordringer_field

    @sum_fordringer_field.setter
    def sum_fordringer_field(self, sum_fordringer_field):
        """Sets the sum_fordringer_field of this EiendelerForetak.


        :param sum_fordringer_field: The sum_fordringer_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_fordringer_field = sum_fordringer_field

    @property
    def fordringer_kunder_field(self):
        """Gets the fordringer_kunder_field of this EiendelerForetak.  


        :return: The fordringer_kunder_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._fordringer_kunder_field

    @fordringer_kunder_field.setter
    def fordringer_kunder_field(self, fordringer_kunder_field):
        """Sets the fordringer_kunder_field of this EiendelerForetak.


        :param fordringer_kunder_field: The fordringer_kunder_field of this EiendelerForetak.  
        :type: int
        """

        self._fordringer_kunder_field = fordringer_kunder_field

    @property
    def fordringer_andre_field(self):
        """Gets the fordringer_andre_field of this EiendelerForetak.  


        :return: The fordringer_andre_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._fordringer_andre_field

    @fordringer_andre_field.setter
    def fordringer_andre_field(self, fordringer_andre_field):
        """Sets the fordringer_andre_field of this EiendelerForetak.


        :param fordringer_andre_field: The fordringer_andre_field of this EiendelerForetak.  
        :type: int
        """

        self._fordringer_andre_field = fordringer_andre_field

    @property
    def fordringer_konsern_field(self):
        """Gets the fordringer_konsern_field of this EiendelerForetak.  


        :return: The fordringer_konsern_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._fordringer_konsern_field

    @fordringer_konsern_field.setter
    def fordringer_konsern_field(self, fordringer_konsern_field):
        """Sets the fordringer_konsern_field of this EiendelerForetak.


        :param fordringer_konsern_field: The fordringer_konsern_field of this EiendelerForetak.  
        :type: int
        """

        self._fordringer_konsern_field = fordringer_konsern_field

    @property
    def krav_innbet_selskapskapital_field(self):
        """Gets the krav_innbet_selskapskapital_field of this EiendelerForetak.  


        :return: The krav_innbet_selskapskapital_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._krav_innbet_selskapskapital_field

    @krav_innbet_selskapskapital_field.setter
    def krav_innbet_selskapskapital_field(self, krav_innbet_selskapskapital_field):
        """Sets the krav_innbet_selskapskapital_field of this EiendelerForetak.


        :param krav_innbet_selskapskapital_field: The krav_innbet_selskapskapital_field of this EiendelerForetak.  
        :type: int
        """

        self._krav_innbet_selskapskapital_field = krav_innbet_selskapskapital_field

    @property
    def sum_investeringer_field(self):
        """Gets the sum_investeringer_field of this EiendelerForetak.  


        :return: The sum_investeringer_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_investeringer_field

    @sum_investeringer_field.setter
    def sum_investeringer_field(self, sum_investeringer_field):
        """Sets the sum_investeringer_field of this EiendelerForetak.


        :param sum_investeringer_field: The sum_investeringer_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_investeringer_field = sum_investeringer_field

    @property
    def aksjer_konsern_field(self):
        """Gets the aksjer_konsern_field of this EiendelerForetak.  


        :return: The aksjer_konsern_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._aksjer_konsern_field

    @aksjer_konsern_field.setter
    def aksjer_konsern_field(self, aksjer_konsern_field):
        """Sets the aksjer_konsern_field of this EiendelerForetak.


        :param aksjer_konsern_field: The aksjer_konsern_field of this EiendelerForetak.  
        :type: int
        """

        self._aksjer_konsern_field = aksjer_konsern_field

    @property
    def aksjer_marked_field(self):
        """Gets the aksjer_marked_field of this EiendelerForetak.  


        :return: The aksjer_marked_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._aksjer_marked_field

    @aksjer_marked_field.setter
    def aksjer_marked_field(self, aksjer_marked_field):
        """Sets the aksjer_marked_field of this EiendelerForetak.


        :param aksjer_marked_field: The aksjer_marked_field of this EiendelerForetak.  
        :type: int
        """

        self._aksjer_marked_field = aksjer_marked_field

    @property
    def obligasjoner_marked_field(self):
        """Gets the obligasjoner_marked_field of this EiendelerForetak.  


        :return: The obligasjoner_marked_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._obligasjoner_marked_field

    @obligasjoner_marked_field.setter
    def obligasjoner_marked_field(self, obligasjoner_marked_field):
        """Sets the obligasjoner_marked_field of this EiendelerForetak.


        :param obligasjoner_marked_field: The obligasjoner_marked_field of this EiendelerForetak.  
        :type: int
        """

        self._obligasjoner_marked_field = obligasjoner_marked_field

    @property
    def andre_marked_fin_inv_field(self):
        """Gets the andre_marked_fin_inv_field of this EiendelerForetak.  


        :return: The andre_marked_fin_inv_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._andre_marked_fin_inv_field

    @andre_marked_fin_inv_field.setter
    def andre_marked_fin_inv_field(self, andre_marked_fin_inv_field):
        """Sets the andre_marked_fin_inv_field of this EiendelerForetak.


        :param andre_marked_fin_inv_field: The andre_marked_fin_inv_field of this EiendelerForetak.  
        :type: int
        """

        self._andre_marked_fin_inv_field = andre_marked_fin_inv_field

    @property
    def andre_fin_inst_field(self):
        """Gets the andre_fin_inst_field of this EiendelerForetak.  


        :return: The andre_fin_inst_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._andre_fin_inst_field

    @andre_fin_inst_field.setter
    def andre_fin_inst_field(self, andre_fin_inst_field):
        """Sets the andre_fin_inst_field of this EiendelerForetak.


        :param andre_fin_inst_field: The andre_fin_inst_field of this EiendelerForetak.  
        :type: int
        """

        self._andre_fin_inst_field = andre_fin_inst_field

    @property
    def bankinnskudd_field(self):
        """Gets the bankinnskudd_field of this EiendelerForetak.  


        :return: The bankinnskudd_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._bankinnskudd_field

    @bankinnskudd_field.setter
    def bankinnskudd_field(self, bankinnskudd_field):
        """Sets the bankinnskudd_field of this EiendelerForetak.


        :param bankinnskudd_field: The bankinnskudd_field of this EiendelerForetak.  
        :type: int
        """

        self._bankinnskudd_field = bankinnskudd_field

    @property
    def andre_omlopsmidler_field(self):
        """Gets the andre_omlopsmidler_field of this EiendelerForetak.  


        :return: The andre_omlopsmidler_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._andre_omlopsmidler_field

    @andre_omlopsmidler_field.setter
    def andre_omlopsmidler_field(self, andre_omlopsmidler_field):
        """Sets the andre_omlopsmidler_field of this EiendelerForetak.


        :param andre_omlopsmidler_field: The andre_omlopsmidler_field of this EiendelerForetak.  
        :type: int
        """

        self._andre_omlopsmidler_field = andre_omlopsmidler_field

    @property
    def sum_eiendeler_field(self):
        """Gets the sum_eiendeler_field of this EiendelerForetak.  


        :return: The sum_eiendeler_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._sum_eiendeler_field

    @sum_eiendeler_field.setter
    def sum_eiendeler_field(self, sum_eiendeler_field):
        """Sets the sum_eiendeler_field of this EiendelerForetak.


        :param sum_eiendeler_field: The sum_eiendeler_field of this EiendelerForetak.  
        :type: int
        """

        self._sum_eiendeler_field = sum_eiendeler_field

    @property
    def pantstillelser_field(self):
        """Gets the pantstillelser_field of this EiendelerForetak.  


        :return: The pantstillelser_field of this EiendelerForetak.  
        :rtype: int
        """
        return self._pantstillelser_field

    @pantstillelser_field.setter
    def pantstillelser_field(self, pantstillelser_field):
        """Sets the pantstillelser_field of this EiendelerForetak.


        :param pantstillelser_field: The pantstillelser_field of this EiendelerForetak.  
        :type: int
        """

        self._pantstillelser_field = pantstillelser_field

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
        if not isinstance(other, EiendelerForetak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
