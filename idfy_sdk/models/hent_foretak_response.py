# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six

from idfy_sdk.models.aksjonar import Aksjonar  
from idfy_sdk.models.avdeling_data import AvdelingData  
from idfy_sdk.models.beta_detaljer import BetaDetaljer  
from idfy_sdk.models.beta_sammendrag import BetaSammendrag  
from idfy_sdk.models.datterselskap import Datterselskap  
from idfy_sdk.models.eiendeler_foretak import EiendelerForetak  
from idfy_sdk.models.eiendeler_konsern import EiendelerKonsern  
from idfy_sdk.models.eiendom_norge import EiendomNorge  
from idfy_sdk.models.eiendom_norge_liste import EiendomNorgeListe  
from idfy_sdk.models.fullmakt_foretak import FullmaktForetak  
from idfy_sdk.models.gjeld_egenkapital_foretak import GjeldEgenkapitalForetak  
from idfy_sdk.models.gjeld_egenkapital_konsern import GjeldEgenkapitalKonsern  
from idfy_sdk.models.grunnfakta import Grunnfakta  
from idfy_sdk.models.historisk_rating import HistoriskRating  
from idfy_sdk.models.identifikasjon import Identifikasjon  
from idfy_sdk.models.juridisk import Juridisk  
from idfy_sdk.models.konsern_link import KonsernLink  
from idfy_sdk.models.losore import Losore  
from idfy_sdk.models.meldinger import Meldinger  
from idfy_sdk.models.navn_adresse import NavnAdresse  
from idfy_sdk.models.nokkeltall_bransje import NokkeltallBransje  
from idfy_sdk.models.nokkeltall_foretak import NokkeltallForetak  
from idfy_sdk.models.nokkeltall_konsern import NokkeltallKonsern  
from idfy_sdk.models.okonomi_detaljer_foretak import OkonomiDetaljerForetak  
from idfy_sdk.models.okonomi_detaljer_konsern import OkonomiDetaljerKonsern  
from idfy_sdk.models.okonomi_enk import OkonomiEnk  
from idfy_sdk.models.okonomi_sammendrag_foretak import OkonomiSammendragForetak  
from idfy_sdk.models.okonomi_sammendrag_konsern import OkonomiSammendragKonsern  
from idfy_sdk.models.rating import Rating  
from idfy_sdk.models.rettighetshavere import Rettighetshavere  
from idfy_sdk.models.scoring import Scoring  
from idfy_sdk.models.verv import Verv  


class HentForetakResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identifikasjon_field': 'Identifikasjon',
        'navn_adresse_field': 'NavnAdresse',
        'rating_field': 'Rating',
        'hist_rating_field': 'list[HistoriskRating]',
        'grunnfakta_field': 'Grunnfakta',
        'juridisk_field': 'list[Juridisk]',
        'verv_field': 'list[Verv]',
        'aksjonar_field': 'list[Aksjonar]',
        'datterselskap_field': 'list[Datterselskap]',
        'okonomi_enk_field': 'list[OkonomiEnk]',
        'nokkeltall_foretak_field': 'list[NokkeltallForetak]',
        'nokkeltall_bransje_field': 'list[NokkeltallBransje]',
        'nokkeltall_konsern_field': 'list[NokkeltallKonsern]',
        'beta_sammendrag_field': 'BetaSammendrag',
        'beta_detaljer_field': 'list[BetaDetaljer]',
        'losore_field': 'list[Losore]',
        'eiendom_norge_field': 'EiendomNorge',
        'konsern_link_field': 'list[KonsernLink]',
        'scoring_field': 'Scoring',
        'okonomi_sammendrag_foretak_field': 'list[OkonomiSammendragForetak]',
        'okonomi_sammendrag_konsern_field': 'list[OkonomiSammendragKonsern]',
        'okonomi_detaljer_foretak_field': 'list[OkonomiDetaljerForetak]',
        'okonomi_detaljer_konsern_field': 'list[OkonomiDetaljerKonsern]',
        'eiendeler_foretak_field': 'list[EiendelerForetak]',
        'eiendeler_konsern_field': 'list[EiendelerKonsern]',
        'gjeld_egenkapital_foretak_field': 'list[GjeldEgenkapitalForetak]',
        'gjeld_egenkapital_konsern_field': 'list[GjeldEgenkapitalKonsern]',
        'avdeling_data_field': 'AvdelingData',
        'rettighetshavere_field': 'list[Rettighetshavere]',
        'eiendom_norge_liste_field': 'list[EiendomNorgeListe]',
        'fullmakt_foretak_field': 'list[FullmaktForetak]',
        'meldinger_field': 'list[Meldinger]'
    }

    attribute_map = {
        'identifikasjon_field': 'identifikasjonField',
        'navn_adresse_field': 'navnAdresseField',
        'rating_field': 'ratingField',
        'hist_rating_field': 'histRatingField',
        'grunnfakta_field': 'grunnfaktaField',
        'juridisk_field': 'juridiskField',
        'verv_field': 'vervField',
        'aksjonar_field': 'aksjonarField',
        'datterselskap_field': 'datterselskapField',
        'okonomi_enk_field': 'okonomiEnkField',
        'nokkeltall_foretak_field': 'nokkeltallForetakField',
        'nokkeltall_bransje_field': 'nokkeltallBransjeField',
        'nokkeltall_konsern_field': 'nokkeltallKonsernField',
        'beta_sammendrag_field': 'betaSammendragField',
        'beta_detaljer_field': 'betaDetaljerField',
        'losore_field': 'losoreField',
        'eiendom_norge_field': 'eiendomNorgeField',
        'konsern_link_field': 'konsernLinkField',
        'scoring_field': 'scoringField',
        'okonomi_sammendrag_foretak_field': 'okonomiSammendragForetakField',
        'okonomi_sammendrag_konsern_field': 'okonomiSammendragKonsernField',
        'okonomi_detaljer_foretak_field': 'okonomiDetaljerForetakField',
        'okonomi_detaljer_konsern_field': 'okonomiDetaljerKonsernField',
        'eiendeler_foretak_field': 'eiendelerForetakField',
        'eiendeler_konsern_field': 'eiendelerKonsernField',
        'gjeld_egenkapital_foretak_field': 'gjeldEgenkapitalForetakField',
        'gjeld_egenkapital_konsern_field': 'gjeldEgenkapitalKonsernField',
        'avdeling_data_field': 'avdelingDataField',
        'rettighetshavere_field': 'rettighetshavereField',
        'eiendom_norge_liste_field': 'eiendomNorgeListeField',
        'fullmakt_foretak_field': 'fullmaktForetakField',
        'meldinger_field': 'meldingerField'
    }

    def __init__(self, identifikasjon_field=None, navn_adresse_field=None, rating_field=None, hist_rating_field=None, grunnfakta_field=None, juridisk_field=None, verv_field=None, aksjonar_field=None, datterselskap_field=None, okonomi_enk_field=None, nokkeltall_foretak_field=None, nokkeltall_bransje_field=None, nokkeltall_konsern_field=None, beta_sammendrag_field=None, beta_detaljer_field=None, losore_field=None, eiendom_norge_field=None, konsern_link_field=None, scoring_field=None, okonomi_sammendrag_foretak_field=None, okonomi_sammendrag_konsern_field=None, okonomi_detaljer_foretak_field=None, okonomi_detaljer_konsern_field=None, eiendeler_foretak_field=None, eiendeler_konsern_field=None, gjeld_egenkapital_foretak_field=None, gjeld_egenkapital_konsern_field=None, avdeling_data_field=None, rettighetshavere_field=None, eiendom_norge_liste_field=None, fullmakt_foretak_field=None, meldinger_field=None):  
        """HentForetakResponse"""  

        self._identifikasjon_field = None
        self._navn_adresse_field = None
        self._rating_field = None
        self._hist_rating_field = None
        self._grunnfakta_field = None
        self._juridisk_field = None
        self._verv_field = None
        self._aksjonar_field = None
        self._datterselskap_field = None
        self._okonomi_enk_field = None
        self._nokkeltall_foretak_field = None
        self._nokkeltall_bransje_field = None
        self._nokkeltall_konsern_field = None
        self._beta_sammendrag_field = None
        self._beta_detaljer_field = None
        self._losore_field = None
        self._eiendom_norge_field = None
        self._konsern_link_field = None
        self._scoring_field = None
        self._okonomi_sammendrag_foretak_field = None
        self._okonomi_sammendrag_konsern_field = None
        self._okonomi_detaljer_foretak_field = None
        self._okonomi_detaljer_konsern_field = None
        self._eiendeler_foretak_field = None
        self._eiendeler_konsern_field = None
        self._gjeld_egenkapital_foretak_field = None
        self._gjeld_egenkapital_konsern_field = None
        self._avdeling_data_field = None
        self._rettighetshavere_field = None
        self._eiendom_norge_liste_field = None
        self._fullmakt_foretak_field = None
        self._meldinger_field = None
        self.discriminator = None

        if identifikasjon_field is not None:
            self.identifikasjon_field = identifikasjon_field
        if navn_adresse_field is not None:
            self.navn_adresse_field = navn_adresse_field
        if rating_field is not None:
            self.rating_field = rating_field
        if hist_rating_field is not None:
            self.hist_rating_field = hist_rating_field
        if grunnfakta_field is not None:
            self.grunnfakta_field = grunnfakta_field
        if juridisk_field is not None:
            self.juridisk_field = juridisk_field
        if verv_field is not None:
            self.verv_field = verv_field
        if aksjonar_field is not None:
            self.aksjonar_field = aksjonar_field
        if datterselskap_field is not None:
            self.datterselskap_field = datterselskap_field
        if okonomi_enk_field is not None:
            self.okonomi_enk_field = okonomi_enk_field
        if nokkeltall_foretak_field is not None:
            self.nokkeltall_foretak_field = nokkeltall_foretak_field
        if nokkeltall_bransje_field is not None:
            self.nokkeltall_bransje_field = nokkeltall_bransje_field
        if nokkeltall_konsern_field is not None:
            self.nokkeltall_konsern_field = nokkeltall_konsern_field
        if beta_sammendrag_field is not None:
            self.beta_sammendrag_field = beta_sammendrag_field
        if beta_detaljer_field is not None:
            self.beta_detaljer_field = beta_detaljer_field
        if losore_field is not None:
            self.losore_field = losore_field
        if eiendom_norge_field is not None:
            self.eiendom_norge_field = eiendom_norge_field
        if konsern_link_field is not None:
            self.konsern_link_field = konsern_link_field
        if scoring_field is not None:
            self.scoring_field = scoring_field
        if okonomi_sammendrag_foretak_field is not None:
            self.okonomi_sammendrag_foretak_field = okonomi_sammendrag_foretak_field
        if okonomi_sammendrag_konsern_field is not None:
            self.okonomi_sammendrag_konsern_field = okonomi_sammendrag_konsern_field
        if okonomi_detaljer_foretak_field is not None:
            self.okonomi_detaljer_foretak_field = okonomi_detaljer_foretak_field
        if okonomi_detaljer_konsern_field is not None:
            self.okonomi_detaljer_konsern_field = okonomi_detaljer_konsern_field
        if eiendeler_foretak_field is not None:
            self.eiendeler_foretak_field = eiendeler_foretak_field
        if eiendeler_konsern_field is not None:
            self.eiendeler_konsern_field = eiendeler_konsern_field
        if gjeld_egenkapital_foretak_field is not None:
            self.gjeld_egenkapital_foretak_field = gjeld_egenkapital_foretak_field
        if gjeld_egenkapital_konsern_field is not None:
            self.gjeld_egenkapital_konsern_field = gjeld_egenkapital_konsern_field
        if avdeling_data_field is not None:
            self.avdeling_data_field = avdeling_data_field
        if rettighetshavere_field is not None:
            self.rettighetshavere_field = rettighetshavere_field
        if eiendom_norge_liste_field is not None:
            self.eiendom_norge_liste_field = eiendom_norge_liste_field
        if fullmakt_foretak_field is not None:
            self.fullmakt_foretak_field = fullmakt_foretak_field
        if meldinger_field is not None:
            self.meldinger_field = meldinger_field

    @property
    def identifikasjon_field(self):
        """Gets the identifikasjon_field of this HentForetakResponse.  


        :return: The identifikasjon_field of this HentForetakResponse.  
        :rtype: Identifikasjon
        """
        return self._identifikasjon_field

    @identifikasjon_field.setter
    def identifikasjon_field(self, identifikasjon_field):
        """Sets the identifikasjon_field of this HentForetakResponse.


        :param identifikasjon_field: The identifikasjon_field of this HentForetakResponse.  
        :type: Identifikasjon
        """

        self._identifikasjon_field = identifikasjon_field

    @property
    def navn_adresse_field(self):
        """Gets the navn_adresse_field of this HentForetakResponse.  


        :return: The navn_adresse_field of this HentForetakResponse.  
        :rtype: NavnAdresse
        """
        return self._navn_adresse_field

    @navn_adresse_field.setter
    def navn_adresse_field(self, navn_adresse_field):
        """Sets the navn_adresse_field of this HentForetakResponse.


        :param navn_adresse_field: The navn_adresse_field of this HentForetakResponse.  
        :type: NavnAdresse
        """

        self._navn_adresse_field = navn_adresse_field

    @property
    def rating_field(self):
        """Gets the rating_field of this HentForetakResponse.  


        :return: The rating_field of this HentForetakResponse.  
        :rtype: Rating
        """
        return self._rating_field

    @rating_field.setter
    def rating_field(self, rating_field):
        """Sets the rating_field of this HentForetakResponse.


        :param rating_field: The rating_field of this HentForetakResponse.  
        :type: Rating
        """

        self._rating_field = rating_field

    @property
    def hist_rating_field(self):
        """Gets the hist_rating_field of this HentForetakResponse.  


        :return: The hist_rating_field of this HentForetakResponse.  
        :rtype: list[HistoriskRating]
        """
        return self._hist_rating_field

    @hist_rating_field.setter
    def hist_rating_field(self, hist_rating_field):
        """Sets the hist_rating_field of this HentForetakResponse.


        :param hist_rating_field: The hist_rating_field of this HentForetakResponse.  
        :type: list[HistoriskRating]
        """

        self._hist_rating_field = hist_rating_field

    @property
    def grunnfakta_field(self):
        """Gets the grunnfakta_field of this HentForetakResponse.  


        :return: The grunnfakta_field of this HentForetakResponse.  
        :rtype: Grunnfakta
        """
        return self._grunnfakta_field

    @grunnfakta_field.setter
    def grunnfakta_field(self, grunnfakta_field):
        """Sets the grunnfakta_field of this HentForetakResponse.


        :param grunnfakta_field: The grunnfakta_field of this HentForetakResponse.  
        :type: Grunnfakta
        """

        self._grunnfakta_field = grunnfakta_field

    @property
    def juridisk_field(self):
        """Gets the juridisk_field of this HentForetakResponse.  


        :return: The juridisk_field of this HentForetakResponse.  
        :rtype: list[Juridisk]
        """
        return self._juridisk_field

    @juridisk_field.setter
    def juridisk_field(self, juridisk_field):
        """Sets the juridisk_field of this HentForetakResponse.


        :param juridisk_field: The juridisk_field of this HentForetakResponse.  
        :type: list[Juridisk]
        """

        self._juridisk_field = juridisk_field

    @property
    def verv_field(self):
        """Gets the verv_field of this HentForetakResponse.  


        :return: The verv_field of this HentForetakResponse.  
        :rtype: list[Verv]
        """
        return self._verv_field

    @verv_field.setter
    def verv_field(self, verv_field):
        """Sets the verv_field of this HentForetakResponse.


        :param verv_field: The verv_field of this HentForetakResponse.  
        :type: list[Verv]
        """

        self._verv_field = verv_field

    @property
    def aksjonar_field(self):
        """Gets the aksjonar_field of this HentForetakResponse.  


        :return: The aksjonar_field of this HentForetakResponse.  
        :rtype: list[Aksjonar]
        """
        return self._aksjonar_field

    @aksjonar_field.setter
    def aksjonar_field(self, aksjonar_field):
        """Sets the aksjonar_field of this HentForetakResponse.


        :param aksjonar_field: The aksjonar_field of this HentForetakResponse.  
        :type: list[Aksjonar]
        """

        self._aksjonar_field = aksjonar_field

    @property
    def datterselskap_field(self):
        """Gets the datterselskap_field of this HentForetakResponse.  


        :return: The datterselskap_field of this HentForetakResponse.  
        :rtype: list[Datterselskap]
        """
        return self._datterselskap_field

    @datterselskap_field.setter
    def datterselskap_field(self, datterselskap_field):
        """Sets the datterselskap_field of this HentForetakResponse.


        :param datterselskap_field: The datterselskap_field of this HentForetakResponse.  
        :type: list[Datterselskap]
        """

        self._datterselskap_field = datterselskap_field

    @property
    def okonomi_enk_field(self):
        """Gets the okonomi_enk_field of this HentForetakResponse.  


        :return: The okonomi_enk_field of this HentForetakResponse.  
        :rtype: list[OkonomiEnk]
        """
        return self._okonomi_enk_field

    @okonomi_enk_field.setter
    def okonomi_enk_field(self, okonomi_enk_field):
        """Sets the okonomi_enk_field of this HentForetakResponse.


        :param okonomi_enk_field: The okonomi_enk_field of this HentForetakResponse.  
        :type: list[OkonomiEnk]
        """

        self._okonomi_enk_field = okonomi_enk_field

    @property
    def nokkeltall_foretak_field(self):
        """Gets the nokkeltall_foretak_field of this HentForetakResponse.  


        :return: The nokkeltall_foretak_field of this HentForetakResponse.  
        :rtype: list[NokkeltallForetak]
        """
        return self._nokkeltall_foretak_field

    @nokkeltall_foretak_field.setter
    def nokkeltall_foretak_field(self, nokkeltall_foretak_field):
        """Sets the nokkeltall_foretak_field of this HentForetakResponse.


        :param nokkeltall_foretak_field: The nokkeltall_foretak_field of this HentForetakResponse.  
        :type: list[NokkeltallForetak]
        """

        self._nokkeltall_foretak_field = nokkeltall_foretak_field

    @property
    def nokkeltall_bransje_field(self):
        """Gets the nokkeltall_bransje_field of this HentForetakResponse.  


        :return: The nokkeltall_bransje_field of this HentForetakResponse.  
        :rtype: list[NokkeltallBransje]
        """
        return self._nokkeltall_bransje_field

    @nokkeltall_bransje_field.setter
    def nokkeltall_bransje_field(self, nokkeltall_bransje_field):
        """Sets the nokkeltall_bransje_field of this HentForetakResponse.


        :param nokkeltall_bransje_field: The nokkeltall_bransje_field of this HentForetakResponse.  
        :type: list[NokkeltallBransje]
        """

        self._nokkeltall_bransje_field = nokkeltall_bransje_field

    @property
    def nokkeltall_konsern_field(self):
        """Gets the nokkeltall_konsern_field of this HentForetakResponse.  


        :return: The nokkeltall_konsern_field of this HentForetakResponse.  
        :rtype: list[NokkeltallKonsern]
        """
        return self._nokkeltall_konsern_field

    @nokkeltall_konsern_field.setter
    def nokkeltall_konsern_field(self, nokkeltall_konsern_field):
        """Sets the nokkeltall_konsern_field of this HentForetakResponse.


        :param nokkeltall_konsern_field: The nokkeltall_konsern_field of this HentForetakResponse.  
        :type: list[NokkeltallKonsern]
        """

        self._nokkeltall_konsern_field = nokkeltall_konsern_field

    @property
    def beta_sammendrag_field(self):
        """Gets the beta_sammendrag_field of this HentForetakResponse.  


        :return: The beta_sammendrag_field of this HentForetakResponse.  
        :rtype: BetaSammendrag
        """
        return self._beta_sammendrag_field

    @beta_sammendrag_field.setter
    def beta_sammendrag_field(self, beta_sammendrag_field):
        """Sets the beta_sammendrag_field of this HentForetakResponse.


        :param beta_sammendrag_field: The beta_sammendrag_field of this HentForetakResponse.  
        :type: BetaSammendrag
        """

        self._beta_sammendrag_field = beta_sammendrag_field

    @property
    def beta_detaljer_field(self):
        """Gets the beta_detaljer_field of this HentForetakResponse.  


        :return: The beta_detaljer_field of this HentForetakResponse.  
        :rtype: list[BetaDetaljer]
        """
        return self._beta_detaljer_field

    @beta_detaljer_field.setter
    def beta_detaljer_field(self, beta_detaljer_field):
        """Sets the beta_detaljer_field of this HentForetakResponse.


        :param beta_detaljer_field: The beta_detaljer_field of this HentForetakResponse.  
        :type: list[BetaDetaljer]
        """

        self._beta_detaljer_field = beta_detaljer_field

    @property
    def losore_field(self):
        """Gets the losore_field of this HentForetakResponse.  


        :return: The losore_field of this HentForetakResponse.  
        :rtype: list[Losore]
        """
        return self._losore_field

    @losore_field.setter
    def losore_field(self, losore_field):
        """Sets the losore_field of this HentForetakResponse.


        :param losore_field: The losore_field of this HentForetakResponse.  
        :type: list[Losore]
        """

        self._losore_field = losore_field

    @property
    def eiendom_norge_field(self):
        """Gets the eiendom_norge_field of this HentForetakResponse.  


        :return: The eiendom_norge_field of this HentForetakResponse.  
        :rtype: EiendomNorge
        """
        return self._eiendom_norge_field

    @eiendom_norge_field.setter
    def eiendom_norge_field(self, eiendom_norge_field):
        """Sets the eiendom_norge_field of this HentForetakResponse.


        :param eiendom_norge_field: The eiendom_norge_field of this HentForetakResponse.  
        :type: EiendomNorge
        """

        self._eiendom_norge_field = eiendom_norge_field

    @property
    def konsern_link_field(self):
        """Gets the konsern_link_field of this HentForetakResponse.  


        :return: The konsern_link_field of this HentForetakResponse.  
        :rtype: list[KonsernLink]
        """
        return self._konsern_link_field

    @konsern_link_field.setter
    def konsern_link_field(self, konsern_link_field):
        """Sets the konsern_link_field of this HentForetakResponse.


        :param konsern_link_field: The konsern_link_field of this HentForetakResponse.  
        :type: list[KonsernLink]
        """

        self._konsern_link_field = konsern_link_field

    @property
    def scoring_field(self):
        """Gets the scoring_field of this HentForetakResponse.  


        :return: The scoring_field of this HentForetakResponse.  
        :rtype: Scoring
        """
        return self._scoring_field

    @scoring_field.setter
    def scoring_field(self, scoring_field):
        """Sets the scoring_field of this HentForetakResponse.


        :param scoring_field: The scoring_field of this HentForetakResponse.  
        :type: Scoring
        """

        self._scoring_field = scoring_field

    @property
    def okonomi_sammendrag_foretak_field(self):
        """Gets the okonomi_sammendrag_foretak_field of this HentForetakResponse.  


        :return: The okonomi_sammendrag_foretak_field of this HentForetakResponse.  
        :rtype: list[OkonomiSammendragForetak]
        """
        return self._okonomi_sammendrag_foretak_field

    @okonomi_sammendrag_foretak_field.setter
    def okonomi_sammendrag_foretak_field(self, okonomi_sammendrag_foretak_field):
        """Sets the okonomi_sammendrag_foretak_field of this HentForetakResponse.


        :param okonomi_sammendrag_foretak_field: The okonomi_sammendrag_foretak_field of this HentForetakResponse.  
        :type: list[OkonomiSammendragForetak]
        """

        self._okonomi_sammendrag_foretak_field = okonomi_sammendrag_foretak_field

    @property
    def okonomi_sammendrag_konsern_field(self):
        """Gets the okonomi_sammendrag_konsern_field of this HentForetakResponse.  


        :return: The okonomi_sammendrag_konsern_field of this HentForetakResponse.  
        :rtype: list[OkonomiSammendragKonsern]
        """
        return self._okonomi_sammendrag_konsern_field

    @okonomi_sammendrag_konsern_field.setter
    def okonomi_sammendrag_konsern_field(self, okonomi_sammendrag_konsern_field):
        """Sets the okonomi_sammendrag_konsern_field of this HentForetakResponse.


        :param okonomi_sammendrag_konsern_field: The okonomi_sammendrag_konsern_field of this HentForetakResponse.  
        :type: list[OkonomiSammendragKonsern]
        """

        self._okonomi_sammendrag_konsern_field = okonomi_sammendrag_konsern_field

    @property
    def okonomi_detaljer_foretak_field(self):
        """Gets the okonomi_detaljer_foretak_field of this HentForetakResponse.  


        :return: The okonomi_detaljer_foretak_field of this HentForetakResponse.  
        :rtype: list[OkonomiDetaljerForetak]
        """
        return self._okonomi_detaljer_foretak_field

    @okonomi_detaljer_foretak_field.setter
    def okonomi_detaljer_foretak_field(self, okonomi_detaljer_foretak_field):
        """Sets the okonomi_detaljer_foretak_field of this HentForetakResponse.


        :param okonomi_detaljer_foretak_field: The okonomi_detaljer_foretak_field of this HentForetakResponse.  
        :type: list[OkonomiDetaljerForetak]
        """

        self._okonomi_detaljer_foretak_field = okonomi_detaljer_foretak_field

    @property
    def okonomi_detaljer_konsern_field(self):
        """Gets the okonomi_detaljer_konsern_field of this HentForetakResponse.  


        :return: The okonomi_detaljer_konsern_field of this HentForetakResponse.  
        :rtype: list[OkonomiDetaljerKonsern]
        """
        return self._okonomi_detaljer_konsern_field

    @okonomi_detaljer_konsern_field.setter
    def okonomi_detaljer_konsern_field(self, okonomi_detaljer_konsern_field):
        """Sets the okonomi_detaljer_konsern_field of this HentForetakResponse.


        :param okonomi_detaljer_konsern_field: The okonomi_detaljer_konsern_field of this HentForetakResponse.  
        :type: list[OkonomiDetaljerKonsern]
        """

        self._okonomi_detaljer_konsern_field = okonomi_detaljer_konsern_field

    @property
    def eiendeler_foretak_field(self):
        """Gets the eiendeler_foretak_field of this HentForetakResponse.  


        :return: The eiendeler_foretak_field of this HentForetakResponse.  
        :rtype: list[EiendelerForetak]
        """
        return self._eiendeler_foretak_field

    @eiendeler_foretak_field.setter
    def eiendeler_foretak_field(self, eiendeler_foretak_field):
        """Sets the eiendeler_foretak_field of this HentForetakResponse.


        :param eiendeler_foretak_field: The eiendeler_foretak_field of this HentForetakResponse.  
        :type: list[EiendelerForetak]
        """

        self._eiendeler_foretak_field = eiendeler_foretak_field

    @property
    def eiendeler_konsern_field(self):
        """Gets the eiendeler_konsern_field of this HentForetakResponse.  


        :return: The eiendeler_konsern_field of this HentForetakResponse.  
        :rtype: list[EiendelerKonsern]
        """
        return self._eiendeler_konsern_field

    @eiendeler_konsern_field.setter
    def eiendeler_konsern_field(self, eiendeler_konsern_field):
        """Sets the eiendeler_konsern_field of this HentForetakResponse.


        :param eiendeler_konsern_field: The eiendeler_konsern_field of this HentForetakResponse.  
        :type: list[EiendelerKonsern]
        """

        self._eiendeler_konsern_field = eiendeler_konsern_field

    @property
    def gjeld_egenkapital_foretak_field(self):
        """Gets the gjeld_egenkapital_foretak_field of this HentForetakResponse.  


        :return: The gjeld_egenkapital_foretak_field of this HentForetakResponse.  
        :rtype: list[GjeldEgenkapitalForetak]
        """
        return self._gjeld_egenkapital_foretak_field

    @gjeld_egenkapital_foretak_field.setter
    def gjeld_egenkapital_foretak_field(self, gjeld_egenkapital_foretak_field):
        """Sets the gjeld_egenkapital_foretak_field of this HentForetakResponse.


        :param gjeld_egenkapital_foretak_field: The gjeld_egenkapital_foretak_field of this HentForetakResponse.  
        :type: list[GjeldEgenkapitalForetak]
        """

        self._gjeld_egenkapital_foretak_field = gjeld_egenkapital_foretak_field

    @property
    def gjeld_egenkapital_konsern_field(self):
        """Gets the gjeld_egenkapital_konsern_field of this HentForetakResponse.  


        :return: The gjeld_egenkapital_konsern_field of this HentForetakResponse.  
        :rtype: list[GjeldEgenkapitalKonsern]
        """
        return self._gjeld_egenkapital_konsern_field

    @gjeld_egenkapital_konsern_field.setter
    def gjeld_egenkapital_konsern_field(self, gjeld_egenkapital_konsern_field):
        """Sets the gjeld_egenkapital_konsern_field of this HentForetakResponse.


        :param gjeld_egenkapital_konsern_field: The gjeld_egenkapital_konsern_field of this HentForetakResponse.  
        :type: list[GjeldEgenkapitalKonsern]
        """

        self._gjeld_egenkapital_konsern_field = gjeld_egenkapital_konsern_field

    @property
    def avdeling_data_field(self):
        """Gets the avdeling_data_field of this HentForetakResponse.  


        :return: The avdeling_data_field of this HentForetakResponse.  
        :rtype: AvdelingData
        """
        return self._avdeling_data_field

    @avdeling_data_field.setter
    def avdeling_data_field(self, avdeling_data_field):
        """Sets the avdeling_data_field of this HentForetakResponse.


        :param avdeling_data_field: The avdeling_data_field of this HentForetakResponse.  
        :type: AvdelingData
        """

        self._avdeling_data_field = avdeling_data_field

    @property
    def rettighetshavere_field(self):
        """Gets the rettighetshavere_field of this HentForetakResponse.  


        :return: The rettighetshavere_field of this HentForetakResponse.  
        :rtype: list[Rettighetshavere]
        """
        return self._rettighetshavere_field

    @rettighetshavere_field.setter
    def rettighetshavere_field(self, rettighetshavere_field):
        """Sets the rettighetshavere_field of this HentForetakResponse.


        :param rettighetshavere_field: The rettighetshavere_field of this HentForetakResponse.  
        :type: list[Rettighetshavere]
        """

        self._rettighetshavere_field = rettighetshavere_field

    @property
    def eiendom_norge_liste_field(self):
        """Gets the eiendom_norge_liste_field of this HentForetakResponse.  


        :return: The eiendom_norge_liste_field of this HentForetakResponse.  
        :rtype: list[EiendomNorgeListe]
        """
        return self._eiendom_norge_liste_field

    @eiendom_norge_liste_field.setter
    def eiendom_norge_liste_field(self, eiendom_norge_liste_field):
        """Sets the eiendom_norge_liste_field of this HentForetakResponse.


        :param eiendom_norge_liste_field: The eiendom_norge_liste_field of this HentForetakResponse.  
        :type: list[EiendomNorgeListe]
        """

        self._eiendom_norge_liste_field = eiendom_norge_liste_field

    @property
    def fullmakt_foretak_field(self):
        """Gets the fullmakt_foretak_field of this HentForetakResponse.  


        :return: The fullmakt_foretak_field of this HentForetakResponse.  
        :rtype: list[FullmaktForetak]
        """
        return self._fullmakt_foretak_field

    @fullmakt_foretak_field.setter
    def fullmakt_foretak_field(self, fullmakt_foretak_field):
        """Sets the fullmakt_foretak_field of this HentForetakResponse.


        :param fullmakt_foretak_field: The fullmakt_foretak_field of this HentForetakResponse.  
        :type: list[FullmaktForetak]
        """

        self._fullmakt_foretak_field = fullmakt_foretak_field

    @property
    def meldinger_field(self):
        """Gets the meldinger_field of this HentForetakResponse.  


        :return: The meldinger_field of this HentForetakResponse.  
        :rtype: list[Meldinger]
        """
        return self._meldinger_field

    @meldinger_field.setter
    def meldinger_field(self, meldinger_field):
        """Sets the meldinger_field of this HentForetakResponse.


        :param meldinger_field: The meldinger_field of this HentForetakResponse.  
        :type: list[Meldinger]
        """

        self._meldinger_field = meldinger_field

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
        if not isinstance(other, HentForetakResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
