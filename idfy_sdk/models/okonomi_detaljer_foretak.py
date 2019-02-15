# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class OkonomiDetaljerForetak(object):

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
        'totalinntekt_field': 'int',
        'salgsinntekter_field': 'int',
        'annen_driftsinntekt_field': 'int',
        'varekostnad_field': 'int',
        'beholdningsendring_field': 'int',
        'lonnskostnad_field': 'int',
        'avskrivninger_field': 'int',
        'nedskrivninger_field': 'int',
        'annen_driftskostnad_field': 'int',
        'drifts_resultat_field': 'int',
        'inntekt_inv_datter_field': 'int',
        'inntekt_inv_konsern_field': 'int',
        'inntekt_inv_annen_field': 'int',
        'renteinntekt_konsern_field': 'int',
        'renteinntekt_annen_field': 'int',
        'finansinntekt_annen_field': 'int',
        'finansinntekt_field': 'int',
        'verdiendring_mar_fin_omlopsmidler_field': 'int',
        'nedskrivning_mar_fin_omlopsmidler_field': 'int',
        'nedskrivning_fin_anleggsmidler_field': 'int',
        'rentekostnad_konsern_field': 'int',
        'annen_rentekostnad_field': 'int',
        'annen_finanskostnad_field': 'int',
        'finanskostnad_field': 'int',
        'ord_resultat_for_skatt_field': 'int',
        'skatt_ord_resultat_field': 'int',
        'ord_resultat_field': 'int',
        'ekstraord_inntekt_field': 'int',
        'ekstraord_kostnad_field': 'int',
        'skatt_ekstraord_resultat_field': 'int',
        'sum_skatt_field': 'int',
        'minoritets_interesser_field': 'int',
        'ars_resultat_field': 'int',
        'konsernbidrag_field': 'int',
        'utbytte_field': 'int',
        'til_fond_vurd_for_field': 'int',
        'til_annen_egenkapital_field': 'int',
        'tap_krav_field': 'int'
    }

    attribute_map = {
        'regnskaps_av_ar_field': 'regnskapsAvArField',
        'regnskaps_av_mnd_field': 'regnskapsAvMndField',
        'totalinntekt_field': 'totalinntektField',
        'salgsinntekter_field': 'salgsinntekterField',
        'annen_driftsinntekt_field': 'annenDriftsinntektField',
        'varekostnad_field': 'varekostnadField',
        'beholdningsendring_field': 'beholdningsendringField',
        'lonnskostnad_field': 'lonnskostnadField',
        'avskrivninger_field': 'avskrivningerField',
        'nedskrivninger_field': 'nedskrivningerField',
        'annen_driftskostnad_field': 'annenDriftskostnadField',
        'drifts_resultat_field': 'driftsResultatField',
        'inntekt_inv_datter_field': 'inntektInvDatterField',
        'inntekt_inv_konsern_field': 'inntektInvKonsernField',
        'inntekt_inv_annen_field': 'inntektInvAnnenField',
        'renteinntekt_konsern_field': 'renteinntektKonsernField',
        'renteinntekt_annen_field': 'renteinntektAnnenField',
        'finansinntekt_annen_field': 'finansinntektAnnenField',
        'finansinntekt_field': 'finansinntektField',
        'verdiendring_mar_fin_omlopsmidler_field': 'verdiendringMarFinOmlopsmidlerField',
        'nedskrivning_mar_fin_omlopsmidler_field': 'nedskrivningMarFinOmlopsmidlerField',
        'nedskrivning_fin_anleggsmidler_field': 'nedskrivningFinAnleggsmidlerField',
        'rentekostnad_konsern_field': 'rentekostnadKonsernField',
        'annen_rentekostnad_field': 'annenRentekostnadField',
        'annen_finanskostnad_field': 'annenFinanskostnadField',
        'finanskostnad_field': 'finanskostnadField',
        'ord_resultat_for_skatt_field': 'ordResultatForSkattField',
        'skatt_ord_resultat_field': 'skattOrdResultatField',
        'ord_resultat_field': 'ordResultatField',
        'ekstraord_inntekt_field': 'ekstraordInntektField',
        'ekstraord_kostnad_field': 'ekstraordKostnadField',
        'skatt_ekstraord_resultat_field': 'skattEkstraordResultatField',
        'sum_skatt_field': 'sumSkattField',
        'minoritets_interesser_field': 'minoritetsInteresserField',
        'ars_resultat_field': 'arsResultatField',
        'konsernbidrag_field': 'konsernbidragField',
        'utbytte_field': 'utbytteField',
        'til_fond_vurd_for_field': 'tilFondVurdForField',
        'til_annen_egenkapital_field': 'tilAnnenEgenkapitalField',
        'tap_krav_field': 'tapKravField'
    }

    def __init__(self, regnskaps_av_ar_field=None, regnskaps_av_mnd_field=None, totalinntekt_field=None, salgsinntekter_field=None, annen_driftsinntekt_field=None, varekostnad_field=None, beholdningsendring_field=None, lonnskostnad_field=None, avskrivninger_field=None, nedskrivninger_field=None, annen_driftskostnad_field=None, drifts_resultat_field=None, inntekt_inv_datter_field=None, inntekt_inv_konsern_field=None, inntekt_inv_annen_field=None, renteinntekt_konsern_field=None, renteinntekt_annen_field=None, finansinntekt_annen_field=None, finansinntekt_field=None, verdiendring_mar_fin_omlopsmidler_field=None, nedskrivning_mar_fin_omlopsmidler_field=None, nedskrivning_fin_anleggsmidler_field=None, rentekostnad_konsern_field=None, annen_rentekostnad_field=None, annen_finanskostnad_field=None, finanskostnad_field=None, ord_resultat_for_skatt_field=None, skatt_ord_resultat_field=None, ord_resultat_field=None, ekstraord_inntekt_field=None, ekstraord_kostnad_field=None, skatt_ekstraord_resultat_field=None, sum_skatt_field=None, minoritets_interesser_field=None, ars_resultat_field=None, konsernbidrag_field=None, utbytte_field=None, til_fond_vurd_for_field=None, til_annen_egenkapital_field=None, tap_krav_field=None):  
        """OkonomiDetaljerForetak"""  

        self._regnskaps_av_ar_field = None
        self._regnskaps_av_mnd_field = None
        self._totalinntekt_field = None
        self._salgsinntekter_field = None
        self._annen_driftsinntekt_field = None
        self._varekostnad_field = None
        self._beholdningsendring_field = None
        self._lonnskostnad_field = None
        self._avskrivninger_field = None
        self._nedskrivninger_field = None
        self._annen_driftskostnad_field = None
        self._drifts_resultat_field = None
        self._inntekt_inv_datter_field = None
        self._inntekt_inv_konsern_field = None
        self._inntekt_inv_annen_field = None
        self._renteinntekt_konsern_field = None
        self._renteinntekt_annen_field = None
        self._finansinntekt_annen_field = None
        self._finansinntekt_field = None
        self._verdiendring_mar_fin_omlopsmidler_field = None
        self._nedskrivning_mar_fin_omlopsmidler_field = None
        self._nedskrivning_fin_anleggsmidler_field = None
        self._rentekostnad_konsern_field = None
        self._annen_rentekostnad_field = None
        self._annen_finanskostnad_field = None
        self._finanskostnad_field = None
        self._ord_resultat_for_skatt_field = None
        self._skatt_ord_resultat_field = None
        self._ord_resultat_field = None
        self._ekstraord_inntekt_field = None
        self._ekstraord_kostnad_field = None
        self._skatt_ekstraord_resultat_field = None
        self._sum_skatt_field = None
        self._minoritets_interesser_field = None
        self._ars_resultat_field = None
        self._konsernbidrag_field = None
        self._utbytte_field = None
        self._til_fond_vurd_for_field = None
        self._til_annen_egenkapital_field = None
        self._tap_krav_field = None
        self.discriminator = None

        if regnskaps_av_ar_field is not None:
            self.regnskaps_av_ar_field = regnskaps_av_ar_field
        if regnskaps_av_mnd_field is not None:
            self.regnskaps_av_mnd_field = regnskaps_av_mnd_field
        if totalinntekt_field is not None:
            self.totalinntekt_field = totalinntekt_field
        if salgsinntekter_field is not None:
            self.salgsinntekter_field = salgsinntekter_field
        if annen_driftsinntekt_field is not None:
            self.annen_driftsinntekt_field = annen_driftsinntekt_field
        if varekostnad_field is not None:
            self.varekostnad_field = varekostnad_field
        if beholdningsendring_field is not None:
            self.beholdningsendring_field = beholdningsendring_field
        if lonnskostnad_field is not None:
            self.lonnskostnad_field = lonnskostnad_field
        if avskrivninger_field is not None:
            self.avskrivninger_field = avskrivninger_field
        if nedskrivninger_field is not None:
            self.nedskrivninger_field = nedskrivninger_field
        if annen_driftskostnad_field is not None:
            self.annen_driftskostnad_field = annen_driftskostnad_field
        if drifts_resultat_field is not None:
            self.drifts_resultat_field = drifts_resultat_field
        if inntekt_inv_datter_field is not None:
            self.inntekt_inv_datter_field = inntekt_inv_datter_field
        if inntekt_inv_konsern_field is not None:
            self.inntekt_inv_konsern_field = inntekt_inv_konsern_field
        if inntekt_inv_annen_field is not None:
            self.inntekt_inv_annen_field = inntekt_inv_annen_field
        if renteinntekt_konsern_field is not None:
            self.renteinntekt_konsern_field = renteinntekt_konsern_field
        if renteinntekt_annen_field is not None:
            self.renteinntekt_annen_field = renteinntekt_annen_field
        if finansinntekt_annen_field is not None:
            self.finansinntekt_annen_field = finansinntekt_annen_field
        if finansinntekt_field is not None:
            self.finansinntekt_field = finansinntekt_field
        if verdiendring_mar_fin_omlopsmidler_field is not None:
            self.verdiendring_mar_fin_omlopsmidler_field = verdiendring_mar_fin_omlopsmidler_field
        if nedskrivning_mar_fin_omlopsmidler_field is not None:
            self.nedskrivning_mar_fin_omlopsmidler_field = nedskrivning_mar_fin_omlopsmidler_field
        if nedskrivning_fin_anleggsmidler_field is not None:
            self.nedskrivning_fin_anleggsmidler_field = nedskrivning_fin_anleggsmidler_field
        if rentekostnad_konsern_field is not None:
            self.rentekostnad_konsern_field = rentekostnad_konsern_field
        if annen_rentekostnad_field is not None:
            self.annen_rentekostnad_field = annen_rentekostnad_field
        if annen_finanskostnad_field is not None:
            self.annen_finanskostnad_field = annen_finanskostnad_field
        if finanskostnad_field is not None:
            self.finanskostnad_field = finanskostnad_field
        if ord_resultat_for_skatt_field is not None:
            self.ord_resultat_for_skatt_field = ord_resultat_for_skatt_field
        if skatt_ord_resultat_field is not None:
            self.skatt_ord_resultat_field = skatt_ord_resultat_field
        if ord_resultat_field is not None:
            self.ord_resultat_field = ord_resultat_field
        if ekstraord_inntekt_field is not None:
            self.ekstraord_inntekt_field = ekstraord_inntekt_field
        if ekstraord_kostnad_field is not None:
            self.ekstraord_kostnad_field = ekstraord_kostnad_field
        if skatt_ekstraord_resultat_field is not None:
            self.skatt_ekstraord_resultat_field = skatt_ekstraord_resultat_field
        if sum_skatt_field is not None:
            self.sum_skatt_field = sum_skatt_field
        if minoritets_interesser_field is not None:
            self.minoritets_interesser_field = minoritets_interesser_field
        if ars_resultat_field is not None:
            self.ars_resultat_field = ars_resultat_field
        if konsernbidrag_field is not None:
            self.konsernbidrag_field = konsernbidrag_field
        if utbytte_field is not None:
            self.utbytte_field = utbytte_field
        if til_fond_vurd_for_field is not None:
            self.til_fond_vurd_for_field = til_fond_vurd_for_field
        if til_annen_egenkapital_field is not None:
            self.til_annen_egenkapital_field = til_annen_egenkapital_field
        if tap_krav_field is not None:
            self.tap_krav_field = tap_krav_field

    @property
    def regnskaps_av_ar_field(self):
        """Gets the regnskaps_av_ar_field of this OkonomiDetaljerForetak.  


        :return: The regnskaps_av_ar_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._regnskaps_av_ar_field

    @regnskaps_av_ar_field.setter
    def regnskaps_av_ar_field(self, regnskaps_av_ar_field):
        """Sets the regnskaps_av_ar_field of this OkonomiDetaljerForetak.


        :param regnskaps_av_ar_field: The regnskaps_av_ar_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._regnskaps_av_ar_field = regnskaps_av_ar_field

    @property
    def regnskaps_av_mnd_field(self):
        """Gets the regnskaps_av_mnd_field of this OkonomiDetaljerForetak.  


        :return: The regnskaps_av_mnd_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._regnskaps_av_mnd_field

    @regnskaps_av_mnd_field.setter
    def regnskaps_av_mnd_field(self, regnskaps_av_mnd_field):
        """Sets the regnskaps_av_mnd_field of this OkonomiDetaljerForetak.


        :param regnskaps_av_mnd_field: The regnskaps_av_mnd_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._regnskaps_av_mnd_field = regnskaps_av_mnd_field

    @property
    def totalinntekt_field(self):
        """Gets the totalinntekt_field of this OkonomiDetaljerForetak.  


        :return: The totalinntekt_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._totalinntekt_field

    @totalinntekt_field.setter
    def totalinntekt_field(self, totalinntekt_field):
        """Sets the totalinntekt_field of this OkonomiDetaljerForetak.


        :param totalinntekt_field: The totalinntekt_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._totalinntekt_field = totalinntekt_field

    @property
    def salgsinntekter_field(self):
        """Gets the salgsinntekter_field of this OkonomiDetaljerForetak.  


        :return: The salgsinntekter_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._salgsinntekter_field

    @salgsinntekter_field.setter
    def salgsinntekter_field(self, salgsinntekter_field):
        """Sets the salgsinntekter_field of this OkonomiDetaljerForetak.


        :param salgsinntekter_field: The salgsinntekter_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._salgsinntekter_field = salgsinntekter_field

    @property
    def annen_driftsinntekt_field(self):
        """Gets the annen_driftsinntekt_field of this OkonomiDetaljerForetak.  


        :return: The annen_driftsinntekt_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._annen_driftsinntekt_field

    @annen_driftsinntekt_field.setter
    def annen_driftsinntekt_field(self, annen_driftsinntekt_field):
        """Sets the annen_driftsinntekt_field of this OkonomiDetaljerForetak.


        :param annen_driftsinntekt_field: The annen_driftsinntekt_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._annen_driftsinntekt_field = annen_driftsinntekt_field

    @property
    def varekostnad_field(self):
        """Gets the varekostnad_field of this OkonomiDetaljerForetak.  


        :return: The varekostnad_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._varekostnad_field

    @varekostnad_field.setter
    def varekostnad_field(self, varekostnad_field):
        """Sets the varekostnad_field of this OkonomiDetaljerForetak.


        :param varekostnad_field: The varekostnad_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._varekostnad_field = varekostnad_field

    @property
    def beholdningsendring_field(self):
        """Gets the beholdningsendring_field of this OkonomiDetaljerForetak.  


        :return: The beholdningsendring_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._beholdningsendring_field

    @beholdningsendring_field.setter
    def beholdningsendring_field(self, beholdningsendring_field):
        """Sets the beholdningsendring_field of this OkonomiDetaljerForetak.


        :param beholdningsendring_field: The beholdningsendring_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._beholdningsendring_field = beholdningsendring_field

    @property
    def lonnskostnad_field(self):
        """Gets the lonnskostnad_field of this OkonomiDetaljerForetak.  


        :return: The lonnskostnad_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._lonnskostnad_field

    @lonnskostnad_field.setter
    def lonnskostnad_field(self, lonnskostnad_field):
        """Sets the lonnskostnad_field of this OkonomiDetaljerForetak.


        :param lonnskostnad_field: The lonnskostnad_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._lonnskostnad_field = lonnskostnad_field

    @property
    def avskrivninger_field(self):
        """Gets the avskrivninger_field of this OkonomiDetaljerForetak.  


        :return: The avskrivninger_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._avskrivninger_field

    @avskrivninger_field.setter
    def avskrivninger_field(self, avskrivninger_field):
        """Sets the avskrivninger_field of this OkonomiDetaljerForetak.


        :param avskrivninger_field: The avskrivninger_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._avskrivninger_field = avskrivninger_field

    @property
    def nedskrivninger_field(self):
        """Gets the nedskrivninger_field of this OkonomiDetaljerForetak.  


        :return: The nedskrivninger_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._nedskrivninger_field

    @nedskrivninger_field.setter
    def nedskrivninger_field(self, nedskrivninger_field):
        """Sets the nedskrivninger_field of this OkonomiDetaljerForetak.


        :param nedskrivninger_field: The nedskrivninger_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._nedskrivninger_field = nedskrivninger_field

    @property
    def annen_driftskostnad_field(self):
        """Gets the annen_driftskostnad_field of this OkonomiDetaljerForetak.  


        :return: The annen_driftskostnad_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._annen_driftskostnad_field

    @annen_driftskostnad_field.setter
    def annen_driftskostnad_field(self, annen_driftskostnad_field):
        """Sets the annen_driftskostnad_field of this OkonomiDetaljerForetak.


        :param annen_driftskostnad_field: The annen_driftskostnad_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._annen_driftskostnad_field = annen_driftskostnad_field

    @property
    def drifts_resultat_field(self):
        """Gets the drifts_resultat_field of this OkonomiDetaljerForetak.  


        :return: The drifts_resultat_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._drifts_resultat_field

    @drifts_resultat_field.setter
    def drifts_resultat_field(self, drifts_resultat_field):
        """Sets the drifts_resultat_field of this OkonomiDetaljerForetak.


        :param drifts_resultat_field: The drifts_resultat_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._drifts_resultat_field = drifts_resultat_field

    @property
    def inntekt_inv_datter_field(self):
        """Gets the inntekt_inv_datter_field of this OkonomiDetaljerForetak.  


        :return: The inntekt_inv_datter_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._inntekt_inv_datter_field

    @inntekt_inv_datter_field.setter
    def inntekt_inv_datter_field(self, inntekt_inv_datter_field):
        """Sets the inntekt_inv_datter_field of this OkonomiDetaljerForetak.


        :param inntekt_inv_datter_field: The inntekt_inv_datter_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._inntekt_inv_datter_field = inntekt_inv_datter_field

    @property
    def inntekt_inv_konsern_field(self):
        """Gets the inntekt_inv_konsern_field of this OkonomiDetaljerForetak.  


        :return: The inntekt_inv_konsern_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._inntekt_inv_konsern_field

    @inntekt_inv_konsern_field.setter
    def inntekt_inv_konsern_field(self, inntekt_inv_konsern_field):
        """Sets the inntekt_inv_konsern_field of this OkonomiDetaljerForetak.


        :param inntekt_inv_konsern_field: The inntekt_inv_konsern_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._inntekt_inv_konsern_field = inntekt_inv_konsern_field

    @property
    def inntekt_inv_annen_field(self):
        """Gets the inntekt_inv_annen_field of this OkonomiDetaljerForetak.  


        :return: The inntekt_inv_annen_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._inntekt_inv_annen_field

    @inntekt_inv_annen_field.setter
    def inntekt_inv_annen_field(self, inntekt_inv_annen_field):
        """Sets the inntekt_inv_annen_field of this OkonomiDetaljerForetak.


        :param inntekt_inv_annen_field: The inntekt_inv_annen_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._inntekt_inv_annen_field = inntekt_inv_annen_field

    @property
    def renteinntekt_konsern_field(self):
        """Gets the renteinntekt_konsern_field of this OkonomiDetaljerForetak.  


        :return: The renteinntekt_konsern_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._renteinntekt_konsern_field

    @renteinntekt_konsern_field.setter
    def renteinntekt_konsern_field(self, renteinntekt_konsern_field):
        """Sets the renteinntekt_konsern_field of this OkonomiDetaljerForetak.


        :param renteinntekt_konsern_field: The renteinntekt_konsern_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._renteinntekt_konsern_field = renteinntekt_konsern_field

    @property
    def renteinntekt_annen_field(self):
        """Gets the renteinntekt_annen_field of this OkonomiDetaljerForetak.  


        :return: The renteinntekt_annen_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._renteinntekt_annen_field

    @renteinntekt_annen_field.setter
    def renteinntekt_annen_field(self, renteinntekt_annen_field):
        """Sets the renteinntekt_annen_field of this OkonomiDetaljerForetak.


        :param renteinntekt_annen_field: The renteinntekt_annen_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._renteinntekt_annen_field = renteinntekt_annen_field

    @property
    def finansinntekt_annen_field(self):
        """Gets the finansinntekt_annen_field of this OkonomiDetaljerForetak.  


        :return: The finansinntekt_annen_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._finansinntekt_annen_field

    @finansinntekt_annen_field.setter
    def finansinntekt_annen_field(self, finansinntekt_annen_field):
        """Sets the finansinntekt_annen_field of this OkonomiDetaljerForetak.


        :param finansinntekt_annen_field: The finansinntekt_annen_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._finansinntekt_annen_field = finansinntekt_annen_field

    @property
    def finansinntekt_field(self):
        """Gets the finansinntekt_field of this OkonomiDetaljerForetak.  


        :return: The finansinntekt_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._finansinntekt_field

    @finansinntekt_field.setter
    def finansinntekt_field(self, finansinntekt_field):
        """Sets the finansinntekt_field of this OkonomiDetaljerForetak.


        :param finansinntekt_field: The finansinntekt_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._finansinntekt_field = finansinntekt_field

    @property
    def verdiendring_mar_fin_omlopsmidler_field(self):
        """Gets the verdiendring_mar_fin_omlopsmidler_field of this OkonomiDetaljerForetak.  


        :return: The verdiendring_mar_fin_omlopsmidler_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._verdiendring_mar_fin_omlopsmidler_field

    @verdiendring_mar_fin_omlopsmidler_field.setter
    def verdiendring_mar_fin_omlopsmidler_field(self, verdiendring_mar_fin_omlopsmidler_field):
        """Sets the verdiendring_mar_fin_omlopsmidler_field of this OkonomiDetaljerForetak.


        :param verdiendring_mar_fin_omlopsmidler_field: The verdiendring_mar_fin_omlopsmidler_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._verdiendring_mar_fin_omlopsmidler_field = verdiendring_mar_fin_omlopsmidler_field

    @property
    def nedskrivning_mar_fin_omlopsmidler_field(self):
        """Gets the nedskrivning_mar_fin_omlopsmidler_field of this OkonomiDetaljerForetak.  


        :return: The nedskrivning_mar_fin_omlopsmidler_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._nedskrivning_mar_fin_omlopsmidler_field

    @nedskrivning_mar_fin_omlopsmidler_field.setter
    def nedskrivning_mar_fin_omlopsmidler_field(self, nedskrivning_mar_fin_omlopsmidler_field):
        """Sets the nedskrivning_mar_fin_omlopsmidler_field of this OkonomiDetaljerForetak.


        :param nedskrivning_mar_fin_omlopsmidler_field: The nedskrivning_mar_fin_omlopsmidler_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._nedskrivning_mar_fin_omlopsmidler_field = nedskrivning_mar_fin_omlopsmidler_field

    @property
    def nedskrivning_fin_anleggsmidler_field(self):
        """Gets the nedskrivning_fin_anleggsmidler_field of this OkonomiDetaljerForetak.  


        :return: The nedskrivning_fin_anleggsmidler_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._nedskrivning_fin_anleggsmidler_field

    @nedskrivning_fin_anleggsmidler_field.setter
    def nedskrivning_fin_anleggsmidler_field(self, nedskrivning_fin_anleggsmidler_field):
        """Sets the nedskrivning_fin_anleggsmidler_field of this OkonomiDetaljerForetak.


        :param nedskrivning_fin_anleggsmidler_field: The nedskrivning_fin_anleggsmidler_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._nedskrivning_fin_anleggsmidler_field = nedskrivning_fin_anleggsmidler_field

    @property
    def rentekostnad_konsern_field(self):
        """Gets the rentekostnad_konsern_field of this OkonomiDetaljerForetak.  


        :return: The rentekostnad_konsern_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._rentekostnad_konsern_field

    @rentekostnad_konsern_field.setter
    def rentekostnad_konsern_field(self, rentekostnad_konsern_field):
        """Sets the rentekostnad_konsern_field of this OkonomiDetaljerForetak.


        :param rentekostnad_konsern_field: The rentekostnad_konsern_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._rentekostnad_konsern_field = rentekostnad_konsern_field

    @property
    def annen_rentekostnad_field(self):
        """Gets the annen_rentekostnad_field of this OkonomiDetaljerForetak.  


        :return: The annen_rentekostnad_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._annen_rentekostnad_field

    @annen_rentekostnad_field.setter
    def annen_rentekostnad_field(self, annen_rentekostnad_field):
        """Sets the annen_rentekostnad_field of this OkonomiDetaljerForetak.


        :param annen_rentekostnad_field: The annen_rentekostnad_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._annen_rentekostnad_field = annen_rentekostnad_field

    @property
    def annen_finanskostnad_field(self):
        """Gets the annen_finanskostnad_field of this OkonomiDetaljerForetak.  


        :return: The annen_finanskostnad_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._annen_finanskostnad_field

    @annen_finanskostnad_field.setter
    def annen_finanskostnad_field(self, annen_finanskostnad_field):
        """Sets the annen_finanskostnad_field of this OkonomiDetaljerForetak.


        :param annen_finanskostnad_field: The annen_finanskostnad_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._annen_finanskostnad_field = annen_finanskostnad_field

    @property
    def finanskostnad_field(self):
        """Gets the finanskostnad_field of this OkonomiDetaljerForetak.  


        :return: The finanskostnad_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._finanskostnad_field

    @finanskostnad_field.setter
    def finanskostnad_field(self, finanskostnad_field):
        """Sets the finanskostnad_field of this OkonomiDetaljerForetak.


        :param finanskostnad_field: The finanskostnad_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._finanskostnad_field = finanskostnad_field

    @property
    def ord_resultat_for_skatt_field(self):
        """Gets the ord_resultat_for_skatt_field of this OkonomiDetaljerForetak.  


        :return: The ord_resultat_for_skatt_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._ord_resultat_for_skatt_field

    @ord_resultat_for_skatt_field.setter
    def ord_resultat_for_skatt_field(self, ord_resultat_for_skatt_field):
        """Sets the ord_resultat_for_skatt_field of this OkonomiDetaljerForetak.


        :param ord_resultat_for_skatt_field: The ord_resultat_for_skatt_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._ord_resultat_for_skatt_field = ord_resultat_for_skatt_field

    @property
    def skatt_ord_resultat_field(self):
        """Gets the skatt_ord_resultat_field of this OkonomiDetaljerForetak.  


        :return: The skatt_ord_resultat_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._skatt_ord_resultat_field

    @skatt_ord_resultat_field.setter
    def skatt_ord_resultat_field(self, skatt_ord_resultat_field):
        """Sets the skatt_ord_resultat_field of this OkonomiDetaljerForetak.


        :param skatt_ord_resultat_field: The skatt_ord_resultat_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._skatt_ord_resultat_field = skatt_ord_resultat_field

    @property
    def ord_resultat_field(self):
        """Gets the ord_resultat_field of this OkonomiDetaljerForetak.  


        :return: The ord_resultat_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._ord_resultat_field

    @ord_resultat_field.setter
    def ord_resultat_field(self, ord_resultat_field):
        """Sets the ord_resultat_field of this OkonomiDetaljerForetak.


        :param ord_resultat_field: The ord_resultat_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._ord_resultat_field = ord_resultat_field

    @property
    def ekstraord_inntekt_field(self):
        """Gets the ekstraord_inntekt_field of this OkonomiDetaljerForetak.  


        :return: The ekstraord_inntekt_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._ekstraord_inntekt_field

    @ekstraord_inntekt_field.setter
    def ekstraord_inntekt_field(self, ekstraord_inntekt_field):
        """Sets the ekstraord_inntekt_field of this OkonomiDetaljerForetak.


        :param ekstraord_inntekt_field: The ekstraord_inntekt_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._ekstraord_inntekt_field = ekstraord_inntekt_field

    @property
    def ekstraord_kostnad_field(self):
        """Gets the ekstraord_kostnad_field of this OkonomiDetaljerForetak.  


        :return: The ekstraord_kostnad_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._ekstraord_kostnad_field

    @ekstraord_kostnad_field.setter
    def ekstraord_kostnad_field(self, ekstraord_kostnad_field):
        """Sets the ekstraord_kostnad_field of this OkonomiDetaljerForetak.


        :param ekstraord_kostnad_field: The ekstraord_kostnad_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._ekstraord_kostnad_field = ekstraord_kostnad_field

    @property
    def skatt_ekstraord_resultat_field(self):
        """Gets the skatt_ekstraord_resultat_field of this OkonomiDetaljerForetak.  


        :return: The skatt_ekstraord_resultat_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._skatt_ekstraord_resultat_field

    @skatt_ekstraord_resultat_field.setter
    def skatt_ekstraord_resultat_field(self, skatt_ekstraord_resultat_field):
        """Sets the skatt_ekstraord_resultat_field of this OkonomiDetaljerForetak.


        :param skatt_ekstraord_resultat_field: The skatt_ekstraord_resultat_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._skatt_ekstraord_resultat_field = skatt_ekstraord_resultat_field

    @property
    def sum_skatt_field(self):
        """Gets the sum_skatt_field of this OkonomiDetaljerForetak.  


        :return: The sum_skatt_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._sum_skatt_field

    @sum_skatt_field.setter
    def sum_skatt_field(self, sum_skatt_field):
        """Sets the sum_skatt_field of this OkonomiDetaljerForetak.


        :param sum_skatt_field: The sum_skatt_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._sum_skatt_field = sum_skatt_field

    @property
    def minoritets_interesser_field(self):
        """Gets the minoritets_interesser_field of this OkonomiDetaljerForetak.  


        :return: The minoritets_interesser_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._minoritets_interesser_field

    @minoritets_interesser_field.setter
    def minoritets_interesser_field(self, minoritets_interesser_field):
        """Sets the minoritets_interesser_field of this OkonomiDetaljerForetak.


        :param minoritets_interesser_field: The minoritets_interesser_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._minoritets_interesser_field = minoritets_interesser_field

    @property
    def ars_resultat_field(self):
        """Gets the ars_resultat_field of this OkonomiDetaljerForetak.  


        :return: The ars_resultat_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._ars_resultat_field

    @ars_resultat_field.setter
    def ars_resultat_field(self, ars_resultat_field):
        """Sets the ars_resultat_field of this OkonomiDetaljerForetak.


        :param ars_resultat_field: The ars_resultat_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._ars_resultat_field = ars_resultat_field

    @property
    def konsernbidrag_field(self):
        """Gets the konsernbidrag_field of this OkonomiDetaljerForetak.  


        :return: The konsernbidrag_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._konsernbidrag_field

    @konsernbidrag_field.setter
    def konsernbidrag_field(self, konsernbidrag_field):
        """Sets the konsernbidrag_field of this OkonomiDetaljerForetak.


        :param konsernbidrag_field: The konsernbidrag_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._konsernbidrag_field = konsernbidrag_field

    @property
    def utbytte_field(self):
        """Gets the utbytte_field of this OkonomiDetaljerForetak.  


        :return: The utbytte_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._utbytte_field

    @utbytte_field.setter
    def utbytte_field(self, utbytte_field):
        """Sets the utbytte_field of this OkonomiDetaljerForetak.


        :param utbytte_field: The utbytte_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._utbytte_field = utbytte_field

    @property
    def til_fond_vurd_for_field(self):
        """Gets the til_fond_vurd_for_field of this OkonomiDetaljerForetak.  


        :return: The til_fond_vurd_for_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._til_fond_vurd_for_field

    @til_fond_vurd_for_field.setter
    def til_fond_vurd_for_field(self, til_fond_vurd_for_field):
        """Sets the til_fond_vurd_for_field of this OkonomiDetaljerForetak.


        :param til_fond_vurd_for_field: The til_fond_vurd_for_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._til_fond_vurd_for_field = til_fond_vurd_for_field

    @property
    def til_annen_egenkapital_field(self):
        """Gets the til_annen_egenkapital_field of this OkonomiDetaljerForetak.  


        :return: The til_annen_egenkapital_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._til_annen_egenkapital_field

    @til_annen_egenkapital_field.setter
    def til_annen_egenkapital_field(self, til_annen_egenkapital_field):
        """Sets the til_annen_egenkapital_field of this OkonomiDetaljerForetak.


        :param til_annen_egenkapital_field: The til_annen_egenkapital_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._til_annen_egenkapital_field = til_annen_egenkapital_field

    @property
    def tap_krav_field(self):
        """Gets the tap_krav_field of this OkonomiDetaljerForetak.  


        :return: The tap_krav_field of this OkonomiDetaljerForetak.  
        :rtype: int
        """
        return self._tap_krav_field

    @tap_krav_field.setter
    def tap_krav_field(self, tap_krav_field):
        """Sets the tap_krav_field of this OkonomiDetaljerForetak.


        :param tap_krav_field: The tap_krav_field of this OkonomiDetaljerForetak.  
        :type: int
        """

        self._tap_krav_field = tap_krav_field

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
        if not isinstance(other, OkonomiDetaljerForetak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
